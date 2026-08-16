import asyncio
import logging
import os
import json
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# Admin ID
ADMIN_ID = 8650091524

# Import styles from admin_panel
from admin_panel import GLASS_PANEL_STYLE, format_glass_section, format_stats, admin_log

# Minimal admin handlers for the requested features only

async def handle_finance_action(update: Update, context: ContextTypes.DEFAULT_TYPE, data: str):
    """Handle finance management actions"""
    query = update.callback_query
    action = data.split("_")[-1]
    
    if action == "add":
        await query.edit_message_text(
            f"{GLASS_PANEL_STYLE['header']}\n\n"
            f"💰 افزایش موجودی کاربر\n\n"
            f"برای افزایش موجودی از دستور زیر استفاده کنید:\n\n"
            f"<code>/charge [user_id] [amount]</code>\n\n"
            f"مثال: <code>/charge 123456789 100000</code>\n\n"
            f"{GLASS_PANEL_STYLE['footer']}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data="admin_refresh")]]),
            parse_mode="HTML"
        )
    elif action == "cut":
        await query.edit_message_text(
            f"{GLASS_PANEL_STYLE['header']}\n\n"
            f"💸 کاهش موجودی کاربر\n\n"
            f"برای کاهش موجودی از دستور زیر استفاده کنید:\n\n"
            f"<code>/cut [user_id] [amount]</code>\n\n"
            f"مثال: <code>/cut 123456789 50000</code>\n\n"
            f"{GLASS_PANEL_STYLE['footer']}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data="admin_refresh")]]),
            parse_mode="HTML"
        )
    elif action == "report":
        await show_finance_report(update, context)

async def show_finance_report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show financial report"""
    query = update.callback_query
    
    try:
        with open("data/balances_tapchi.json", "r", encoding="utf-8") as f:
            balances = json.load(f)
        
        message = f"{GLASS_PANEL_STYLE['header']}\n\n"
        
        if balances:
            total_balance = sum(int(balance) for balance in balances.values())
            positive_balances = [int(b) for b in balances.values() if int(b) > 0]
            
            stats = {
                "کل موجودی سیستم": f"{total_balance:,} تومان",
                "کاربران با موجودی مثبت": len(positive_balances),
                "متوسط موجودی": f"{total_balance // len(balances):,} تومان" if balances else "0"
            }
            
            message += format_glass_section("گزارش مالی", format_stats(stats))
        else:
            message += format_glass_section("گزارش مالی", "هیچ اطلاعات مالی یافت نشد.")
            
    except Exception as e:
        message = f"{GLASS_PANEL_STYLE['header']}\n\n"
        message += format_glass_section("خطا", f"خطا در دریافت گزارش مالی: {e}")
    
    keyboard = [[InlineKeyboardButton("🔙 بازگشت", callback_data="admin_refresh")]]
    message += f"\n\n{GLASS_PANEL_STYLE['footer']}"
    
    await query.edit_message_text(
        message,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

async def handle_settings_action(update: Update, context: ContextTypes.DEFAULT_TYPE, data: str):
    """Handle settings management actions"""
    query = update.callback_query
    action = data.split("_")[-1]
    
    if action == "maintenance":
        await toggle_maintenance_mode(update, context)

async def toggle_maintenance_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Toggle maintenance mode"""
    query = update.callback_query
    
    # Get current maintenance status
    current_maintenance = context.bot_data.get("maintenance_mode", False)
    new_maintenance = not current_maintenance
    context.bot_data["maintenance_mode"] = new_maintenance
    
    maintenance_text = "فعال" if new_maintenance else "غیرفعال"
    status_emoji = "🔧" if new_maintenance else "✅"
    
    message = f"{GLASS_PANEL_STYLE['header']}\n\n"
    message += format_glass_section(
        "حالت تعمیر و نگهداری", 
        f"{status_emoji} حالت تعمیر و نگهداری {maintenance_text} شد.\n\n"
        f"{'⚠️ در این حالت کاربران عادی نمی‌توانند از ربات استفاده کنند.' if new_maintenance else '✅ ربات برای همه کاربران فعال است.'}"
    )
    
    admin_log(f"Maintenance mode changed to: {maintenance_text}", "INFO", query.from_user.id)
    
    keyboard = [[InlineKeyboardButton("🔙 بازگشت", callback_data="admin_refresh")]]
    message += f"\n\n{GLASS_PANEL_STYLE['footer']}"
    
    await query.edit_message_text(
        message,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

async def handle_subscription_action(update: Update, context: ContextTypes.DEFAULT_TYPE, data: str):
    """Handle subscription management actions"""
    query = update.callback_query
    action = data.split("_")[-1]
    
    if action == "add":
        await query.edit_message_text(
            f"{GLASS_PANEL_STYLE['header']}\n\n"
            f"➕ افزودن اشتراک\n\n"
            f"برای افزودن اشتراک از دستور زیر استفاده کنید:\n\n"
            f"<code>/add_plan [user_id] [days]</code>\n\n"
            f"مثال: <code>/add_plan 123456789 30</code>\n\n"
            f"{GLASS_PANEL_STYLE['footer']}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data="admin_refresh")]]),
            parse_mode="HTML"
        )
    elif action == "remove":
        await query.edit_message_text(
            f"{GLASS_PANEL_STYLE['header']}\n\n"
            f"➖ کاهش اشتراک\n\n"
            f"برای کاهش اشتراک از دستور زیر استفاده کنید:\n\n"
            f"<code>/cut_plan [user_id] [days]</code>\n\n"
            f"مثال: <code>/cut_plan 123456789 5</code>\n\n"
            f"{GLASS_PANEL_STYLE['footer']}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data="admin_refresh")]]),
            parse_mode="HTML"
        )
    elif action == "list":
        await query.edit_message_text(
            f"{GLASS_PANEL_STYLE['header']}\n\n"
            f"👁 مشاهده اشتراک کاربر\n\n"
            f"برای مشاهده اشتراک کاربر از دستور زیر استفاده کنید:\n\n"
            f"<code>/see_plan [user_id]</code>\n\n"
            f"مثال: <code>/see_plan 123456789</code>\n\n"
            f"{GLASS_PANEL_STYLE['footer']}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data="admin_refresh")]]),
            parse_mode="HTML"
        )

async def handle_accounts_action(update: Update, context: ContextTypes.DEFAULT_TYPE, data: str):
    """Handle accounts actions"""
    query = update.callback_query
    action = data.split("_")[-1]
    
    if action == "check":
        await show_accounts_status(update, context)
    elif action == "limited":
        await show_limited_accounts(update, context)
    elif action == "delete":
        await query.edit_message_text(
            f"{GLASS_PANEL_STYLE['header']}\n\n"
            f"🗑 حذف اکانت\n\n"
            f"این قابلیت به زودی اضافه می‌شود.\n"
            f"فعلاً می‌توانید از پنل مدیریت اکانت استفاده کنید.\n\n"
            f"{GLASS_PANEL_STYLE['footer']}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data="admin_refresh")]]),
            parse_mode="HTML"
        )

async def show_accounts_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show accounts status"""
    query = update.callback_query
    
    try:
        # Count total sessions
        session_dir = "data/sessions"
        total_sessions = 0
        if os.path.exists(session_dir):
            session_files = [f for f in os.listdir(session_dir) if f.endswith('.session')]
            total_sessions = len(session_files)
        
        message = f"{GLASS_PANEL_STYLE['header']}\n\n"
        
        stats = {
            "کل اکانت‌ها": total_sessions,
            "اکانت‌های فعال": context.bot_data.get("active_accounts", 0),
            "اکانت‌های محدود شده": context.bot_data.get("limited_accounts", 0)
        }
        
        message += format_glass_section("وضعیت اکانت‌ها", format_stats(stats))
        
    except Exception as e:
        message = f"{GLASS_PANEL_STYLE['header']}\n\n"
        message += format_glass_section("خطا", f"خطا در دریافت وضعیت اکانت‌ها: {e}")
    
    keyboard = [[InlineKeyboardButton("🔙 بازگشت", callback_data="admin_refresh")]]
    message += f"\n\n{GLASS_PANEL_STYLE['footer']}"
    
    await query.edit_message_text(
        message,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

async def show_limited_accounts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show limited accounts"""
    query = update.callback_query
    
    message = f"{GLASS_PANEL_STYLE['header']}\n\n"
    
    limited_count = context.bot_data.get("limited_accounts_count", 0)
    
    if limited_count > 0:
        message += format_glass_section(f"اکانت‌های محدود شده ({limited_count} اکانت)", "لیست اکانت‌های محدود شده در حال توسعه است.")
    else:
        message += format_glass_section("اکانت‌های محدود شده", "هیچ اکانت محدود شده‌ای یافت نشد. عالی!")
    
    keyboard = [[InlineKeyboardButton("🔙 بازگشت", callback_data="admin_refresh")]]
    message += f"\n\n{GLASS_PANEL_STYLE['footer']}"
    
    await query.edit_message_text(
        message,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

async def handle_stats_action(update: Update, context: ContextTypes.DEFAULT_TYPE, data: str):
    """Handle stats actions"""
    query = update.callback_query
    action = data.split("_")[-1]
    
    if action == "users":
        await show_user_stats(update, context)
    elif action == "messages":
        await show_message_stats(update, context)

async def show_user_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show user and subscription statistics"""
    query = update.callback_query
    
    try:
        with open("data/subscriptions.json", "r", encoding="utf-8") as f:
            subscriptions = json.load(f)
        
        message = f"{GLASS_PANEL_STYLE['header']}\n\n"
        
        # Calculate stats
        total_users = len(subscriptions)
        active_subs = 0
        trial_users = 0
        premium_users = 0
        
        now = datetime.now()
        
        for user_subs in subscriptions.values():
            iterable = user_subs if isinstance(user_subs, list) else [user_subs]
            for sub in iterable:
                try:
                    expiry_dt = datetime.fromisoformat(sub.get("expiry"))
                    if expiry_dt > now:
                        active_subs += 1
                    
                    if sub.get("is_trial", False):
                        trial_users += 1
                    else:
                        premium_users += 1
                    break
                except Exception:
                    continue
        
        stats = {
            "کل کاربران": total_users,
            "اشتراک‌های فعال": active_subs,
            "کاربران آزمایشی": trial_users,
            "کاربران پرمیوم": premium_users
        }
        
        message += format_glass_section("آمار کاربران و اشتراک‌ها", format_stats(stats))
        
    except Exception as e:
        message = f"{GLASS_PANEL_STYLE['header']}\n\n"
        message += format_glass_section("خطا", f"خطا در دریافت آمار: {e}")
    
    keyboard = [[InlineKeyboardButton("🔙 بازگشت", callback_data="admin_refresh")]]
    message += f"\n\n{GLASS_PANEL_STYLE['footer']}"
    
    await query.edit_message_text(
        message,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

async def show_message_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show message statistics"""
    query = update.callback_query
    
    message = f"{GLASS_PANEL_STYLE['header']}\n\n"
    
    # Get message stats from bot_data
    total_messages = context.bot_data.get("total_messages_sent", 0)
    daily_messages = context.bot_data.get("daily_messages", 0)
    failed_messages = context.bot_data.get("failed_messages", 0)
    
    stats = {
        "کل پیام‌های ارسالی": total_messages,
        "پیام‌های ارسالی امروز": daily_messages,
        "پیام‌های ناموفق": failed_messages,
        "نرخ موفقیت": f"{((total_messages - failed_messages) / max(total_messages, 1) * 100):.1f}%" if total_messages > 0 else "100%"
    }
    
    message += format_glass_section("آمار پیام‌ها", format_stats(stats))
    
    keyboard = [[InlineKeyboardButton("🔙 بازگشت", callback_data="admin_refresh")]]
    message += f"\n\n{GLASS_PANEL_STYLE['footer']}"
    
    await query.edit_message_text(
        message,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

async def handle_broadcast_action(update: Update, context: ContextTypes.DEFAULT_TYPE, data: str):
    """Handle broadcast actions"""
    query = update.callback_query
    action = data.split("_")[-1]
    
    if action == "text":
        await query.edit_message_text(
            f"{GLASS_PANEL_STYLE['header']}\n\n"
            f"📢 ارسال پیام همگانی\n\n"
            f"برای ارسال پیام همگانی از دستور زیر استفاده کنید:\n\n"
            f"<code>/send_msg</code>\n\n"
            f"سپس پیام خود را ارسال کنید.\n\n"
            f"{GLASS_PANEL_STYLE['footer']}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data="admin_refresh")]]),
            parse_mode="HTML"
        )

# Text input handler for admin panel (minimal implementation)
async def handle_admin_text_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text input for admin panel operations (minimal)"""
    user_id = update.effective_user.id
    
    # Check if user is admin
    if user_id != 7135477742:
        return False
    
    # For now, just return False since we're using commands
    # This can be expanded later if needed
    return False

# ==================== TICKET MANAGEMENT FOR ADMIN ====================

async def handle_admin_tickets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show admin ticket management panel"""
    query = update.callback_query
    user_id = update.effective_user.id
    
    if user_id != ADMIN_ID:
        await query.edit_message_text(f"{GLASS_PANEL_STYLE['error']}شما دسترسی به این بخش را ندارید.", parse_mode="HTML")
        return
    
    # Import ticket functions from main file
    try:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from Tapchi import get_open_tickets, load_tickets
    except ImportError:
        await query.edit_message_text("❌ خطا در بارگذاری سیستم تیکت.", parse_mode="HTML")
        return
    
    open_tickets = get_open_tickets()
    all_tickets = load_tickets()
    closed_tickets = [t for t in all_tickets if t["status"] == "closed"]
    
    message = (
        f"🎫 <b>مدیریت تیکت‌های پشتیبانی</b>\n\n"
        f"📊 <b>آمار کلی:</b>\n"
        f"🟢 تیکت‌های باز: <code>{len(open_tickets)}</code>\n"
        f"🔴 تیکت‌های بسته: <code>{len(closed_tickets)}</code>\n"
        f"📊 کل تیکت‌ها: <code>{len(all_tickets)}</code>\n\n"
    )
    
    if not open_tickets:
        message += "✅ <b>هیچ تیکت بازی وجود ندارد!</b>\n"
        keyboard = [
            [InlineKeyboardButton("📊 آمار تیکت‌ها", callback_data="admin_ticket_stats")],
            [InlineKeyboardButton("🔙 بازگشت به پنل", callback_data="admin_refresh")]
        ]
    else:
        message += "📋 <b>تیکت‌های باز:</b>\n\n"
        
        keyboard = []
        for i, ticket in enumerate(open_tickets[:10]):  # Show max 10 tickets
            replies_count = len(ticket["replies"])
            
            # Format date
            try:
                date_obj = datetime.fromisoformat(ticket["timestamp"])
                date_str = date_obj.strftime("%m/%d")
            except:
                date_str = "N/A"
            
            button_text = f"🎫 {ticket['id']} - {ticket.get('user_name', 'نامشخص')} ({replies_count} پاسخ)"
            keyboard.append([InlineKeyboardButton(button_text, callback_data=f"view_ticket_{ticket['id']}")])
        
        keyboard.append([InlineKeyboardButton("📊 آمار تیکت‌ها", callback_data="admin_ticket_stats")])
        keyboard.append([InlineKeyboardButton("🔄 به‌روزرسانی", callback_data="admin_tickets")])
        keyboard.append([InlineKeyboardButton("🔙 بازگشت به پنل", callback_data="admin_refresh")])
    
    markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(message, reply_markup=markup, parse_mode="HTML")