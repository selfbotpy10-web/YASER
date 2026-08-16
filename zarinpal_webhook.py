"""
ZarinPal Webhook Handler for automatic payment verification
This script should be deployed to handle callback URLs from ZarinPal
"""

from flask import Flask, request, jsonify, redirect
import json
import logging
from datetime import datetime, timedelta
import sys
import os

# Add the project directory to Python path to import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from zarinpal_payment import zarinpal, get_pending_payment, remove_pending_payment
from admin_panel import admin_log

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load configuration
try:
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        BOT_TOKEN = config.get("bot_token", "")
        ADMIN_ID = config.get("admin_id", 0)
except:
    # Fallback to environment variables or hardcoded values
    BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
    ADMIN_ID = int(os.getenv("ADMIN_ID", "7135477742"))

# Load subscription data functions
def load_subscriptions():
    """Load user subscriptions from file"""
    try:
        with open("data/user_subscriptions.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except Exception as e:
        logger.error(f"Error loading subscriptions: {e}")
        return {}

def save_subscriptions(subscriptions):
    """Save user subscriptions to file"""
    try:
        os.makedirs("data", exist_ok=True)
        with open("data/user_subscriptions.json", "w", encoding="utf-8") as f:
            json.dump(subscriptions, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        logger.error(f"Error saving subscriptions: {e}")
        return False

@app.route('/zarinpal_callback', methods=['GET', 'POST'])
def zarinpal_callback():
    """Handle ZarinPal payment callback"""
    try:
        # Get parameters from callback
        if request.method == 'GET':
            authority = request.args.get('Authority')
            status = request.args.get('Status')
        else:
            authority = request.form.get('Authority')
            status = request.form.get('Status')
        
        logger.info(f"ZarinPal callback received: Authority={authority}, Status={status}")
        
        if not authority:
            logger.error("No authority provided in callback")
            return redirect("https://t.me/your_bot_username?start=payment_error")
        
        # Get pending payment data
        payment_data = get_pending_payment(authority)
        if not payment_data:
            logger.error(f"No pending payment found for authority: {authority}")
            return redirect("https://t.me/your_bot_username?start=payment_not_found")
        
        user_id = payment_data["user_id"]
        amount = payment_data["amount"]
        subscription_data = payment_data["subscription_data"]
        
        if status == "OK":
            # Payment successful, verify it
            success, result = zarinpal.verify_payment(amount, authority)
            
            if success:
                ref_id = result.get("ref_id")
                logger.info(f"Payment verification successful: RefID={ref_id}, User={user_id}")
                
                # Process subscription
                if process_subscription_payment(user_id, subscription_data, ref_id, authority):
                    # Remove pending payment
                    remove_pending_payment(authority)
                    
                    # Log successful payment
                    admin_log(f"Webhook: ZarinPal payment successful - User {user_id}, Amount {amount}, RefID {ref_id}", "INFO")
                    
                    # Redirect to bot with success message
                    return redirect(f"https://t.me/your_bot_username?start=payment_success_{ref_id}")
                else:
                    logger.error(f"Failed to process subscription for user {user_id}")
                    return redirect("https://t.me/your_bot_username?start=subscription_error")
            else:
                error_code = result.get("data", {}).get("code", -1) if result.get("data") else -1
                logger.error(f"Payment verification failed: Authority={authority}, Error={error_code}")
                
                # Remove pending payment on failure
                remove_pending_payment(authority)
                
                # Log failed payment
                admin_log(f"Webhook: ZarinPal payment verification failed - User {user_id}, Authority {authority}, Error {error_code}", "WARNING")
                
                return redirect(f"https://t.me/your_bot_username?start=payment_failed_{error_code}")
        else:
            # Payment cancelled or failed
            logger.info(f"Payment cancelled by user: Authority={authority}, User={user_id}")
            
            # Remove pending payment
            remove_pending_payment(authority)
            
            # Log cancelled payment
            admin_log(f"Webhook: Payment cancelled by user {user_id}, Authority {authority}", "INFO")
            
            return redirect("https://t.me/your_bot_username?start=payment_cancelled")
            
    except Exception as e:
        logger.error(f"Error in ZarinPal callback handler: {e}")
        return redirect("https://t.me/your_bot_username?start=webhook_error")

def process_subscription_payment(user_id, subscription_data, ref_id, authority):
    """Process subscription after successful payment"""
    try:
        # Load current subscriptions
        user_subscriptions = load_subscriptions()
        
        # Check if this is an upgrade or regular subscription
        if subscription_data.get("type") == "upgrade":
            # Handle upgrade payment
            allowed = subscription_data["allowed"]
            final_price = subscription_data["final_price"]
            duration = subscription_data["duration"]
            
            # Get current subscriptions
            subs = user_subscriptions.get(str(user_id), [])
            if isinstance(subs, dict):
                subs = [subs]
            elif isinstance(subs, str):
                try:
                    subs = json.loads(subs)
                    if isinstance(subs, dict):
                        subs = [subs]
                    elif not isinstance(subs, list):
                        subs = []
                except:
                    subs = []
            elif not isinstance(subs, list):
                subs = []
            
            # Cancel the old subscription by setting expiry to now
            now = datetime.now()
            for s in subs:
                try:
                    expiry = datetime.fromisoformat(s["expiry"])
                    if expiry > now:
                        s["expiry"] = now.isoformat()
                        break
                except:
                    continue
            
            # Add new subscription
            expiry = datetime.utcnow() + timedelta(days=duration)
            sub = {
                "allowed_accounts": allowed,
                "expiry": expiry.isoformat(),
                "price": final_price,
                "payment_method": "zarinpal_webhook",
                "ref_id": ref_id,
                "authority": authority
            }
            subs.append(sub)
            user_subscriptions[str(user_id)] = subs
            
        else:
            # Handle regular subscription payment
            allowed = subscription_data["allowed"]
            price = subscription_data["price"]
            duration = subscription_data["duration"]
            
            # Get current subscriptions
            subs = user_subscriptions.get(str(user_id), [])
            if isinstance(subs, dict):
                subs = [subs]
            
            # Add new subscription
            expiry = datetime.utcnow() + timedelta(days=duration)
            sub = {
                "allowed_accounts": allowed, 
                "expiry": expiry.isoformat(), 
                "price": price,
                "payment_method": "zarinpal_webhook",
                "ref_id": ref_id,
                "authority": authority
            }
            subs.append(sub)
            user_subscriptions[str(user_id)] = subs
        
        # Save updated subscriptions
        return save_subscriptions(user_subscriptions)
        
    except Exception as e:
        logger.error(f"Error processing subscription payment: {e}")
        return False

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "zarinpal_webhook"
    })

@app.route('/payment_status/<authority>', methods=['GET'])
def check_payment_status(authority):
    """Check payment status endpoint for manual verification"""
    try:
        payment_data = get_pending_payment(authority)
        if payment_data:
            return jsonify({
                "status": "pending",
                "user_id": payment_data["user_id"],
                "amount": payment_data["amount"],
                "timestamp": payment_data["timestamp"]
            })
        else:
            return jsonify({
                "status": "not_found",
                "message": "Payment not found or already processed"
            })
    except Exception as e:
        logger.error(f"Error checking payment status: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs("data", exist_ok=True)
    
    # Run the Flask app
    # In production, use a proper WSGI server like Gunicorn
    app.run(host='0.0.0.0', port=5000, debug=False)
