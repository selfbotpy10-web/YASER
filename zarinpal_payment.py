"""
ZarinPal Payment Gateway Integration for Telegram Bot
Handles payment requests and verification for subscription purchases
"""

import json
import requests
import logging
import os
from typing import Dict, Optional, Tuple
from datetime import datetime

# Load configuration
def load_config():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
            return config.get("zarinpal", {})
    except FileNotFoundError:
        return {}
    except Exception as e:
        logging.error(f"Error loading config: {e}")
        return {}

# ZarinPal Configuration
config = load_config()
ZARINPAL_MERCHANT_ID = config.get("merchant_id", "YOUR_MERCHANT_ID_HERE")  # Replace with your actual merchant ID
SANDBOX_MODE = config.get("sandbox_mode", True)
if SANDBOX_MODE:
    # Sandbox URLs for testing
    ZARINPAL_REQUEST_URL = "https://sandbox.zarinpal.com/pg/v4/payment/request.json"
    ZARINPAL_VERIFY_URL = "https://sandbox.zarinpal.com/pg/v4/payment/verify.json"
    ZARINPAL_GATEWAY_URL = "https://sandbox.zarinpal.com/pg/StartPay/"
else:
    # Production URLs
    ZARINPAL_REQUEST_URL = "https://payment.zarinpal.com/pg/v4/payment/request.json"
    ZARINPAL_VERIFY_URL = "https://payment.zarinpal.com/pg/v4/payment/verify.json"
    ZARINPAL_GATEWAY_URL = "https://payment.zarinpal.com/pg/StartPay/"

class ZarinPalPayment:
    def __init__(self, merchant_id: str = ZARINPAL_MERCHANT_ID):
        self.merchant_id = merchant_id
        self.logger = logging.getLogger(__name__)
    
    def create_payment_request(self, amount: int, description: str, callback_url: str, 
                             mobile: str = None, email: str = None, order_id: str = None) -> Tuple[bool, Dict]:
        """
        Create a payment request to ZarinPal
        
        Args:
            amount: Payment amount in Tomans
            description: Payment description
            callback_url: URL to redirect after payment
            mobile: User's mobile number (optional)
            email: User's email (optional)
            order_id: Order ID for tracking (optional)
            
        Returns:
            Tuple of (success: bool, response_data: dict)
        """
        try:
            # Prepare payment data
            payment_data = {
                "merchant_id": self.merchant_id,
                "amount": str(amount),
                "currency": "IRT",  # Tomans
                "description": description,
                "callback_url": callback_url
            }
            
            # Add metadata if provided
            metadata = {}
            if mobile:
                metadata["mobile"] = mobile
            if email:
                metadata["email"] = email
            if order_id:
                metadata["order_id"] = order_id
            
            if metadata:
                payment_data["metadata"] = metadata
            
            self.logger.info(f"Creating ZarinPal payment request for amount: {amount}")
            
            # Send request to ZarinPal
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            
            response = requests.post(
                ZARINPAL_REQUEST_URL,
                json=payment_data,
                headers=headers,
                timeout=30
            )
            
            response.raise_for_status()
            result = response.json()
            
            self.logger.info(f"ZarinPal payment request response: {result}")
            
            # Check if request was successful
            if result.get("data", {}).get("code") == 100:
                return True, result["data"]
            else:
                self.logger.error(f"ZarinPal payment request failed: {result}")
                return False, result
                
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Network error during ZarinPal payment request: {e}")
            return False, {"error": f"Network error: {str(e)}"}
        except Exception as e:
            self.logger.error(f"Error creating ZarinPal payment request: {e}")
            return False, {"error": f"Unexpected error: {str(e)}"}
    
    def verify_payment(self, amount: int, authority: str) -> Tuple[bool, Dict]:
        """
        Verify a payment with ZarinPal
        
        Args:
            amount: Original payment amount in Tomans
            authority: Authority code from payment callback
            
        Returns:
            Tuple of (success: bool, verification_data: dict)
        """
        try:
            verify_data = {
                "merchant_id": self.merchant_id,
                "amount": str(amount),
                "authority": authority
            }
            
            self.logger.info(f"Verifying ZarinPal payment with authority: {authority}")
            
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            
            response = requests.post(
                ZARINPAL_VERIFY_URL,
                json=verify_data,
                headers=headers,
                timeout=30
            )
            
            response.raise_for_status()
            result = response.json()
            
            self.logger.info(f"ZarinPal verification response: {result}")
            
            # Check verification result
            data = result.get("data", {})
            code = data.get("code")
            
            if code == 100:
                # Payment successful
                return True, data
            elif code == 101:
                # Payment already verified
                self.logger.warning(f"Payment already verified for authority: {authority}")
                return True, data
            else:
                # Payment failed or other error
                self.logger.error(f"ZarinPal payment verification failed: {result}")
                return False, result
                
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Network error during ZarinPal payment verification: {e}")
            return False, {"error": f"Network error: {str(e)}"}
        except Exception as e:
            self.logger.error(f"Error verifying ZarinPal payment: {e}")
            return False, {"error": f"Unexpected error: {str(e)}"}
    
    def get_payment_url(self, authority: str) -> str:
        """
        Generate payment URL for redirecting user to ZarinPal gateway
        
        Args:
            authority: Authority code received from payment request
            
        Returns:
            Payment URL string
        """
        return f"{ZARINPAL_GATEWAY_URL}{authority}"
    
    def format_error_message(self, error_code: int) -> str:
        """
        Convert ZarinPal error codes to user-friendly Persian messages
        
        Args:
            error_code: ZarinPal error code
            
        Returns:
            Persian error message
        """
        error_messages = {
            -9: "خطای اعتبارسنجی",
            -10: "ای پی یا مرچنت کد پذیرنده صحیح نمی‌باشد",
            -11: "مرچنت کد فعال نمی‌باشد، لطفاً با تیم پشتیبانی ما تماس بگیرید",
            -12: "تلاش بیش از حد در یک بازه زمانی کوتاه",
            -15: "ترمینال شما به حالت تعلیق در آمده، با تیم پشتیبانی تماس بگیرید",
            -16: "سطح تأیید پذیرنده پایین‌تر از سطح نقره‌ای می‌باشد",
            -30: "اجازه دسترسی به تسویه اشتراکی شناور ندارید",
            -31: "حساب بانکی تسویه را به پنل اضافه کنید، مقادیر وارد شده واسه تسویه نامعتبر است",
            -32: "مبلغ وارد شده از مبلغ کل تراکنش بیشتر است",
            -33: "درصد های وارد شده صحیح نمی‌باشد",
            -34: "مبلغ از کمترین میزان قابل تسویه کمتر است",
            -35: "تعداد روز های تسویه عدد صحیحی نمی‌باشد",
            -40: "پارامترهای اضافی نامعتبر، شما تنها می‌توانید یکی از پارامترهای زیر را ارسال کنید",
            -50: "مبلغ پرداخت شده با مقدار مبلغ در وریفای متفاوت است",
            -51: "پرداخت ناموفق",
            -52: "خطای غیر منتظره‌ای رخ داده است",
            -53: "اتوریتی برای این مرچنت کد نمی‌باشد",
            -54: "اتوریتی نامعتبر است",
            100: "پرداخت موفقیت آمیز",
            101: "پرداخت تأیید شده"
        }
        
        return error_messages.get(error_code, f"خطای نامشخص (کد: {error_code})")

# Global instance for easy access
zarinpal = ZarinPalPayment()

# Payment storage for tracking pending payments
pending_payments = {}

def store_pending_payment(authority: str, user_id: int, amount: int, 
                         subscription_data: dict, timestamp: str = None):
    """Store pending payment data for verification"""
    if timestamp is None:
        timestamp = datetime.now().isoformat()
    
    pending_payments[authority] = {
        "user_id": user_id,
        "amount": amount,
        "subscription_data": subscription_data,
        "timestamp": timestamp,
        "status": "pending"
    }
    
    # Save to file for persistence
    try:
        with open("data/pending_payments.json", "w", encoding="utf-8") as f:
            json.dump(pending_payments, f, ensure_ascii=False, indent=2)
    except Exception as e:
        logging.error(f"Error saving pending payments: {e}")

def get_pending_payment(authority: str) -> Optional[dict]:
    """Get pending payment data by authority"""
    return pending_payments.get(authority)

def remove_pending_payment(authority: str):
    """Remove pending payment after processing"""
    if authority in pending_payments:
        del pending_payments[authority]
        try:
            with open("data/pending_payments.json", "w", encoding="utf-8") as f:
                json.dump(pending_payments, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logging.error(f"Error saving pending payments after removal: {e}")

def load_pending_payments():
    """Load pending payments from file"""
    global pending_payments
    try:
        with open("data/pending_payments.json", "r", encoding="utf-8") as f:
            pending_payments = json.load(f)
    except FileNotFoundError:
        pending_payments = {}
    except Exception as e:
        logging.error(f"Error loading pending payments: {e}")
        pending_payments = {}

# Load pending payments on module import
load_pending_payments()
