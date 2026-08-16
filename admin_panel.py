import asyncio
import logging
import os
import json
from datetime import datetime
import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

# Import from main file
ADMIN_ID = 8650091524

# Glass-like admin panel styling
GLASS_PANEL_STYLE = {
    "header": "🔷 <b>پنل مدیریت شیشه‌ای تپچی</b> 🔷",
    "footer": "⚡️ <b>تپچی پیشرفته</b> | نسخه ۲.۰ | طراحی شده با ❤️",
    "section_start": "🔹 <b>",
    "section_end": "</b> 🔹",
    "item_bullet": "• ",
    "highlight_start": "<code>",
    "highlight_end": "</code>",
    "warning": "⚠️ ",
    "success": "✅ ",
    "error": "❌ ",
    "info": "ℹ️ "
}

# Enhanced logging function
def admin_log(message, level="INFO", user_id=None):
    """Log messages with enhanced formatting for admin panel"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_info = f"[USER:{user_id}] " if user_id else ""
    log_message = f"[{timestamp}] [{level}] {user_info}{message}"
    
    if level == "ERROR":
        logging.error(log_message)
    elif level == "WARNING":
        logging.warning(log_message)
    else:
        logging.info(log_message)
    
    # Store in admin logs file
    try:
        os.makedirs("data/admin_logs", exist_ok=True)
        log_file = f"data/admin_logs/admin_{datetime.now().strftime('%Y-%m-%d')}.log"
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log_message + "\n")
    except Exception as e:
        logging.error(f"Failed to write to admin log file: {e}")

# Helper function to create glass-like formatted sections
def format_glass_section(title, content):
    """Format a section with glass-like styling"""
    return f"\n{GLASS_PANEL_STYLE['section_start']}{title}{GLASS_PANEL_STYLE['section_end']}\n\n{content}\n"

# Helper function to format statistics
def format_stats(stats_dict):
    """Format statistics dictionary into readable text"""
    result = ""
    for key, value in stats_dict.items():
        result += f"{GLASS_PANEL_STYLE['item_bullet']}{key}: {GLASS_PANEL_STYLE['highlight_start']}{value}{GLASS_PANEL_STYLE['highlight_end']}\n"
    return result

# Main admin panel handler
async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /admin command and display the glass-like admin panel"""
    user_id = update.effective_user.id
    
    # Check if user is admin
    if user_id != ADMIN_ID:
        message_text = f"{GLASS_PANEL_STYLE['error']}شما دسترسی به پنل مدیریت را ندارید."
        
        # Handle both callback query and regular message
        query = getattr(update, "callback_query", None)
        if query:
            await query.answer("دسترسی غیرمجاز", show_alert=True)
            try:
                await query.edit_message_text(message_text, parse_mode="HTML")
            except:
                await query.message.reply_text(message_text, parse_mode="HTML")
        else:
            await update.message.reply_text(message_text, parse_mode="HTML")
        admin_log(f"Unauthorized access attempt to admin panel", "WARNING", user_id)
        return
    
    # Log admin panel access
    admin_log(f"Admin panel accessed", "INFO", user_id)
    
    # Get system stats
    try:
        import psutil
        memory = psutil.virtual_memory()
        memory_usage = f"{memory.percent}%"
        cpu_usage = f"{psutil.cpu_percent()}%"
        disk = psutil.disk_usage('/')
        disk_usage = f"{disk.percent}%"
    except ImportError:
        memory_usage = "N/A"
        cpu_usage = "N/A"
        disk_usage = "N/A"
    
    # Get bot stats
    try:
        with open("data/user_subscriptions.json", "r") as f:
            subscriptions = json.load(f)
        total_users = len(subscriptions)
        
        # Count active subscriptions
        active_subs = 0
        tehran = pytz.timezone("Asia/Tehran")
        now = datetime.now(tehran)
        
        for user_subs in subscriptions.values():
            if isinstance(user_subs, dict):
                user_subs = [user_subs]
            
            for sub in user_subs:
                try:
                    expiry = datetime.fromisoformat(sub["expiry"])
                    if expiry.tzinfo is None:
                        expiry = tehran.localize(expiry)
                    else:
                        expiry = expiry.astimezone(tehran)
                    if expiry > now:
                        active_subs += 1
                except:
                    continue
    except:
        total_users = 0
        active_subs = 0
    
    # Count total accounts
    try:
        session_dir = "data/sessions"
        if os.path.exists(session_dir):
            session_files = [f for f in os.listdir(session_dir) if f.endswith('.session')]
            total_accounts = len(session_files)
        else:
            total_accounts = 0
    except:
        total_accounts = 0
    
    # Create admin panel message
    message = f"{GLASS_PANEL_STYLE['header']}\n\n"
    
    # Add system stats section
    message += f"{GLASS_PANEL_STYLE['section_start']}وضعیت سیستم{GLASS_PANEL_STYLE['section_end']}\n\n"
    message += f"{GLASS_PANEL_STYLE['item_bullet']}حافظه: {GLASS_PANEL_STYLE['highlight_start']}{memory_usage}{GLASS_PANEL_STYLE['highlight_end']}\n"
    message += f"{GLASS_PANEL_STYLE['item_bullet']}پردازنده: {GLASS_PANEL_STYLE['highlight_start']}{cpu_usage}{GLASS_PANEL_STYLE['highlight_end']}\n"
    message += f"{GLASS_PANEL_STYLE['item_bullet']}دیسک: {GLASS_PANEL_STYLE['highlight_start']}{disk_usage}{GLASS_PANEL_STYLE['highlight_end']}\n"
    message += f"{GLASS_PANEL_STYLE['item_bullet']}زمان اجرا: {GLASS_PANEL_STYLE['highlight_start']}{context.bot_data.get('uptime', 'نامشخص')}{GLASS_PANEL_STYLE['highlight_end']}\n\n"
    
    # Add bot stats section
    message += f"{GLASS_PANEL_STYLE['section_start']}آمار ربات{GLASS_PANEL_STYLE['section_end']}\n\n"
    message += f"{GLASS_PANEL_STYLE['item_bullet']}کل کاربران: {GLASS_PANEL_STYLE['highlight_start']}{total_users}{GLASS_PANEL_STYLE['highlight_end']}\n"
    message += f"{GLASS_PANEL_STYLE['item_bullet']}اشتراک‌های فعال: {GLASS_PANEL_STYLE['highlight_start']}{active_subs}{GLASS_PANEL_STYLE['highlight_end']}\n"
    message += f"{GLASS_PANEL_STYLE['item_bullet']}تعداد اکانت‌ها: {GLASS_PANEL_STYLE['highlight_start']}{total_accounts}{GLASS_PANEL_STYLE['highlight_end']}\n"
    message += f"{GLASS_PANEL_STYLE['item_bullet']}پیام‌های امروز: {GLASS_PANEL_STYLE['highlight_start']}{context.bot_data.get('daily_messages', 0)}{GLASS_PANEL_STYLE['highlight_end']}\n\n"
    
    # Create admin panel keyboard with organized layout
    keyboard = [
        [InlineKeyboardButton("💰 افزایش موجودی", callback_data="admin_finance_add"), 
         InlineKeyboardButton("💸 کاهش موجودی", callback_data="admin_finance_cut")],
        [InlineKeyboardButton("📊 گزارش مالی", callback_data="admin_finance_report"),
         InlineKeyboardButton("🔧 حالت تعمیر", callback_data="admin_settings_maintenance")],
        [InlineKeyboardButton("➕ افزودن اشتراک", callback_data="admin_sub_add"), 
         InlineKeyboardButton("➖ کاهش اشتراک", callback_data="admin_sub_remove")],
        [InlineKeyboardButton("👁‍🗨 مشاهده اشتراک", callback_data="admin_sub_list"),
         InlineKeyboardButton("📱 وضعیت اکانت‌ها", callback_data="admin_accounts_check")],
        [InlineKeyboardButton("⛔️ اکانت‌های محدود", callback_data="admin_accounts_limited"),
         InlineKeyboardButton("🗑 حذف اکانت", callback_data="admin_accounts_delete")],
        [InlineKeyboardButton("📈 آمار کاربران", callback_data="admin_stats_users"),
         InlineKeyboardButton("📨 آمار پیام‌ها", callback_data="admin_stats_messages")],
        [InlineKeyboardButton("🎫 مدیریت تیکت‌ها", callback_data="admin_tickets")],
        [InlineKeyboardButton("📢 ارسال همگانی", callback_data="admin_broadcast_text"),
         InlineKeyboardButton("🔄 بروزرسانی", callback_data="admin_refresh")]
    ]
    
    # Add footer
    message += f"{GLASS_PANEL_STYLE['footer']}"
    
    # Send or edit the admin panel
    query = getattr(update, "callback_query", None)
    if query:
        try:
            await query.edit_message_text(
                message,
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode="HTML"
            )
        except:
            await query.message.reply_text(
                message,
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode="HTML"
            )
    else:
        await update.message.reply_text(
            message,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="HTML"
        )

# Handler for admin panel button clicks
async def admin_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle admin panel button clicks"""
    query = update.callback_query
    await query.answer()
    
    # Extract the section from callback data
    data = query.data
    user_id = update.effective_user.id
    
    # Check if user is admin
    if user_id != ADMIN_ID:
        await query.edit_message_text(
            f"{GLASS_PANEL_STYLE['error']}شما دسترسی به پنل مدیریت را ندارید.",
            parse_mode="HTML"
        )
        return
    
    if data == "admin_refresh" or data == "admin_back":
        await admin_panel(update, context)
        return
    
    # Route to specific handlers in admin_handlers.py
    try:
        if data.startswith("admin_finance_"):
            from admin_handlers import handle_finance_action
            await handle_finance_action(update, context, data)
        elif data.startswith("admin_settings_"):
            from admin_handlers import handle_settings_action
            await handle_settings_action(update, context, data)
        elif data.startswith("admin_sub_"):
            from admin_handlers import handle_subscription_action
            await handle_subscription_action(update, context, data)
        elif data.startswith("admin_accounts_"):
            from admin_handlers import handle_accounts_action
            await handle_accounts_action(update, context, data)
        elif data.startswith("admin_stats_"):
            from admin_handlers import handle_stats_action
            await handle_stats_action(update, context, data)
        elif data.startswith("admin_broadcast_"):
            from admin_handlers import handle_broadcast_action
            await handle_broadcast_action(update, context, data)
        elif data == "admin_tickets":
            from admin_handlers import handle_admin_tickets
            await handle_admin_tickets(update, context)
        else:
            await query.edit_message_text(f"{GLASS_PANEL_STYLE['error']}دستور نامشخص.", parse_mode="HTML")
    except Exception as e:
        admin_log(f"خطا در پردازش دکمه ادمین: {e}", "ERROR", user_id)
        await query.edit_message_text(
            f"{GLASS_PANEL_STYLE['error']}خطا در پردازش درخواست: {str(e)}\n\n"
            f"لطفاً دوباره تلاش کنید یا با پشتیبانی تماس بگیرید.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data="admin_refresh")]]),
            parse_mode="HTML"
        )