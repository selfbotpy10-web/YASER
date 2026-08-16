import sys

sys.stdout.write(">>> ABSOLUTE TOP OF FILE REACHED <<<\n")

sys.stdout.flush()

import asyncio

# Import admin panel functions
try:
    from admin_panel import admin_panel, admin_button_handler, admin_log
except ImportError:
    # Fallback functions if admin panel is not available
    def admin_log(msg, level="INFO", user_id=None):
        logging.info(f"[ADMIN LOG] {msg}")
    
    async def admin_panel(update, context):
        await update.message.reply_text("پنل مدیریت در دسترس نیست.")
    
    async def admin_button_handler(update, context):
        pass

try:
    from admin_handlers import handle_admin_text_input
except ImportError:
    async def handle_admin_text_input(*args, **kwargs):
        return False

task_queue = asyncio.Queue()
# Standard Library

import os
import json
import math
import uuid
import random
import threading
import logging
import threading

accounts_lock = threading.Lock()
session_locks = {}  

logging.getLogger('telethon').setLevel(logging.WARNING)

import re
from pathlib import Path
from datetime import datetime, timedelta
import sys
import os
sys.stderr = sys.stdout

# 3rd-Party Libraries

import pytz
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.orm import sessionmaker, declarative_base

from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    ContextTypes,
    filters,
    JobQueue,
    Job
)

from telegram.error import BadRequest
from sqlalchemy.orm.attributes import flag_modified
from telethon import TelegramClient
from telethon.errors import FloodWaitError
from telethon.tl.types import Channel, Chat, InputFile
from telethon.tl.types import User
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateProfileRequest
import multiprocessing
from telethon.events import NewMessage
from telethon import events
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import BadRequest
from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import Message

# ZarinPal payment gateway
from zarinpal_payment import zarinpal, store_pending_payment, get_pending_payment, remove_pending_payment

# Set up base logging
logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
logging.info("Current working directory: " + os.getcwd())

# Silence noisy third-party loggers
logging.getLogger("httpx").setLevel(logging.WARNING)


########## LOGGING ############
########## LOGGING ############
########## LOGGING ############
########## LOGGING ############
########## LOGGING ############


MONSHI_DEBUG = True

def debug_monshi(msg):
    if MONSHI_DEBUG:
        print(f"[MONSHI DEBUG] {msg}", flush=True)
        admin_log(f"منشی: {msg}", "DEBUG")
        
########## LOGGING ############

PHOTO_DEBUG = False

def debug_photo(msg):
    if PHOTO_DEBUG:
        print(f"[PHOTO DEBUG] {msg}", flush=True)     
           
########## LOGGING ############

BANNER_DEBUG = False  

def debug_banner(msg):
    if BANNER_DEBUG:
        print(f"[BANNER DEBUG] {msg}", flush=True)

#BANNER_DEBUG = True  
#DEBUG_PHONES = {
#    "+989331790203",
#    "+989339347375",
#    "+989155446338",
#    "+989104321206"
#}

#def debug_banner(msg, phone=None):
#    if BANNER_DEBUG and (phone is None or phone in DEBUG_PHONES):
#        print(f"[BANNER DEBUG] {msg}", flush=True)
        
########## LOGGING ############

CLOCK_DEBUG = False

def debug_clock(msg):
    if CLOCK_DEBUG:
        print(f"[CLOCK DEBUG] {msg}", flush=True)
        
########## LOGGING ############

GROUPS_UPDATE_DEBUG = False
 
def groups_update_debug(msg):
    if GROUPS_UPDATE_DEBUG:
        print(f"[UPDATE GROUP] {msg}", flush=True)      

########## LOGGING ############

GROUPS_DEBUG = False

def debug_groups(msg):
    if GROUPS_DEBUG:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[Groups DEBUG {ts}] {msg}", flush=True)

########## LOGGING ############

ERROR_DEBUG = True

def error_debug(msg):
    if ERROR_DEBUG:
        print(f"[ERROR DEBUG] {msg}", flush=True)
        admin_log(f"{msg}", "ERROR")                                                                                         
  
########## LOGGING ############
                                                                                    
PV_DEBUG = False

def debug_pv(msg):
    if PV_DEBUG:
        print(f"[PV DEBUG] {msg}", flush=True)                                                                                      
########## LOGGING ############                                                                           
SUBSCRIPTIONS_DEBUG = False

def debug_subscriptions(msg):
    if SUBSCRIPTIONS_DEBUG:
        print(f"[SUBSCRIPTIONS DEBUG] {msg}", flush=True)                                        
        
########## LOGGING ############ 
               
SET_BANNER_DEBUG = False

def set_banner_debug(msg):
    if SET_BANNER_DEBUG:
        print(f"[BANNER SET DEBUG] {msg}", flush=True)                                                                                                                                ########## LOGGING ############                                                                           
GET_LINKS_DEBUG = False

def get_links_debug(msg):
    if GET_LINKS_DEBUG:
        print(f"[GET LINKS DEBUG] {msg}", flush=True)                                                                                                                                 ########## LOGGING ############
        
FIX_DEBUG = True

def fix_debug(msg):
    if FIX_DEBUG:
        print(f"[FIX DEBUG] {msg}", flush=True)                                                                                         
########## LOGGING ############        

LOGGIN_DEBUG = True

def loggin_debug(msg):
    if LOGGIN_DEBUG:
        print(f"[LOGGIN DEBUG] {msg}", flush=True)
        admin_log(f"{msg}", "INFO")
        
########## LOGGING ############                                                                           
LOCK_DEBUG = True

def lock_debug(msg):
    if LOCK_DEBUG:
        print(f"[LOCK DEBUG] {msg}", flush=True)

                                                                           ########## LOGGING ############                                                             

SAFE_CONNECT_DEBUG = True

def safe_connect_debug(msg):
    if SAFE_CONNECT_DEBUG:
        print(f"[SAFE CONNECT DEBUG] {msg}", flush=True)                                                                                                                   ########## LOGGING ############                                                                           
TASK_WORKER_DEBUG = True

def task_worker_debug(msg):
    if TASK_WORKER_DEBUG:
        print(f"[TASK WORKER DEBUG] {msg}", flush=True)  
        
########## LOGGING ############                                                                           
LOAD_DATA_DEBUG = True

def load_data_debug(msg):
    if LOAD_DATA_DEBUG:
        print(f"[LOAD DATA DEBUG] {msg}", flush=True)                                                                                      
                                                                                                                            
                                                                                                                                                                                                                                                
########## LOGGING ############
########## LOGGING ############
########## LOGGING ############
########## LOGGING ############
########## LOGGING ############                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
# Global Timezone
tehran = pytz.timezone("Asia/Tehran")

def get_reply_id(update):
    if update.message:
        return update.message.message_id
    elif update.callback_query and update.callback_query.message:
        return update.callback_query.message.message_id
    return None




REPLIED_USERS_FILE = "replied_users.json"

try:
    with open(REPLIED_USERS_FILE, "r") as f:
        all_replied_users = json.load(f)
except:
    all_replied_users = {}
    

NORMAL_FILE = "normal_monshi_messages.json"

KNOWN_USERS_FILE = "known_users.json"

# Load cache on startup
if os.path.exists(KNOWN_USERS_FILE):
    with open(KNOWN_USERS_FILE, "r") as f:
        try:
            known_users = {
                int(k): User(**v) for k, v in json.load(f).items()
            }
        except Exception:
            known_users = {}
else:
    known_users = {}
def read_json(filename):
    """Read JSON data from a file, or create an empty file if not found."""
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=2)
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
        
#session_locks = {}

#def get_session_lock(session_path):
#    if session_path not in session_locks:
#        session_locks[session_path] = asyncio.Lock()
#    return session_locks[session_path]                                                                                                       
    
            
                    
                            
                                    
import asyncio
import inspect
session_wants_lock = {}
session_locks = {}

def get_session_lock(session_path):
    if session_path not in session_locks:
        session_locks[session_path] = asyncio.Lock()

    # Only log if the session path contains one of the specified phone numbers
    monitored_numbers = ["+989921334364", "+989104321206", "+989331790203"]
    if any(phone in session_path for phone in monitored_numbers):
        caller = inspect.stack()[1].function
        lock_debug(f"[LOCK DEBUG] Lock requested for {session_path} by {caller}()")

    return session_locks[session_path]                                

                                                    
                                                                                                        
                                                                                                                                                                                                                
                                                            
                                                                    
def get_next_api_credentials(new_user_id, phone):
    API_JSON_PATH = "api.json"

    if not os.path.exists(API_JSON_PATH):
        raise FileNotFoundError(f"{API_JSON_PATH} not found.")

    with open(API_JSON_PATH, "r", encoding="utf-8") as f:
        apis = json.load(f)

    # Sort by fewest accounts
    sorted_apis = sorted(apis.items(), key=lambda item: len(item[1]["accounts_logged_in"]))

    for key, api in sorted_apis:
        # If no accounts yet, or user_id not already in list
        if not api["accounts_logged_in"] or not any(acc["user_id"] == str(new_user_id) for acc in api["accounts_logged_in"]):
            # Add user + phone
            api["accounts_logged_in"].append({
                "user_id": str(new_user_id),
                "phone": phone
            })
            with open(API_JSON_PATH, "w", encoding="utf-8") as f:
                json.dump(apis, f, indent=2, ensure_ascii=False)
            return api["api_id"], api["api_hash"]

    # Fallback — use first anyway
    key, api = sorted_apis[0]
    api["accounts_logged_in"].append({
        "user_id": str(new_user_id),
        "phone": phone
    })
    with open(API_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(apis, f, indent=2, ensure_ascii=False)
    return api["api_id"], api["api_hash"]
                                                                                
                                                                                    
                                                                                            
                                                                                                            
def write_json(filename, data):
    """Write dictionary data to a JSON file with UTF-8 encoding."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        


AUTO_REPLY_FILE = "data/auto_reply_status.json"

def load_auto_reply_status():
    if not os.path.exists(AUTO_REPLY_FILE):
        return {}
    with open(AUTO_REPLY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
        
def is_auto_reply_enabled_for_account(user_id, phone):
    data = load_auto_reply_status()
    user_data = data.get(str(user_id), {})
    accounts = user_data.get("accounts", [])
    return user_data.get("auto_reply_enabled", False) and phone in accounts
    
def save_auto_reply_status(data):
    with open(AUTO_REPLY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def is_auto_reply_enabled(user_id):
    data = load_auto_reply_status()
    return data.get(str(user_id), {}).get("auto_reply_enabled", False)

def set_auto_reply_status(user_id, enabled: bool):
    data = load_auto_reply_status()

    # Get all accounts for the user
    accounts = get_tapchi_list(user_id)
    account_phones = [acc.get("phone", "unknown") for acc in accounts]

    data[str(user_id)] = {
        "auto_reply_enabled": enabled,
        "accounts": account_phones
    }

    save_auto_reply_status(data)


# ---------- Normal Monshi ----------
def get_normal_monshi(user_id):
    data = read_json(NORMAL_FILE)
    return data.get(str(user_id), [])

def add_normal_monshi(user_id, message):
    data = read_json(NORMAL_FILE)
    uid = str(user_id)
    if uid not in data:
        data[uid] = []
    if len(data[uid]) < 5:
        data[uid].append(message)
        write_json(NORMAL_FILE, data)
        return True
    return False

def delete_normal_monshi(user_id, index):
    data = read_json(NORMAL_FILE)
    uid = str(user_id)
    if uid in data and 0 <= index < len(data[uid]):
        data[uid].pop(index)
        write_json(NORMAL_FILE, data)
        return True
    return False

def clear_normal_monshi(user_id):
    data = read_json(NORMAL_FILE)
    uid = str(user_id)
    if uid in data:
        del data[uid]
        write_json(NORMAL_FILE, data)
        return True
    return False

# ---------- Advanced Monshi ----------
def get_advanced_monshi(user_id: int):
    filename = f"data/advanced_{user_id}.json"
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            debug_monshi(f"[READ FAIL] {filename}: {e}")
    return {}
def remove_active_session(user_id, phone):
    SESSIONS_JSON = "data/auto_reply_active_sessions.json"
    if not os.path.exists(SESSIONS_JSON):
        return
    with open(SESSIONS_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    uid = str(user_id)
    if uid in data:
        data[uid] = [acc for acc in data[uid] if acc["phone"] != phone]
        if not data[uid]:
            del data[uid]

        with open(SESSIONS_JSON, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
def add_advanced_monshi(user_id: int, trigger, reply):
    data = get_advanced_monshi(user_id)
    data[trigger] = reply
    save_advanced_monshi(user_id, data)
    return True

def delete_advanced_monshi(user_id: int, trigger):
    data = get_advanced_monshi(user_id)
    if trigger in data:
        del data[trigger]
        save_advanced_monshi(user_id, data)
        return True
    return False

def clear_advanced_monshi(user_id: int):
    filename = f"data/advanced_{user_id}.json"
    if os.path.exists(filename):
        os.remove(filename)
        return True
    return False
def save_advanced_monshi(user_id: int, data):
    filename = f"data/advanced_{user_id}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)    
    
    
def clear_user_flags(context):
    """Clear all user input flags to prevent stuck states"""
    for key in [
        # Edit flags
        "awaiting_edit_name", "awaiting_edit_bio", "new_names", "new_bio",
        # Photo flags
        "awaiting_multi_photos", "profile_photos", "awaiting_photo", "gm_edit_photo",
        # Banner flags
        "gm_set_banner", "gm_set_banner_forward", "gm_join_groups",
        "in_set_banner_mode", "banner_adding_for", "temp_banner",
        # Broadcast flags
        "awaiting_pv_broadcast", "pv_broadcast_messages",
        # Monshi flags
        "awaiting_advanced_trigger", "awaiting_advanced_reply", "advanced_trigger", "advanced_reply",
        # Ticket flags
        "awaiting_ticket_message", "awaiting_ticket_reply", "current_ticket_id"
    ]:
        context.user_data.pop(key, None)
    
    return True  # Return value to indicate success

# ==================== TICKET SYSTEM FUNCTIONS ====================

def load_tickets():
    """Load tickets from JSON file"""
    try:
        with open("data/tickets.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tickets(tickets):
    """Save tickets to JSON file"""
    try:
        os.makedirs("data", exist_ok=True)
        with open("data/tickets.json", "w", encoding="utf-8") as f:
            json.dump(tickets, f, ensure_ascii=False, indent=4)
    except Exception as e:
        logging.error(f"Error saving tickets: {e}")

def create_ticket(user_id, message, user_name=""):
    """Create a new ticket"""
    tickets = load_tickets()
    ticket_id = str(uuid.uuid4())[:8].upper()  # Short unique ID
    new_ticket = {
        "id": ticket_id,
        "user_id": user_id,
        "user_name": user_name,
        "message": message,
        "replies": [],
        "status": "open",
        "timestamp": datetime.now().isoformat(),
        "last_activity": datetime.now().isoformat()
    }
    tickets.append(new_ticket)
    save_tickets(tickets)
    return ticket_id

def add_reply_to_ticket(ticket_id, reply, is_admin=False, sender_name=""):
    """Add a reply to a ticket"""
    tickets = load_tickets()
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["replies"].append({
                "text": reply,
                "is_admin": is_admin,
                "sender_name": sender_name,
                "timestamp": datetime.now().isoformat()
            })
            ticket["last_activity"] = datetime.now().isoformat()
            save_tickets(tickets)
            return True
    return False

def close_ticket(ticket_id):
    """Close a ticket"""
    tickets = load_tickets()
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = "closed"
            ticket["last_activity"] = datetime.now().isoformat()
            save_tickets(tickets)
            return True
    return False

def get_user_tickets(user_id):
    """Get all tickets for a user"""
    tickets = load_tickets()
    user_tickets = [t for t in tickets if t["user_id"] == user_id]
    return sorted(user_tickets, key=lambda x: x["last_activity"], reverse=True)

def get_open_tickets():
    """Get all open tickets"""
    tickets = load_tickets()
    open_tickets = [t for t in tickets if t["status"] == "open"]
    return sorted(open_tickets, key=lambda x: x["last_activity"], reverse=True)

def get_ticket_by_id(ticket_id):
    """Get a specific ticket by ID"""
    tickets = load_tickets()
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket
    return None

DATABASE_URL = "postgresql://botuser:StrongPassword123@localhost:5432/botdb"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def remove_session_files(user_id: int, phone: str):
    session_path = os.path.join("data/sessions", f"session_{user_id}_{phone}.session")
    for suffix in ["", ".journal", ".db-shm", ".db-wal"]:
        path = session_path + suffix
        if os.path.exists(path):
            try:
                os.remove(path)
            except Exception as e:
                logging.error(f"Error removing session file {path}: {e}")

def require_active_subscription(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        user_id = query.from_user.id
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return
        return await func(update, context)
    return wrapper
    
# CONFIG & VERSION
BOT_VERSION = "1.0.1"

def check_version():
    version_file = os.path.join(DATA_DIR, "version.json")  # Ensure it's stored inside /data

    version_info = {"version": BOT_VERSION}

    if os.path.exists(version_file):
        try:
            with open(version_file, "r", encoding="utf-8") as f:
                current = json.load(f)

            if current.get("version") != BOT_VERSION:
                with open(version_file, "w", encoding="utf-8") as fw:
                    json.dump(version_info, fw, ensure_ascii=False, indent=4)

        except Exception as e:
            logging.error(f"Error reading version.json: {e}")
    else:
        with open(version_file, "w", encoding="utf-8") as fw:
            json.dump(version_info, fw, ensure_ascii=False, indent=4)
            
def has_used_trial_before(user_id):
    trials = load_trials()
    return str(user_id) in trials            

# BASE PATH & DIRS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

SESSION_DIR = os.path.join(DATA_DIR, "sessions")

BALANCES_FILE = os.path.join(DATA_DIR, "balances_tapchi.json")

ACCOUNTS_FILE = os.path.join(DATA_DIR, "tapchi_accounts.json")

SUBSCRIPTIONS_FILE = os.path.join(DATA_DIR, "subscriptions.json")

TRIAL_FILE = os.path.join(BASE_DIR, "tapchi_trials.json")  # User trials file

# Ensure required directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(SESSION_DIR, exist_ok=True)

def load_trials():
    if not os.path.exists(TRIAL_FILE):
        return {}
    with open(TRIAL_FILE, "r") as f:
        return json.load(f)
# --- Get all tapchi accounts for the current user ---
def get_user_sessions(user_id: int):
    db = SessionLocal()
    try:
        row = db.query(TapchiAccount).filter_by(user_id=str(user_id)).first()
        if row:
            return row.account_data
        return []
    except Exception as e:
        logging.error(f"Failed to fetch user sessions for {user_id}: {e}")
        return []
    finally:
        db.close()


# Track running jobs
active_job_tasks = {}

import asyncio

async def task_worker():
    while True:
        task_func = await task_queue.get()
        task_worker_debug(f"Task received: {getattr(task_func, '__name__', str(task_func))}")
        try:
            await asyncio.wait_for(task_func(), timeout=300)
            task_worker_debug(f"Task completed: {getattr(task_func, '__name__', str(task_func))}")
        except asyncio.TimeoutError:
            task_worker_debug("Task timed out after 60 seconds and was cancelled.")
        except Exception as e:
            task_worker_debug(f"ERROR while executing task: {e}")
        finally:
            task_queue.task_done()
            task_worker_debug(f"task_done called. Queue size: {task_queue.qsize()}")

async def monitor_task_queue():
    while True:
        qsize = task_queue.qsize()
        if qsize > 0:
            task_worker_debug(f"Queue backlog detected: {qsize} tasks waiting")
        else:
            task_worker_debug("Queue is currently empty")
        await asyncio.sleep(10)           
            
pending_sessions = set()

async def schedule_send_banner(phone_info, user_id, context):
    phone = phone_info.get("phone", "UNKNOWN")
    session_id = f"{user_id}_{phone}"
    
    if session_id in pending_sessions:
        debug_banner(f"[SKIP] Banner already scheduled for {phone}")
        return

    pending_sessions.add(session_id)

    async def banner_task():
        debug_banner("#####\n#####\n#####\n#####\n#####")
        debug_banner(f"[BANNER TASK START] {phone}")
        try:
            await send_banner_for_account(phone_info, user_id, context)
        finally:
            pending_sessions.discard(session_id)
            debug_banner(f"[BANNER TASK END] {phone}")
            debug_banner("#####\n#####\n#####\n#####\n#####")

    await task_queue.put(banner_task)
    
async def schedule_clock_updater(acc, user_id):
    async def clock_task():
        await clock_updater(acc, user_id)
    await task_queue.put(clock_task)   
    
      
async def process_job_queue(user_id, phone):
    key = f"{user_id}_{phone}"
    job_data = load_job_list()
    jobs = job_data.get(key, [])

    updated_jobs = []
    for job in jobs:
        if job.get("status") != "pending":
            continue

        job_type = job["type"]
        payload = job.get("payload", {})

        try:
            if job_type == "send_banner":
                await run_send_banner(user_id, phone, payload)
            elif job_type == "change_name":
                await run_change_name(user_id, phone, payload)
            elif job_type == "auto_reply":
                await start_auto_reply_for_user(phone, user_id)
            elif job_type == "join_groups":
                await process_group_joining(user_id, phone, payload)

            # Don't add back successful jobs
        except Exception as e:
            logging.error(f"[JOB ERROR] {job_type} for {phone}: {e}")
            # Optional: Retry logic or logging
        await asyncio.sleep(5)

    # Save updated (unfinished) job list
    job_data[key] = updated_jobs
    save_job_list(job_data)


async def start_processing_queues():
    while True:
        job_data = load_job_list()
        for key in job_data:
            if any(job["status"] == "pending" for job in job_data[key]):
                if key not in active_job_tasks:
                    user_id, phone = key.split("_", 1)
                    task = asyncio.create_task(process_job_queue(int(user_id), phone))
                    active_job_tasks[key] = task
        await asyncio.sleep(10)
#126                            
from telethon.errors import SecurityError

async def connect_to_session(user_id: int, phone: str) -> TelegramClient:
    session_path = os.path.join("data/sessions", f"session_{user_id}_{phone}.session")

    for attempt in range(3):
        client = TelegramClient(session_path, API_ID, API_HASH)
        try:
            await client.connect()
            if await client.is_user_authorized():
                await client.get_me()
                return client
            else:
                raise Exception("Client not authorized")

        except SecurityError as se:
            logging.warning(f"[SECURITY ERROR] Invalid session for {phone}. Deleting session: {se}")
            # Delete corrupted session files
            for suffix in ["", ".journal", ".db-shm", ".db-wal"]:
                try:
                    os.remove(session_path + suffix)
                except FileNotFoundError:
                    continue
                except Exception as e:
                    logging.error(f"[SESSION DELETE ERROR] {session_path + suffix}: {e}")
            # Wait a bit before retry
            await asyncio.sleep(1)
            continue  # Retry with a fresh session

        except Exception as e:
            logging.error(f"[CONNECT ERROR] Attempt {attempt+1} failed for {phone}: {e}")
            await asyncio.sleep(1)

    raise Exception(f"{phone}: Failed to connect or authorize after retries.")

#async def connect_to_session(user_id: int, phone: str) -> TelegramClient:
#    session_path = os.path.join("data/sessions", f"session_{user_id}_{phone}.session")
#    client = TelegramClient(session_path, API_ID, API_HASH)

#    for attempt in range(3):
#        try:
#@@@            
#            await client.connect()            
#            if await client.is_user_authorized():
#                await client.get_me()
#                return client
#            else:
#                raise Exception("Client not authorized")
#        except Exception as e:
#            await asyncio.sleep(1)

#    raise Exception(f"{phone}: Failed to connect or authorize after retries.")
        
    
                        
def save_trials(trials):
    with open(TRIAL_FILE, "w") as f:
        json.dump(trials, f, indent=4)
def is_trial_active(user_id):
    trials = load_trials()
    trial = trials.get(str(user_id))
    if not trial:
        return False
#x
    tehran = pytz.timezone("Asia/Tehran")
    now = datetime.now(tehran)

    expiry = datetime.fromisoformat(trial["expiry"])
    if expiry.tzinfo is None:
        expiry = tehran.localize(expiry)
    else:
        expiry = expiry.astimezone(tehran)

    return now < expiry
            
# BOT & API Credentials
BOT_TOKEN = "8874940402:AAFXnMVQT5xrpMSpQ4TcZ6K5quiGvIW3hOE"
ADMIN_ID = 8650091524
API_ID = 24775679
API_HASH = "6c534bd84521d6325816520af1d48a23"
WAIT_PHONE = 100
# This is the expected spambot response text.
EXPECTED_SPAMBOT_RESPONSE = "Good news, no limits are currently applied to your account. You’re free as a bird!"
#125
async def check_spambot_for_account(client: TelegramClient, user_id: int, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """
    Sends /start to spambot three times and verifies that all responses are acceptable (either no limits or limited temporarily).
    """
    responses = []
    spambot_username = "spambot"
    for _ in range(3):
        try:
            await client.send_message(spambot_username, "/start")
            await asyncio.sleep(2)
            msgs = await client.get_messages(spambot_username, limit=1)
            if msgs and msgs[0].message:
                resp = msgs[0].message.strip()
                print("SPAMBOT REPLY:", resp)
                responses.append(resp)
        except Exception as e:
            responses.append("")

    EXPECTED_SPAMBOT_RESPONSE = "Good news, no limits are currently applied to your account. You’re free as a bird!"
    LIMITED_BUT_JOINABLE_TEXTS = [
        "your account is now limited until",     # English
        "اکانت شما",                             # Persian
        "محدود شده"                              # Persian
    ]
#def
    def is_acceptable_response(resp):
        if EXPECTED_SPAMBOT_RESPONSE in resp:
            return True
        return False

    return all(is_acceptable_response(resp) for resp in responses) and len(responses) == 3
#w


def get_all_known_user_ids():
    return [int(uid) for uid in user_subscriptions.keys()]

# --- Phone validation (Iran +98 only) ---
def normalize_iran_phone(phone_raw):
    if not phone_raw:
        return None
    # Remove all spaces, dashes, and other special characters
    phone = str(phone_raw).strip().replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    
    # Handle different formats of Iranian numbers
    if phone.startswith("09"):
        phone = "+98" + phone[1:]
    elif phone.startswith("9"):
        phone = "+98" + phone
    elif phone.startswith("989"):
        phone = "+" + phone
    elif phone.startswith("0098"):
        phone = "+" + phone[2:]
    
    # Strictly validate Iranian mobile numbers in format +989XXXXXXXXX
    if phone.startswith("+98") and re.fullmatch(r"\+989\d{9}", phone):
        return phone
    return None

WAITING_FOR_BROADCAST_TEXT = 1

async def send_msg_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != ADMIN_ID:
        await update.message.reply_text("⛔️ فقط ادمین می‌تواند پیام ارسال کند.")
        return ConversationHandler.END
    context.user_data["conversation_state"] = "WAITING_FOR_BROADCAST_TEXT"
    await update.message.reply_text("لطفاً پیام مورد نظر را وارد کنید:")
    return ConversationHandler.END  # We don’t use ConversationHandler states anymore

async def send_msg_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    count = 0
    all_users = get_all_known_user_ids()  # <- Make sure this is defined
    for uid in all_users:
        try:
            await context.bot.send_message(chat_id=uid, text=text)
            count += 1
        except:
            continue
    await update.message.reply_text(f"✅ پیام به {count} نفر ارسال شد.")
    return ConversationHandler.END

send_msg_conv = ConversationHandler(
    entry_points=[CommandHandler("send_msg", send_msg_entry)],
    states={WAITING_FOR_BROADCAST_TEXT: [MessageHandler(filters.TEXT & ~filters.COMMAND, send_msg_broadcast)]},
    fallbacks=[]
)


async def cut_plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("Access Denied: You are not authorized to use this command.")
        return
    try:
        user_id, days = int(context.args[0]), int(context.args[1])
        result = modify_subscription(str(user_id), days, "cut")

        if isinstance(result, dict):
            expiry_str = result["expiry"]
            tehran = pytz.timezone("Asia/Tehran")
            expiry_dt = datetime.fromisoformat(expiry_str).astimezone(tehran)
            now = datetime.now(tehran)
            remaining_days = (expiry_dt - now).days
            readable = f"{remaining_days} روز" if remaining_days >= 0 else "منقضی شده"

            await update.message.reply_text(
                f"🤖 یوزر: {user_id}\n"
                f"⏳️ روز های حذف شده: {days}\n"
                f"📆 تاریخ انقضای اشتراک: {expiry_dt.strftime('%Y-%m-%d %H:%M')} = {readable}"
            )
        else:
            await update.message.reply_text(result)

    except Exception as e:
        await update.message.reply_text(f"❌ Usage: /cut_plan <user_id> <days>\nخطا: {e}")


async def add_plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("Access Denied: You are not authorized to use this command.")
        return
    try:
        user_id, days = int(context.args[0]), int(context.args[1])
        result = modify_subscription(str(user_id), days, "add")

        if isinstance(result, dict):
            expiry_str = result["expiry"]
            tehran = pytz.timezone("Asia/Tehran")
            expiry_dt = datetime.fromisoformat(expiry_str).astimezone(tehran)
            now = datetime.now(tehran)
            remaining_days = (expiry_dt - now).days
            readable = f"{remaining_days} روز" if remaining_days >= 0 else "منقضی شده"

            await update.message.reply_text(
                f"🤖 یوزر: {user_id}\n"
                f"⏳️ روز های اضاف شده: {days}\n"
                f"📆 تاریخ انقضای اشتراک: {expiry_dt.strftime('%Y-%m-%d %H:%M')} = {readable}"
            )
        else:
            await update.message.reply_text(result)

    except Exception as e:
        await update.message.reply_text(f"❌ Usage: /add_plan <user_id> <days>\nخطا: {e}")


async def see_plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("Access Denied: You are not authorized to use this command.")
        return
    try:
        user_id = int(context.args[0])
        result = modify_subscription(str(user_id), mode="see")

        if isinstance(result, dict):
            expiry_str = result["expiry"]
            tehran = pytz.timezone("Asia/Tehran")
            expiry_dt = datetime.fromisoformat(expiry_str).astimezone(tehran)
            now = datetime.now(tehran)
            remaining_days = (expiry_dt - now).days
            readable = f"{remaining_days} روز" if remaining_days >= 0 else "منقضی شده"

            await update.message.reply_text(
                f"🤖 یوزر: {user_id}\n"
                f"📆 تاریخ انقضای اشتراک: {expiry_dt.strftime('%Y-%m-%d %H:%M')} = {readable}"
            )
        else:
            await update.message.reply_text(result)

    except Exception as e:
        await update.message.reply_text(f"❌ Usage: /see_plan <user_id>\nخطا: {e}")

from datetime import datetime, timedelta
import pytz

tehran = pytz.timezone("Asia/Tehran")

def modify_subscription(user_id: str, change_days=0, mode="see"):
    subs = user_subscriptions.get(user_id, [])
    if isinstance(subs, dict):
        subs = [subs]

    now = datetime.now(tehran)
    subs = sorted(subs, key=lambda x: x.get("expiry", ""), reverse=True)

    for s in subs:
        expiry = datetime.fromisoformat(s["expiry"])
        if expiry.tzinfo is None:
            expiry = tehran.localize(expiry)
        if expiry > now:
            if mode == "see":
                return {"expiry": s["expiry"]}
            elif mode == "add":
                new_expiry = expiry + timedelta(days=change_days)
                s["expiry"] = new_expiry.isoformat()
                save_subscriptions()
                return {"expiry": s["expiry"]}
            elif mode == "cut":
                new_expiry = expiry - timedelta(days=change_days)
                s["expiry"] = new_expiry.isoformat()
                save_subscriptions()
                return {"expiry": s["expiry"]}

    if mode == "add":
        new_expiry = now + timedelta(days=change_days)
        new_sub = {"allowed_accounts": 1, "expiry": new_expiry.isoformat(), "price": 0}
        subs.append(new_sub)
        user_subscriptions[user_id] = subs
        save_subscriptions()
        return {"expiry": new_expiry.isoformat()}

    return f"❌ No active subscription for user {user_id}"
    

def is_subscription_valid(user_id: int) -> bool:
    tehran = pytz.timezone("Asia/Tehran")
    subs = user_subscriptions.get(str(user_id), [])

    if isinstance(subs, dict):
        subs = [subs]
    elif not isinstance(subs, list):
        logging.error(f"Invalid subscription format for user {user_id}: {subs}")
        return False

    now = datetime.now(tehran)
    valid_found = False
    cleaned_subs = []

    for s in subs:
        if not isinstance(s, dict):
            continue
        expiry_str = s.get("expiry")
        if not expiry_str:
            continue
        try:
            expiry = datetime.fromisoformat(expiry_str)
            if expiry.tzinfo is None:
                expiry = tehran.localize(expiry)
            else:
                expiry = expiry.astimezone(tehran)

            if now < expiry:
                cleaned_subs.append(s)
                valid_found = True
        except Exception as e:
            logging.error(f"Invalid expiry format for user {user_id}: {expiry_str} ({e})")

    # Optionally update to remove expired subs
    user_subscriptions[str(user_id)] = cleaned_subs
    save_subscriptions()

    return valid_found
#124    
async def update_groups_from_telethon(user_id: int, phone_info: dict):
    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone_info['phone']}")
    client = None
    lock = get_session_lock(session_path)
    
    # Important: Debug logging to track execution
    debug_groups(f"Starting update_groups_from_telethon for {phone_info['phone']}")
    
    async with lock:
        try:
            # Create a NEW client - don't reuse the one from the calling function
            client = TelegramClient(session_path, API_ID, API_HASH)
            await client.connect()
            
            client.session.auto_save = False
            
            debug_groups(f"Connected client for {phone_info['phone']}")
            
            if not await client.is_user_authorized():
                
                debug_groups(f"Account {phone_info['phone']} is not authorized. Returning existing groups.")
                return phone_info.get("groups", [])
                await client.get_me()
                
            client.session._conn.execute("PRAGMA busy_timeout = 200000")
            debug_groups(f"Set busy timeout for {phone_info['phone']}")
        except Exception as e:
            debug_groups(f"Error connecting client for phone {phone_info['phone']}: {e}")
            return phone_info.get("groups", [])

        groups = []
        try:
            debug_groups(f"Fetching dialogs for {phone_info['phone']}")
            dialogs = await client.get_dialogs()
            debug_groups(f"Got {len(dialogs)} dialogs for {phone_info['phone']}")
            
            for dialog in dialogs:
                if dialog.is_group:
                    group = {
                        "id": dialog.id,
                        "link": f"https://t.me/{dialog.entity.username}" if dialog.entity.username else "",
                        "username": dialog.entity.username if dialog.entity.username else ""
                    }
                    groups.append(group)
            
            debug_groups(f"Processed {len(groups)} groups for {phone_info['phone']}")
        except Exception as e:
            debug_groups(f"Error fetching dialogs for phone {phone_info['phone']}: {e}")
        finally:
            if client:
                try:
                    debug_groups(f"Disconnecting client for {phone_info['phone']}")
                    await client.disconnect()
                    debug_groups(f"Successfully disconnected client for {phone_info['phone']}")
                except Exception as e:
                    debug_groups(f"Error disconnecting client for {phone_info['phone']}: {e}")

    # Update the phone_info with the new groups
    phone_info["groups"] = groups
    debug_groups(f"Updated phone_info with {len(groups)} groups for {phone_info['phone']}")

    try:
        # Update the account list and save
        debug_groups(f"Saving updated account information for {phone_info['phone']}")
        accounts = get_tapchi_list(user_id)
        for i, acc in enumerate(accounts):
            if acc.get("phone") == phone_info["phone"]:
                accounts[i] = phone_info
                break

        save_accounts(user_id, accounts)
        debug_groups(f"Successfully saved account information for {phone_info['phone']}")
    except Exception as e:
        debug_groups(f"Error saving account information for {phone_info['phone']}: {e}")

    return groups

def upgrade_accounts():
    global tapchi_accounts
    changed_users = []

    for user_id, accounts in tapchi_accounts.items():
        changed = False
        for acc in accounts:
            if "forward" not in acc:
                acc["forward"] = {"status": "off", "interval": None, "next_send": None, "banner": None}
                changed = True
        if changed:
            changed_users.append((user_id, accounts))

    for user_id, accounts in changed_users:
        save_accounts(user_id, accounts)
    
def load_data():
    global user_balances, tapchi_accounts
    if os.path.exists(BALANCES_FILE):
        with open(BALANCES_FILE, "r", encoding="utf-8") as f:
            user_balances = json.load(f)
    else:
        user_balances = {}
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
            tapchi_accounts = json.load(f)
    else:
        tapchi_accounts = {}
    upgrade_accounts()  # Ensure all accounts have the new "forward" key.                
def save_balances():
    with open(BALANCES_FILE, "w", encoding="utf-8") as f:
        json.dump(user_balances, f, ensure_ascii=False, indent=4)
    

def save_accounts(user_id: int, accounts: list):
    with accounts_lock:
        try:
            if os.path.exists(ACCOUNTS_FILE):
                with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
                    all_data = json.load(f)
            else:
                all_data = {}
            all_data[str(user_id)] = accounts
            with open(ACCOUNTS_FILE, "w", encoding="utf-8") as f:
                json.dump(all_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            logging.error(f"[SAVE ACCOUNTS] Failed to save for user {user_id}: {e}")


        

def load_subscriptions():
    global user_subscriptions
    if os.path.exists(SUBSCRIPTIONS_FILE):
        with open(SUBSCRIPTIONS_FILE, "r", encoding="utf-8") as f:
            user_subscriptions = json.load(f)
        logging.info("Subscriptions loaded: " + str(user_subscriptions))
    else:
        user_subscriptions = {}
        with open(SUBSCRIPTIONS_FILE, "w", encoding="utf-8") as f:
            json.dump(user_subscriptions, f, ensure_ascii=False, indent=4)
        logging.info("subscriptions.json created as it did not exist.")

def save_subscriptions():
    with open(SUBSCRIPTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(user_subscriptions, f, ensure_ascii=False, indent=4)

def get_balance(user_id: int) -> int:
    return user_balances.get(str(user_id), 0)

def add_balance(user_id: int, amount: int):
    cur = get_balance(user_id)
    user_balances[str(user_id)] = cur + amount
    save_balances()

def cut_balance(user_id: int, amount: int):
    cur = get_balance(user_id)
    new_val = cur - amount
    if new_val < 0:
        new_val = 0
    user_balances[str(user_id)] = new_val
    save_balances()
# This is the new /cut command handler.
# This is the new /cut command handler.
async def cut_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Only allow the admin to use this command.
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("Access Denied: You are not authorized to use this command.")
        return

    # Check if the command has two arguments: target user_id and amount.
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /cut <user_id> <amount>")
        return

    try:
        # Parse arguments
        target_id = int(context.args[0])
        amount = int(context.args[1])
        print("DEBUG: Parsed amount =", amount)
    except Exception:
        await update.message.reply_text("فرمت دستور نادرست است. مثلاً: /cut 1791861136 100000000")
        return

    # Deduct the specified amount from the target user's balance.
    cut_balance(target_id, amount)
    new_balance = get_balance(target_id)
    await update.message.reply_text(f"New balance for {target_id}: {new_balance:,}")
#123        
async def forced_join_group(client: TelegramClient, group: dict, account_phone: str, chat_id: int, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """
    Attempts to force join a given group.
    Returns True if the join is successful, otherwise False.
    Suppresses errors for unwanted cases.
    For 'too many channels' errors, sends a custom message.
    """
    username = extract_group_username(group["link"])
    if not username:
        return False
    try:
        await client(JoinChannelRequest(username))
        return True
    except Exception as e:
        error_str = str(e).lower()
        # Do not report if the error indicates that the group is invalid:
        unwanted_errors = ["cannot find any entity", "keyboardbuttoncallback"]
        if any(sub in error_str for sub in unwanted_errors):
            return False
        # If the error indicates that the account can't write (i.e. group is already blacklist) then skip forced join.
        if "you can't write in this chat" in error_str:
            return False
        # For "too many channels" error, send custom message.
        if "too many channels" in error_str:
            await context.bot.send_message(chat_id, f"عدم موفقیت در عضویت اجباری برای گروه\nاکانت: {account_phone}\nعلت:عضو کانال/گروه های زیادی شدید")
            return False
        # For any other error, simply return False (or log if you wish)
        return False
#122        
async def process_forced_join_for_unsuccessful_groups(
    phone_info: dict,
    user_id: int,
    context,
    unsuccessful_groups: list
) -> (int, int):
    account_phone = phone_info.get('phone', '')
    if not account_phone:
        return 0, 0

    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{account_phone}")
    lock = get_session_lock(session_path)
#@@@
    async with lock:
        client = TelegramClient(session_path, API_ID, API_HASH)
        # 2. Connect and check authorization
        try:
            await client.connect()

            if not await client.is_user_authorized():
                await client.disconnect()
                return 0, len(unsuccessful_groups)

            # Authorized — safe to retrieve user info
            await client.get_me()

            forced_success = 0
            forced_failure = 0
            chat_id = user_id
            blacklist = phone_info.get("blacklist", [])
            groups_to_process = [g for g in unsuccessful_groups if g not in blacklist]

            for group in groups_to_process:
                await asyncio.sleep(60)
                result = await send_and_check_group(session_path, client, group, user_id, chat_id, context, wait_time=3)

                if result == "forced_join_needed":
                    username = extract_group_username(group["link"])
                    if username:
                        try:
                            await client(JoinChannelRequest(username))
                            forced_success += 1
                        except Exception:
                            phone_info.setdefault("blacklist", []).append(group)
                            forced_failure += 1
                    else:
                        forced_failure += 1

                elif result == "error":
                    phone_info.setdefault("blacklist", []).append(group)
                    forced_failure += 1
                else:
                    forced_failure += 1

            await client.disconnect()
            return forced_success, forced_failure

        except Exception:
            return 0, len(unsuccessful_groups)     

tapchi_accounts = {}    
tapchi_accounts_cache = {}

def get_tapchi_list(user_id: int):
    uid = str(user_id)
    if uid not in tapchi_accounts:
        tapchi_accounts[uid] = []
    return tapchi_accounts[uid]

#def get_tapchi_list(user_id: int):
#    uid = str(user_id)
#    return tapchi_accounts.get(uid, [])
    
def init_phone_info(phone_dict):
    if "groups" not in phone_dict:
        phone_dict["groups"] = []
    if "normal" not in phone_dict:
        phone_dict["normal"] = {"status": "off", "interval": None, "next_send": None, "banners": []}
    # New forward message configuration – note that only one banner is allowed.
    if "forward" not in phone_dict:
        phone_dict["forward"] = {"status": "off", "interval": None, "next_send": None, "banner": None}
    if "blacklist" not in phone_dict:
        phone_dict["blacklist"] = []
        

def extract_group_username(link: str) -> str:
    link = link.strip()
    if link.startswith("@"):
        return link[1:]
    if link.startswith("https://"):
        link = link[len("https://"):]
    elif link.startswith("http://"):
        link = link[len("http://"):]
    if link.startswith("t.me/"):
        link = link[len("t.me/"):]
    # Split the link at "/" and return only the first part (the username)
    return link.split("/")[0]
def extract_message_id(link: str) -> int:
    # Split the link and try to convert the last part into an integer.
    parts = link.strip().split("/")
    if len(parts) > 1 and parts[-1].isdigit():
        return int(parts[-1])
    return None
    
async def update_bio_for_accounts(user_id, new_bio, context):
    accounts = get_tapchi_list(user_id)
    for acc in accounts:
        acc['bio'] = new_bio
        logging.debug(f"Updated account {acc.get('phone', 'unknown')} bio to: {new_bio}")
    save_accounts(user_id, phone_list)
    
async def forward_banner_message(client, target_group, banner_link: str, user_id: int, context: ContextTypes.DEFAULT_TYPE):
    if not is_subscription_valid(user_id):
        await context.bot.send_message(chat_id=user_id, text="⛔️ شما اشتراکی ندارید")
        return

    username = extract_group_username(banner_link)
    message_id = extract_message_id(banner_link)

    # Continue with the rest of your forwarding logic...
    
    if not username or message_id is None:
        logging.error("Banner link parsing failed.")
        return "invalid_banner_link"

    try:
        # Get the source entity from which the banner will be forwarded
        source_entity = await client.get_entity(username)
        # Get the target group entity using the group's stored link
        target_username = extract_group_username(target_group["link"])
        target_entity = await client.get_entity(target_username)
        
# Forward the message from the source entity to the target entity
        if not is_subscription_valid(user_id):
            await context.bot.send_message(chat_id=user_id, text="⛔️ شما اشتراکی ندارید")
            return "error"

        await client.forward_messages(target_entity, [message_id], source_entity)
        return "success"
    except Exception as e:
        logging.error(f"Error forwarding to {target_group['link']}: {e}")
        return "error"
    

async def update_name_for_accounts(user_id, new_names, context):
    accounts = get_tapchi_list(user_id)
    for i, name in enumerate(new_names):
        if i < len(accounts):
            accounts[i]['name'] = name
            logging.debug(f"Updated account {accounts[i].get('phone', 'unknown')} name to: {name}")
    save_accounts(user_id, phone_list)

async def safe_connect(client: TelegramClient, phone_info: dict, chat_id=None, context=None) -> bool:
    import logging

    user_id = context.user_data.get('user_id') if context and context.user_data else "unknown"
    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone_info['phone']}")

    lock = get_session_lock(session_path)
    retries = 5

    async with lock:
        for attempt in range(retries):
            try:
                logging.debug(f"Attempt {attempt + 1}/{retries} to connect {phone_info['phone']}")
                await client.connect()

                if not await client.is_user_authorized():
                    await client.disconnect()
                    continue

                await client.get_me()
                client.session.auto_save = False
                return True

            except Exception as e:
                error_str = str(e).lower()

                if "database is locked" in error_str:
                    logging.warning(f"Database locked for {phone_info['phone']}. Retrying...")
                    await asyncio.sleep(5)
                    continue

                elif "0 bytes read" in error_str or "security error" in error_str:
                    logging.warning(f"Session corruption suspected for {phone_info['phone']}. Cleaning session files.")
                    for suffix in ["", ".journal", ".db-shm", ".db-wal"]:
                        try:
                            os.remove(session_path + suffix)
                        except FileNotFoundError:
                            continue
                        except Exception as delete_error:
                            logging.error(f"[SESSION DELETE ERROR] {session_path + suffix}: {delete_error}")
                    await client.disconnect()
                    await asyncio.sleep(2)
                    continue

                else:
                    logging.error(f"[CONNECT ERROR] {phone_info['phone']}: {e}")
                    if context and chat_id:
                        await context.bot.send_message(chat_id, f"{phone_info['phone']}: Connection error: {e}")
                    return False

        if context and chat_id:
            await context.bot.send_message(chat_id, f"{phone_info['phone']}: Failed to connect after {retries} retries.")
        return False    
            
    
#121
#async def safe_connect(client: TelegramClient, phone_info: dict, chat_id=None, context=None) -> bool:
#    # Fallback user_id for logging or locking
#    user_id = context.user_data.get('user_id') if context and context.user_data else "unknown"
#    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone_info['phone']}")

#    lock = get_session_lock(session_path)
#    retries = 5
#3
#    async with lock:
#        for attempt in range(retries):
#            try:
#                await client.connect()

#                if not await client.is_user_authorized():
#                    await client.disconnect()
#                    continue

#                await client.get_me()
#                client.session.auto_save = False
#                return True
#            except Exception as e:
#                if "database is locked" in str(e).lower():
#                    await asyncio.sleep(5)
#                else:
#                    if context and chat_id:
#                        await context.bot.send_message(chat_id, f"{phone_info['phone']}: Connection error: {e}")
#                    return False

#        if context and chat_id:
#            await context.bot.send_message(chat_id, f"{phone_info['phone']}: Connection error: database is locked after retries")
#        return False

#async def safe_connect(client: TelegramClient, phone_info: dict, user_id: int, chat_id=None, context=None) -> bool:
#    if not user_id:
#        logging.warning(f"[SAFE_CONNECT] Missing user_id for phone {phone_info.get('phone')}")
#        user_id = "unknown"
        
#async def safe_connect(client: TelegramClient, phone_info: dict, chat_id=None, context=None) -> bool:
#    # Resolve user_id from context or phone_info
#    user_id = (
#        context.user_data.get("user_id")
#        if context and context.user_data and "user_id" in context.user_data
#        else phone_info.get("user_id")
#    )

#    if not user_id:
#        safe_connect_debug(f"[SAFE_CONNECT] Missing user_id for phone {phone_info.get('phone')}")
#        user_id = "unknown"



#async def safe_connect(client: TelegramClient, phone_info: dict, user_id: int, chat_id=None, context=None) -> bool:
#    if not isinstance(user_id, int):
#        logging.error(f"[SAFE_CONNECT] Invalid user_id for phone {phone_info.get('phone')}: {user_id}")
#        return False

#    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone_info['phone']}")
#    lock = get_session_lock(session_path)
#    retries = 5

#    async with lock:
#        for attempt in range(retries):
#            try:
#                await client.connect()
#                client.session._conn.execute("PRAGMA busy_timeout = 200000")

#                if not await client.is_user_authorized():
#                    await client.disconnect()
#                    continue

#                await client.get_me()
#                client.session.auto_save = False
#                return True

#            except Exception as e:
#                if "database is locked" in str(e).lower():
#                    await asyncio.sleep(5)
#                else:
#                    if context and chat_id:
#                        await context.bot.send_message(chat_id, f"{phone_info['phone']}: Connection error: {e}")
#                    return False

#            finally:
#                # Ensure we always disconnect the client if not authorized
#                if client.is_connected() and not await client.is_user_authorized():
#                    await client.disconnect()

#        if context and chat_id:
#            await context.bot.send_message(chat_id, f"{phone_info['phone']}: Connection error: database is locked after retries")
#        return False

async def check_account_status(phone_info: dict, user_id: int) -> str:
    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone_info['phone']}")
    client = TelegramClient(session_path, API_ID, API_HASH)
    lock = get_session_lock(session_path)
#4
    async with lock:
        try:
            await client.connect()

            if not await client.is_user_authorized():
                await client.disconnect()
                return f"اکانت {phone_info['phone']} غیرمجاز است."

            await client.get_me()
            client.session.auto_save = False
            client.session._conn.execute("PRAGMA busy_timeout = 200000")
            await client.get_me()
            await client.disconnect()
            return f"اکانت {phone_info['phone']} سالم است."
        except Exception as e:
            error_text = str(e).lower()
            if "banned" in error_text:
                return f"اکانت {phone_info['phone']} بن شده است."
            elif "limited" in error_text or "restricted" in error_text:
                return f"اکانت {phone_info['phone']} محدود است."
            else:
                return f"اکانت {phone_info['phone']} خطا: {e}"
                

async def check_account_status_spambot(phone_info: dict, user_id: int) -> str:
    phone = phone_info.get("phone")
    if not phone:
        return "اکانت بدون شماره یافت شد."

    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
    lock = get_session_lock(session_path)
#5
    async with lock:
        client = TelegramClient(session_path, API_ID, API_HASH)

        try:
            await client.connect()

            if not await client.is_user_authorized():
                await client.disconnect()
                return f"اکانت: {phone}\nوضعیت: غیرمجاز است."

            await client.get_me()

            spambot_username = "spambot"
            await client.send_message(spambot_username, "/start")
            await asyncio.sleep(2)
            msgs = await client.get_messages(spambot_username, limit=1)
            reply_text = msgs[0].message if msgs else ""

            if "free as a bird" in reply_text:
                status = "سالم است"
            elif "submit a complaint" in reply_text or "برای همیشه" in reply_text:
                status = "برای همیشه لیمیت شده است"
            else:
                import re
                m = re.search(r'برای\s*(\d+)\s*روز', reply_text)
                if m:
                    days = m.group(1)
                    status = f"برای {days} روز لیمیت شده است"
                else:
                    status = "اکانت لیمیت شده است!"
            return f"اکانت: {phone}\nوضعیت: {status}"

        except Exception as e:
            return f"اکانت: {phone}\nوضعیت: خطا: {e}"

        finally:
            try:
                await client.disconnect()
            except Exception:
                pass

async def check_all_status_and_update(msg, user_id, context: ContextTypes.DEFAULT_TYPE):
    phone_list = get_tapchi_list(user_id)
    statuses = []
    for phone_info in phone_list:
        stat = await check_account_status_spambot(phone_info, user_id)
        statuses.append(stat)
    full_status = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~\n".join(statuses)
    await msg.edit_text(full_status)
                
async def check_individual_status_and_update(msg, user_id, idx, context: ContextTypes.DEFAULT_TYPE):
    phone_list = get_tapchi_list(user_id)
    if idx < 0 or idx >= len(phone_list):
        await msg.edit_text("ایندکس نامشخص یا خارج از محدوده")
        return
    phone_info = phone_list[idx]
    status = await check_account_status_spambot(phone_info, user_id)
    await msg.edit_text(status)                                     
async def general_account_status_handler(query: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = query.from_user.id
    phone_list = get_tapchi_list(user_id)
    status_lines = []
    for idx, ph_info in enumerate(phone_list, start=1):
        st = await check_account_status(ph_info, user_id)
        if "سالم" in st:
            status_text = "سالم است."
        elif "غیرمجاز" in st:
            status_text = "غیرمجاز است."
        elif "بن شده" in st:
            status_text = "بن شده است."
        elif "محدود" in st:
            status_text = "محدود است."
        else:
            status_text = st
        status_lines.append(f"{idx}. {ph_info.get('name', ph_info['phone'])} ➡️ {ph_info['phone']}: {status_text}")
    text = "\n".join(status_lines) if status_lines else "هیچ اکانتی یافت نشد."
    await query.message.edit_text(text)

def build_code_keypad(current_code: str):
    row1 = [InlineKeyboardButton("1", callback_data="code_digit:1"),
            InlineKeyboardButton("2", callback_data="code_digit:2"),
            InlineKeyboardButton("3", callback_data="code_digit:3")]
    row2 = [InlineKeyboardButton("4", callback_data="code_digit:4"),
            InlineKeyboardButton("5", callback_data="code_digit:5"),
            InlineKeyboardButton("6", callback_data="code_digit:6")]
    row3 = [InlineKeyboardButton("7", callback_data="code_digit:7"),
            InlineKeyboardButton("8", callback_data="code_digit:8"),
            InlineKeyboardButton("9", callback_data="code_digit:9")]
    row4 = [InlineKeyboardButton("0", callback_data="code_digit:0"),
            InlineKeyboardButton("✅", callback_data="code_confirm"),
            InlineKeyboardButton("❌", callback_data="code_clear")]
    return InlineKeyboardMarkup([row1, row2, row3, row4])

async def update_code_keypad(query: Update, context: ContextTypes.DEFAULT_TYPE):
    code_so_far = context.user_data.get("code_digits", "")
    text = f"📲 کد دریافتی از تلگرام را وارد کنید:\n\ncode: {code_so_far}"
    keypad = build_code_keypad(code_so_far)
    try:
        await query.message.edit_text(text, reply_markup=keypad)
    except Exception as e:
        logging.error(f"Error updating code keypad: {e}")

import os
import asyncio
from telethon import TelegramClient

import os
import asyncio

async def confirm_code_entry(query: Update, context: ContextTypes.DEFAULT_TYPE):
    code = context.user_data.get("code_digits", "")
    client = context.user_data.get("temp_client", None)
    phone = context.user_data.get("phone", "")
    phone_code_hash = context.user_data.get("phone_code_hash", "")
    user_id = query.from_user.id

    loggin_debug(f"[CONFIRM] Starting confirm_code_entry for {phone}, user_id: {user_id}")

    if not code or client is None or not phone_code_hash:
        loggin_debug("[CONFIRM] Missing code, client, or phone_code_hash.")
        await query.answer("کد یا اطلاعات ورود ناقص است.", show_alert=True)
        return
#5
    try:
        if not client.is_connected():
            fix_debug(f"[CONFIRM] Client not connected. Connecting...")
            await client.connect()

            if not await client.is_user_authorized():
                fix_debug(f"[CONFIRM] Client not authorized after connect.")
                # Optional: handle unauthenticated session here if needed
            else:
                await client.get_me()

        try:
            loggin_debug(f"[CONFIRM] Signing in with phone={phone}, code={code}")
            await client.sign_in(phone=phone, code=code, phone_code_hash=phone_code_hash)
        except Exception as sign_in_error:
            if not await client.is_user_authorized():
                loggin_debug(f"[CONFIRM] Sign-in failed: {sign_in_error}")
                raise sign_in_error

        me = await client.get_me()
#@@@
        session_path = context.user_data.get("session_path") or os.path.join("data/sessions", f"session_{user_id}_{phone}.session")
        loggin_debug(f"[CONFIRM] Signed in as {me.id}, session path: {session_path}")

        client.session.save()  # Ensure session is saved to correct path
        await asyncio.sleep(1)
        await client.disconnect()
        loggin_debug(f"[CONFIRM] Session saved and client disconnected for {phone}")

        # Clean up
        context.user_data.pop("temp_client", None)
        context.user_data.pop("phone", None)
        context.user_data.pop("code_digits", None)
        context.user_data.pop("phone_code_hash", None)
        loggin_debug(f"[CONFIRM] Cleared context for {phone}")

        # Save account info
        account_info = {
            "phone": phone,
            "name": me.first_name if me.first_name else phone,
            "groups": [],
            "normal": {"status": "off", "interval": None, "next_send": None, "banners": []}
        }
        accounts = get_tapchi_list(user_id)
        accounts.append(account_info)
        save_accounts(user_id, accounts)
        loggin_debug(f"[CONFIRM] Account info saved for {phone}")

        await update_groups_from_telethon(user_id, account_info)
        loggin_debug(f"[CONFIRM] Group update completed for {phone}")

        await query.answer("اکانت با موفقیت اضافه شد.", show_alert=True)
        await query.message.edit_text("اکانت اضافه شد.\nبرای بروزرسانی گروه‌ها از دکمه بروزرسانی گروه ها در پنل استفاده کنید.")
        loggin_debug(f"[CONFIRM] Finished successfully for {phone}")

    except Exception as e:
        loggin_debug(f"[CONFIRM] Error during confirm_code_entry for {phone}: {e}")
        await query.answer(f"خطا در ورود: {e}", show_alert=True)

async def show_code_keypad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code_so_far = context.user_data.get("code_digits", "")
    text = f"📲 کد دریافتی از تلگرام را وارد کنید:\n\ncode: {code_so_far}"
    keypad = build_code_keypad(code_so_far)
    await update.message.reply_text(text, reply_markup=keypad)

# /add_account ConversationHandler
async def add_account_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    # Check if the user has any active subscription
    if not is_subscription_valid(user_id):
        await update.message.reply_text(
            "⚠️ <b>اشتراک فعال یافت نشد</b> ⚠️\n\n"
            "برای استفاده از امکانات ربات تپچی، ابتدا باید اشتراک تهیه کنید.\n\n"
            "🛒 از منوی اصلی گزینه <b>خرید اشتراک</b> را انتخاب کنید.",
            parse_mode="HTML"
        )
        return ConversationHandler.END

# Check how many accounts the user has and how many are allowed
    accounts = get_tapchi_list(user_id)
    allowed = 0
    subs = user_subscriptions.get(str(user_id), [])
    tehran = pytz.timezone("Asia/Tehran")
    for s in subs:
        expiry = datetime.fromisoformat(s["expiry"])
        if expiry.tzinfo is None:
            expiry = tehran.localize(expiry)
        else:
            expiry = expiry.astimezone(tehran)
        now = datetime.now(tehran)
        if now < expiry:
            allowed += s.get("allowed_accounts", 0)
    
    # Show account usage information
    current = len(accounts)
    if current >= allowed:
        await update.message.reply_text(
            "⚠️ <b>محدودیت تعداد اکانت</b> ⚠️\n\n"
            f"🔢 <b>وضعیت اکانت‌های شما:</b>\n"
            f"• تعداد اکانت‌های فعلی: <code>{current}</code>\n"
            f"• حداکثر مجاز: <code>{allowed}</code>\n\n"
            "برای افزایش ظرفیت اکانت‌ها، لطفا از منوی اصلی گزینه <b>خرید اشتراک</b> را انتخاب کنید و پلن بالاتری تهیه نمایید.",
            parse_mode="HTML"
        )
        return ConversationHandler.END

    # If checks pass, ask for the phone number (+98 only) with contact keyboard
    phone_kb = ReplyKeyboardMarkup(
        [
            [KeyboardButton("📲 ارسال شماره من", request_contact=True)],
            ["لغو"]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    
    # Show account usage before asking for phone
    await update.message.reply_text(
        "✅ <b>افزودن اکانت جدید</b>\n\n"
        f"🔢 <b>وضعیت اکانت‌های شما:</b>\n"
        f"• اکانت‌های فعلی: <code>{current}</code>\n"
        f"• حداکثر مجاز: <code>{allowed}</code>\n"
        f"• باقیمانده: <code>{allowed - current}</code>\n\n"
        "🇮🇷 <b>توجه:</b> فقط شماره‌های ایرانی (+98) قابل استفاده هستند.\n\n"
        "<b>لطفاً شماره تلگرام خود را به یکی از روش‌های زیر وارد کنید:</b>\n"
        "• <code>+989123456789</code>\n"
        "• <code>09123456789</code>\n"
        "• <code>989123456789</code>\n"
        "یا از دکمه زیر برای ارسال شماره استفاده کنید:",
        reply_markup=phone_kb,
        parse_mode="HTML"
    )
    return WAIT_PHONE
#120
async def wait_phone_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    loggin_debug("Entered wait_phone_handler")

    # Accept contact or plain text
    phone_raw = None
    if getattr(update.message, "contact", None) and update.message.contact and update.message.contact.phone_number:
        phone_raw = update.message.contact.phone_number
    elif update.message.text:
        # Allow cancel
        text_lower = update.message.text.strip().lower()
        if text_lower in ["لغو", "cancel", "انصراف", "exit"]:
            await update.message.reply_text("فرایند اضافه کردن اکانت لغو شد.")
            return ConversationHandler.END
        phone_raw = update.message.text.strip()

    phone = normalize_iran_phone(phone_raw)
    if not phone:
        phone_kb = ReplyKeyboardMarkup(
            [[KeyboardButton("📲 ارسال شماره من", request_contact=True)], ["لغو"]],
            resize_keyboard=True,
            one_time_keyboard=True
        )
        await update.message.reply_text(
            "⛔️ شماره معتبر نیست!\n\n"
            "🇮🇷 <b>فقط شماره‌های ایران</b> با فرمت‌های زیر پذیرفته می‌شوند:\n"
            "• +989xxxxxxxxx\n"
            "• 09xxxxxxxxx\n"
            "• 989xxxxxxxxx\n\n"
            "🔄 لطفا دوباره ارسال کنید یا از دکمه زیر استفاده کنید.",
            reply_markup=phone_kb,
            parse_mode='HTML'
        )
        return WAIT_PHONE

    loggin_debug(f"Received phone number: {phone}")

    session_filename = f"session_{update.effective_user.id}_{phone}.session"
    session_path = os.path.join(SESSION_DIR, session_filename)
    loggin_debug(f"Session path: {session_path}")

    api_id, api_hash = get_next_api_credentials(update.effective_user.id, phone)
    loggin_debug(f"API credentials retrieved: api_id={api_id}, api_hash={api_hash}")

    client = TelegramClient(session_path, api_id, api_hash)
    loggin_debug("TelegramClient created")

    context.user_data["session_path"] = session_path
    loggin_debug("Saved session_path in context")

    try:
        await client.connect()
        loggin_debug("Connected to Telegram")

        if not await client.is_user_authorized():
            loggin_debug("Client not authorized, sending code request...")
            result = await client.send_code_request(phone)
            context.user_data["phone_code_hash"] = result.phone_code_hash
            loggin_debug(f"Code sent. phone_code_hash: {result.phone_code_hash}")
        else:
            loggin_debug("Client already authorized, retrieving profile...")
            await client.get_me()
            client.session._conn.execute("PRAGMA busy_timeout = 200000")
            loggin_debug("Busy timeout set on DB connection")

    except Exception as e:
        loggin_debug(f"Exception in wait_phone_handler: {e}")
        await update.message.reply_text(f"خطا در ارسال کد: {e}")
        return ConversationHandler.END

    context.user_data["temp_client"] = client
    context.user_data["phone"] = phone
    context.user_data["code_digits"] = ""
    loggin_debug("Client and session state saved to context")

    await show_code_keypad(update, context)
    loggin_debug("Code keypad shown to user")

    return ConversationHandler.END

async def process_banner_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if this is a forwarded message
    if update.message.forward_from_chat:
        channel, message_id = extract_forward_info(update.message)
        if channel and message_id:
            # Format as a t.me link
            if channel.startswith('-100'):
                # This is a private channel ID, we can't create a direct link
                banner_text = f"فوروارد از کانال با شناسه {channel} و پیام {message_id}"
            else:
                # This is a public channel with username
                banner_text = f"https://t.me/{channel}/{message_id}"
                
            context.user_data["temp_banner"] = banner_text
            if "banner_adding_for" in context.user_data:
                idx, panel_mode = context.user_data["banner_adding_for"]
                confirmation_text = f"بنر فوروارد شده:\n{banner_text}"
                keyboard = InlineKeyboardMarkup([
                    [InlineKeyboardButton("ثبت کردن بنر✅", callback_data=(f"confirm_new_banner:{idx}" if panel_mode != "gm" else "confirm_new_banner_gm"))],
                    [InlineKeyboardButton("↪️بازگشت↩️", callback_data=(f"{panel_mode}:{idx}:back" if panel_mode != "gm" else "gm_back"))]
                ])
                context.user_data.pop("in_set_banner_mode", None)
                await update.message.reply_text(confirmation_text, reply_markup=keyboard)
                return True
        else:
            # If forward info extraction failed, treat as regular message
            if update.message.text:
                new_banner = update.message.text.strip()
                if new_banner:
                    context.user_data["temp_banner"] = new_banner
                    if "banner_adding_for" in context.user_data:
                        idx, panel_mode = context.user_data["banner_adding_for"]
                        confirmation_text = f"بنر جدید شما:\n{new_banner}"
                        keyboard = InlineKeyboardMarkup([
                            [InlineKeyboardButton("ثبت کردن بنر✅", callback_data=(f"confirm_new_banner:{idx}" if panel_mode != "gm" else "confirm_new_banner_gm"))],
                            [InlineKeyboardButton("↪️بازگشت↩️", callback_data=(f"{panel_mode}:{idx}:back" if panel_mode != "gm" else "gm_back"))]
                        ])
                        context.user_data.pop("in_set_banner_mode", None)
                        await update.message.reply_text(confirmation_text, reply_markup=keyboard)
                        return True
            return False
    
    # Regular text message handling
    elif update.message.text:
        new_banner = update.message.text.strip()
        if new_banner:
            context.user_data["temp_banner"] = new_banner
            if "banner_adding_for" in context.user_data:
                idx, panel_mode = context.user_data["banner_adding_for"]
                confirmation_text = f"بنر جدید شما:\n{new_banner}"
                keyboard = InlineKeyboardMarkup([
                    [InlineKeyboardButton("ثبت کردن بنر✅", callback_data=(f"confirm_new_banner:{idx}" if panel_mode != "gm" else "confirm_new_banner_gm"))],
                    [InlineKeyboardButton("↪️بازگشت↩️", callback_data=(f"{panel_mode}:{idx}:back" if panel_mode != "gm" else "gm_back"))]
                ])
                context.user_data.pop("in_set_banner_mode", None)
                await update.message.reply_text(confirmation_text, reply_markup=keyboard)
                return True
    
    return False


# In set banner mode only process banner input
async def banner_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    if context.user_data.get("in_set_banner_mode"):
        # Handle both text and forwarded messages
        return await process_banner_input(update, context)
    return False

# Banner manager functions
async def show_banner_manager_after_adding(update, context, idx: int, panel_mode: str):
    user = update.from_user if update.from_user else update.message.from_user
    user_id = user.id
    phone_info = get_tapchi_list(user_id)[idx]
    banners = phone_info["normal"]["banners"]
    if not banners:
        text = ("❗️ بنری تنظیم نشده است ❗️\n\nبرای تنظیم بنر، روی دکمه «📥اضافه کردن بنر📥» کلیک کنید. 📢👇")
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("📥اضافه کردن بنر📥", callback_data=f"banner_mgr:{panel_mode}:{idx}:add")],
            [InlineKeyboardButton("↪️بازگشت↩️", callback_data=f"{panel_mode}:{idx}:back")]
        ])
    else:
        snippet = banners[0][:20]
        text = f"بنر تنظیم شده: [{snippet}...]"
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("❌حذف بنر❌", callback_data=f"banner_mgr:{panel_mode}:{idx}:delall")],
            [InlineKeyboardButton("↪️بازگشت↩️", callback_data=f"{panel_mode}:{idx}:back")]
        ])
    try:
        await update.message.edit_text(text, reply_markup=markup)
    except Exception as e:
        logging.error("Error editing message in show_banner_manager_after_adding: " + str(e))
        await update.message.reply_text(text, reply_markup=markup)

async def show_banner_manager(query, context, idx: int, panel_mode: str, edit=True):
    user_id = query.from_user.id
    phone_info = get_tapchi_list(user_id)[idx]
    banners = phone_info["normal"]["banners"]
    if not banners:
        text = ("❗️ بنری تنظیم نشده است ❗️\n\nبرای تنظیم بنر، روی دکمه «📥اضافه کردن بنر📥» کلیک کنید. 📢👇")
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("📥اضافه کردن بنر📥", callback_data=f"banner_mgr:{panel_mode}:{idx}:add")],
            [InlineKeyboardButton("↪️بازگشت↩️", callback_data=f"{panel_mode}:{idx}:back")]
        ])
    else:
        snippet = banners[0][:20]
        text = f"بنر تنظیم شده: [{snippet}...]"
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("❌حذف بنر❌", callback_data=f"banner_mgr:{panel_mode}:{idx}:delall")],
            [InlineKeyboardButton("↪️بازگشت↩️", callback_data=f"{panel_mode}:{idx}:back")]
        ])
    if edit:
        try:
            await query.message.edit_text(text, reply_markup=markup)
        except BadRequest as e:
            if "Message is not modified" in str(e):
                pass
            else:
                raise
        await query.answer()
    else:
        try:
            await query.message.delete()
        except:
            pass
        await query.message.chat.send_message(text, reply_markup=markup)

async def process_banner_deletion(query: Update, context: ContextTypes.DEFAULT_TYPE, idx: int, panel_mode: str):
    user_id = query.from_user.id
    phone_info = get_tapchi_list(user_id)[idx]
    phone_info["normal"]["banners"] = []
    save_accounts(user_id, phone_list)
    await query.answer("بنر حذف شد❌️", show_alert=True)
    await show_normal_panel(query, context, idx, phone_info)

# SHOW INTERVAL PICKER – for setting time in normal panel
async def show_interval_picker(query, context, idx, panel_type):
    row1 = [InlineKeyboardButton(str(i), callback_data=f"interval_pick:{panel_type}:{idx}:{i}") for i in range(1, 6)]
    row2 = [InlineKeyboardButton(str(i), callback_data=f"interval_pick:{panel_type}:{idx}:{i}") for i in range(6, 11)]
    row3 = [InlineKeyboardButton(str(i), callback_data=f"interval_pick:{panel_type}:{idx}:{i}") for i in range(15, 40, 5)]
    row4 = [InlineKeyboardButton(str(i), callback_data=f"interval_pick:{panel_type}:{idx}:{i}") for i in range(40, 65, 5)]
    back_row = [InlineKeyboardButton("↪️بازگشت↩️", callback_data=f"back_interval_picker:{panel_type}:{idx}")]
    keyboard = InlineKeyboardMarkup([row1, row2, row3, row4, back_row])
    await query.message.edit_text("انتخاب کنید (دقیقه):", reply_markup=keyboard)

# TAPCHI MENU (مدیریت اکانت)
async def show_tapchi_menu(update_or_query, context: ContextTypes.DEFAULT_TYPE):
    if isinstance(update_or_query, Update):
        chat_id = update_or_query.effective_chat.id
        user_id = update_or_query.effective_user.id
    else:
        chat_id = update_or_query.message.chat.id
        user_id = update_or_query.from_user.id
    phone_list = get_tapchi_list(user_id)
    
    # Send the account list message (header only or with additional text if desired)
    header = (
    "〽️مدیریت اکانت〽️\n"
    "❗️ برای باز شدن دستورات تپچی روی شماره مورد نظر کلیک کنید"
)
    if not phone_list:
        header = (
        "〽️مدیریت اکانت〽️\n"
        "لیست تبچی‌های شما:\n"
        "❗️شما هیچ تپچی ای اضاف نکرده اید\n"
        "❗️ برای اضافه کردن اکانت جدید دستور /add_account را بفرستید"
    )
#@@@    
        await context.bot.send_message(
            chat_id=chat_id,
            text=header,
            reply_to_message_id=get_reply_id(update_or_query)
        )
        return
        
    rows = []
    for idx, pinfo in enumerate(phone_list):
        init_phone_info(pinfo)
        row1 = [InlineKeyboardButton(f"👤 {pinfo.get('name', pinfo.get('phone', 'NoName'))} 👤", callback_data=f"tapchi_select:{idx}"),
                InlineKeyboardButton(f"{pinfo['phone']}", callback_data=f"tapchi_select:{idx}")]
        row2 = [InlineKeyboardButton("حذف❌", callback_data=f"tapchi_ask_delete:{idx}"),
                InlineKeyboardButton("♻️وضعیت ♻️", callback_data=f"tapchi_status:{idx}")]
        row3 = [InlineKeyboardButton(" ", callback_data="noop")]
        rows.extend([row1, row2, row3])
    markup = InlineKeyboardMarkup(rows)
    # Send the account list message with the inline keyboard
#@@@    
    await context.bot.send_message(
        chat_id=chat_id,
        text=header,
        reply_markup=markup,
        reply_to_message_id=get_reply_id(update_or_query)
    )
    
    # Now, send the instructions in a separate message so they appear below:
    instructions = (
        "❗️ برای اضافه کردن اکانت جدید دستور /add_account را بفرستید."
    )
#@@@    
    await context.bot.send_message(
        chat_id=chat_id,
        text=instructions,
        reply_to_message_id=get_reply_id(update_or_query)
    )
# SCHEDULE PANELS
async def show_schedule_menu(query, context, idx: int, phone_info: dict):
    from telegram.error import BadRequest
    text = ("🔰 تنظیمات ارسال زمان‌دار 🔰")
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀پیام معمولی🚀", callback_data=f"schedule_menu:{idx}:normal"),
         InlineKeyboardButton("🚀پیام فوروارد🚀", callback_data=f"schedule_menu:{idx}:forward")],
        [InlineKeyboardButton("↪️بازگشت↩️", callback_data=f"schedule_menu:{idx}:back")]
    ])
    try:
        await query.message.edit_text(text, reply_markup=keyboard)
    except BadRequest as e:
        if "Message is not modified" in str(e):
            pass
        else:
            raise
#j
# NORMAL PANEL – 🚀پیام معمولی🚀 section
async def show_normal_panel(query, context, idx, phone_info):
    from telegram.error import BadRequest
    panel_data = phone_info["normal"]
    prefix = "normal_panel"
    status_label = "روشن ✅" if panel_data["status"] == "on" else "خاموش ❌"
    interval = panel_data["interval"] if panel_data["interval"] else 5
    group_count = len(phone_info.get("groups", []))
    tehran = pytz.timezone("Asia/Tehran")
    if panel_data.get("next_send") and panel_data["status"] == "on":
        dt = datetime.fromisoformat(panel_data["next_send"])
        if dt.tzinfo is None:
            dt = tehran.localize(dt)
        else:
            dt = dt.astimezone(tehran)
        next_str = dt.strftime("%Y/%m/%d %H:%M")
    else:
        next_str = "-"
    text = (f"📊 وضعیت : {status_label}\n"
            f"⏳زمان ارسال : {interval} دقیقه یک بار\n"
            f"🗣 تعداد گروه‌ها : {group_count}\n"
            f"🗓 زمان ارسال بعدی : {next_str}")
    toggle_label = "❌خاموش کردن❌" if panel_data["status"] == "on" else "✅روشن کردن✅"
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("⏳تنظیم زمان⏳", callback_data=f"{prefix}:{idx}:set_time"),
         InlineKeyboardButton("📤تنظیم بنر 📤", callback_data=f"{prefix}:{idx}:set_banner")],
        [InlineKeyboardButton("♻️بروزرسانی گروه‌ها♻️", callback_data=f"{prefix}:{idx}:refresh")],
        [InlineKeyboardButton(toggle_label, callback_data=f"{prefix}:{idx}:turn_on")],
        [InlineKeyboardButton("↪️بازگشت↩️", callback_data=f"schedule_menu:{idx}:back")]
    ])
    try:
        await query.message.edit_text(text, reply_markup=markup)
    except BadRequest as e:
        if "Message is not modified" in str(e):
            pass
        else:
            raise
#h            
async def show_forward_panel(query, context, idx, phone_info):
    panel_data = phone_info["forward"]
    status_label = "روشن ✅" if panel_data["status"] == "on" else "خاموش ❌"
    interval = panel_data["interval"] if panel_data["interval"] is not None else 5
    group_count = len(phone_info.get("groups", []))
    tehran = pytz.timezone("Asia/Tehran")
    
    if panel_data.get("next_send") and panel_data["status"] == "on":
        dt = datetime.fromisoformat(panel_data["next_send"])
        if dt.tzinfo is None:
            dt = tehran.localize(dt)
        else:
            dt = dt.astimezone(tehran)
        next_str = dt.strftime("%Y/%m/%d %H:%M")
    else:
        next_str = "-"
    text = (f"📊 وضعیت : {status_label}\n"
            f"⏳زمان ارسال : {interval} دقیقه یک بار\n"
            f"🗣 تعداد گروه‌ها : {group_count}\n"
            f"🗓 زمان ارسال بعدی : {next_str}")
    toggle_label = "❌خاموش کردن❌" if panel_data["status"] == "on" else "✅روشن کردن✅"
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("⏳تنظیم زمان⏳", callback_data=f"forward_panel:{idx}:set_time"),
         InlineKeyboardButton("📤تنظیم بنر 📤", callback_data=f"forward_panel:{idx}:set_banner")],
        [InlineKeyboardButton("♻️بروزرسانی گروه‌ها♻️", callback_data=f"forward_panel:{idx}:refresh")],
        [InlineKeyboardButton(toggle_label, callback_data=f"forward_panel:{idx}:toggle")],
        [InlineKeyboardButton("↪️بازگشت↩️", callback_data=f"schedule_menu:{idx}:back")]
    ])
    try:
        await query.message.edit_text(text, reply_markup=markup)
    except Exception as e:
        logging.error("Error editing forward panel: " + str(e))            
            
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import BadRequest


async def show_phone_management(query, context, idx: int, phone_info: dict):
    phone = phone_info["phone"]
    name = phone_info.get("name", phone)
    text = f"مدیریت اکانت «{name}» با شماره {phone}"

    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("❖ ارسال پیام زمان‌دار ❖", callback_data=f"phone_menu:{idx}:schedule")],
        [InlineKeyboardButton("❖ شناسایی عضویت اجباری ❖", callback_data=f"phone_menu:{idx}:detect_forced_solo")],
        [InlineKeyboardButton("❖ عضو شدن در گروه‌ها ❖", callback_data=f"phone_menu:{idx}:join_groups")],
        [InlineKeyboardButton("❖ ارسال پیام همگانی به پیوی ❖", callback_data=f"phone_menu:{idx}:broadcast_pm_solo")],
        [InlineKeyboardButton("❖ حذف تمام گروه‌ها و کانال‌ها ❖", callback_data=f"phone_menu:{idx}:remove_all_solo")],
        [InlineKeyboardButton("❖ مشاهده لیست گروه‌های اکانت ❖", callback_data=f"phone_menu:{idx}:groups")],
        [InlineKeyboardButton("❖ افزودن عکس پروفایل اکانت ❖", callback_data=f"phone_menu:{idx}:add_profile_photo_solo")],
        [
            InlineKeyboardButton("❖ ویرایش نام ❖", callback_data=f"phone_menu:{idx}:edit_name_solo"),
            InlineKeyboardButton("❖ ویرایش بیو ❖", callback_data=f"phone_menu:{idx}:edit_bio_solo")
        ],
        [InlineKeyboardButton("❖ بازگشت به منو ❖", callback_data=f"phone_menu:{idx}:back")]
    ])

    try:
        await query.message.edit_text(text, reply_markup=markup)
    except BadRequest as e:
        if "Message is not modified" not in str(e):
            raise
#119            
async def send_and_check_group(session_path: str, client: TelegramClient, group: dict, user_id: int, chat_id: int, context: ContextTypes.DEFAULT_TYPE, wait_time=3) -> str:
    """
    Checks spambot status, sends a test message to a group, and checks if the message is deleted (forced join detection).

    Returns:
      "spambot_not_ok" if the spambot response is not good,
      "no_forced_join" if message remains,
      "forced_join_needed" if message is deleted,
      "error" on any exception.
    """
    lock = get_session_lock(session_path)
    async with lock:
        # 1. Check the spambot status first
        spambot_ok = await check_spambot_for_account(client, user_id, context)
        if not spambot_ok:
            logging.info(f"Spambot check failed for account {user_id}. Skipping group: {group.get('link')}")
            return "spambot_not_ok"

        try:
            # 2. Send a test message
            sent_msg = await client.send_message(group["id"], "سلام")
            await asyncio.sleep(wait_time)

            # 3. See if message was deleted (forced join detected)
            check_msg = await client.get_messages(group["id"], ids=sent_msg.id)
            return "no_forced_join" if check_msg else "forced_join_needed"

        except Exception as e:
            logging.warning(f"[JOIN-FAIL SILENCED] Group: {group.get('link')} | Reason: {e}")
            return "error"
#118        
async def send_and_check_group_without_spambot(client: TelegramClient, group: dict, user_id: int, chat_id: int, context: ContextTypes.DEFAULT_TYPE, wait_time=3) -> str:
    """
    Sends a "سلام" message to the given group (without checking spambot) and waits.
    Then it checks if the message is still present.
    
    Returns:
      "no_forced_join" if the message is still there,
      "forced_join_needed" if the message was deleted,
      "limited_group" if an exception occurs (treated as limited),
      "error" if another error occurred.
    """
    try:
        sent_msg = await client.send_message(group["id"], "سلام")
        await asyncio.sleep(wait_time)
        check_msg = await client.get_messages(group["id"], ids=sent_msg.id)
        if check_msg:
            return "no_forced_join"
        else:
            return "forced_join_needed"
    except Exception as e:
        error_text = str(e).lower()
        if any(err in error_text for err in ["forbidden", "not in the chat", "can't write", "restricted", "permission"]):
            return "limited_group"
        return "error"

async def show_phone_groups(query, context, idx: int, phone_info: dict):
    groups = phone_info["groups"]
    phone = phone_info["phone"]

    if not groups:
        text_chunks = [f"اکانت: {phone}\nهیچ گروهی یافت نشد."]
    else:
        header = f"اکانت: {phone}\nگروه‌های شما:\n"
        footer = f"\nتعداد کلی گروه‌های شما: {len(groups)}"
        chunks = []
        chunk = header

        for i, g in enumerate(groups, 1):
            link = g.get("link")
            if not link:
                username = g.get("username")
                if username:
                    link = f"@{username}"
                else:
                    link = f"ID: {g.get('id', 'نامشخص')}"
            line = f"{i}: {link}\n"
            if len(chunk) + len(line) + len(footer) > 3900:
                chunks.append(chunk.strip())
                chunk = ""
            chunk += line

        if chunk:
            chunk += footer
            chunks.append(chunk.strip())

        text_chunks = chunks

    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("↪️بازگشت↩️", callback_data=f"phone_menu:{idx}:back")]
    ])

    try:
        for i, part in enumerate(text_chunks):
            if i == 0:
                await query.message.edit_text(part)
            elif i == len(text_chunks) - 1:
                await context.bot.send_message(chat_id=query.message.chat_id, text=part, reply_markup=markup)
            else:
                await context.bot.send_message(chat_id=query.message.chat_id, text=part)
    except Exception as e:
        logging.error("Error in show_phone_groups: " + str(e))
    
async def show_general_management_panel(update_or_query, context: ContextTypes.DEFAULT_TYPE):
    user = update_or_query.from_user if hasattr(update_or_query, 'from_user') else update_or_query.message.from_user
    user_id = user.id
    user_name = user.first_name
    accounts = get_tapchi_list(user_id)
    num_accounts = len(accounts)
#@@@    
    text = (f"🌟 کاربر {user_name} عزیز، به پنل کنترل همگانی تپچی‌ها خوش آمدید! 🌟\n"
            f"تعداد کل اکانت‌های شما: {num_accounts}\n\n"
            "اطلاع: توی این پنل هرکاری انجام بدید برای همه اکانت‌هاتون ثبت میشه، پس حواستون باشه.")    
    
# Build the inline keyboard with one button per row for first two buttons, then two buttons per row for the rest
    row1  = [InlineKeyboardButton("❈ ارسال پیام معمولی به گروه ❈", callback_data="gm_timebound")]
    row2  = [InlineKeyboardButton("❈ ارسال پیام فوروارد به گروه ❈", callback_data="gm_forward")]
    row3  = [
        InlineKeyboardButton("❈ بررسی وضعیت ❈", callback_data="gm_account_status"),
        InlineKeyboardButton("❈ عضویت اجباری ❈", callback_data="gm_identify")
    ]
    row4  = [
        InlineKeyboardButton("❈ عضویت در گروه ❈", callback_data="gm_join_groups"),
        InlineKeyboardButton("❈ ارسال پیام همگانی ❈", callback_data="gm_broadcast_pv")
    ]
    row5  = [
        InlineKeyboardButton("❈ ساعت کنار اسم ❈", callback_data="Clock_on_the_right"),
        InlineKeyboardButton("❈ منشی خودکار اکانت ❈", callback_data="Auto_reply")
    ]
    row6  = [
        InlineKeyboardButton("❈ استخراج از لینکدونی ❈", callback_data="linkdoni_find_groups"),
        InlineKeyboardButton("❈ آمار اکانت ها ❈", callback_data="accounts_state")
    ]        
    row7  = [
        InlineKeyboardButton("❈ حذف گروه/کانال ها ❈", callback_data="gm_delete_all_groups"),
        InlineKeyboardButton("❈ تغییر عکس پروفایل ❈", callback_data="gm_edit_photo")
    ]
    row8  = [
        InlineKeyboardButton("❈ ویرایش بیو اکانت ❈", callback_data="gm_edit_bio"),
        InlineKeyboardButton("❈ ویرایش نام اکانت ❈", callback_data="gm_edit_name")
    ]

    keyboard = InlineKeyboardMarkup([
        row1, row2, row3, row4, row5, row6, row7, row8
    ])
#@@@ Send or edit the message accordingly
    if hasattr(update_or_query, "edit_message_text"):
        await update_or_query.edit_message_text(text, reply_markup=keyboard)
    else:
        await update_or_query.message.reply_text(
            text,
            reply_markup=keyboard,
            reply_to_message_id=get_reply_id(update_or_query)
        )

async def general_timebound_panel(update_or_query, context: ContextTypes.DEFAULT_TYPE):
    text = ("پنل عادی زمان دار همگانی:\n"
            "• تنظیم زمان: فاصله زمانی (1 الی 60 دقیقه)\n"
            "• تنظیم بنر: بنر جدید برای تمامی اکانت‌ها (جایگزین بنر قبلی)\n"
            "• بروزرسانی گروه ها: گروه‌های جدید را شناسایی می‌کند.\n"
            "• روشن/خاموش: همه اکانت‌ها را یکجا روشن یا خاموش کنید.")
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("⏳تنظیم زمان⏳", callback_data="gm_timebound_interval_show")],
        [InlineKeyboardButton("📥تنظیم بنر 📥", callback_data="gm_set_banner")],
        [InlineKeyboardButton("♻️بروزرسانی گروه ها♻️", callback_data="gm_update_all_groups")],
        [InlineKeyboardButton("✅روشن/خاموش❌", callback_data="gm_timebound_toggle")],
        [InlineKeyboardButton("↪️بازگشت↩️", callback_data="gm_back")]
    ])
    if hasattr(update_or_query, "edit_message_text"):
        await update_or_query.edit_message_text(text, reply_markup=keyboard)
    else:
        await update_or_query.message.reply_text(text, reply_markup=keyboard)
       
                
async def general_forward_panel(update_or_query, context: ContextTypes.DEFAULT_TYPE):
    text = ("پنل فوروارد زمان دار همگانی:\n"
            "• تنظیم زمان: فاصله زمانی (1 الی 60 دقیقه)\n"
            "• تنظیم بنر: بنر جدید برای تمامی اکانت‌ها (جایگزین بنر قبلی)\n"
            "• بروزرسانی گروه ها: گروه‌های جدید را شناسایی می‌کند.\n"
            "• روشن/خاموش: همه اکانت‌ها را یکجا روشن یا خاموش کنید.")
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("⏳تنظیم زمان⏳", callback_data="gm_forward_set_time")],
        [InlineKeyboardButton("📥تنظیم بنر 📥", callback_data="gm_set_forward_banner")],
        [InlineKeyboardButton("♻️بروزرسانی گروه ها♻️", callback_data="gm_update_all_groups")],
        [InlineKeyboardButton("✅روشن/خاموش❌", callback_data="gm_forward_toggle")],
        [InlineKeyboardButton("↪️بازگشت↩️", callback_data="gm_back")]
    ])
    if hasattr(update_or_query, "edit_message_text"):
        await update_or_query.edit_message_text(text, reply_markup=keyboard)
    else:
        await update_or_query.message.reply_text(text, reply_markup=keyboard)       

async def general_set_time(update_or_query, context: ContextTypes.DEFAULT_TYPE, mode="timebound"):
    label = "پیام فوروارد" if mode == "forward" else "پیام معمولی"
    callback_prefix = "gm_forward_set_time" if mode == "forward" else "gm_timebound_set_time"

    set_banner_debug(f"Setting time for mode: {mode}, prefix: {callback_prefix}")

    # Your requested time steps: 1-10, then 15 to 60
    time_options = list(range(1, 11)) + list(range(15, 61, 5))
    set_banner_debug(f"Time options generated: {time_options}")

    buttons = [InlineKeyboardButton(f"{i}", callback_data=f"{callback_prefix}:{i}") for i in time_options]
    set_banner_debug(f"{len(buttons)} buttons created.")

    # Group into rows of 4
    keyboard = []
    for i in range(0, len(buttons), 4):
        keyboard.append(buttons[i:i + 4])

    # Add Back Button
    back_button = InlineKeyboardButton("↩️بازگشت↩️", callback_data="gm_forward_back" if mode == "forward" else "gm_back")
    keyboard.append([back_button])
    set_banner_debug("Back button appended.")

    try:
        await update_or_query.message.edit_text(
            f"لطفاً زمان ارسال {label} را به دقیقه انتخاب کنید:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        set_banner_debug("Time selection message sent successfully.")
    except Exception as e:
        set_banner_debug(f"Failed to send time selection message: {e}")
        await context.bot.send_message(
            chat_id=update_or_query.effective_user.id,
            text="❌ خطا در تنظیم زمان"
        )
    
            
# NEW CODE: Start Handler Function
#async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    main_menu_keyboard = ReplyKeyboardMarkup(
#        [
#            ["〽️مدیریت اکانت〽️", "〽️کنترل همگانی〽️"],
#            ["🛒خرید اشتراک🛒", "👤اطلاعات کاربر👤"],
#            ["🔰اموزش استفاده🔰", "📜راهنما و قوانین📜"],
#            ["💰شارژ حساب💰"]
#        ],
#        resize_keyboard=True
#    )
#    await update.message.reply_text(
#        "به ربات تپچی خوش آمدید! لطفاً یک گزینه را انتخاب کنید:",
#        reply_markup=main_menu_keyboard
#    )

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

# ==================== TICKET SYSTEM UI FUNCTIONS ====================

async def show_support_menu(update_or_query, context: ContextTypes.DEFAULT_TYPE):
    """Show support menu to users"""
    user_id = update_or_query.effective_user.id
    
    # Count user's open tickets
    user_tickets = get_user_tickets(user_id)
    open_count = len([t for t in user_tickets if t["status"] == "open"])
    total_count = len(user_tickets)
    
    message = (
        "🎫 <b>سیستم پشتیبانی تپچی</b> 🎫\n\n"
        "💬 <b>خوش آمدید به بخش پشتیبانی!</b>\n\n"
        f"📊 آمار تیکت‌های شما:\n"
        f"🔸 تیکت‌های باز: <code>{open_count}</code>\n"
        f"🔸 کل تیکت‌ها: <code>{total_count}</code>\n\n"
        "🔽 <b>لطفاً یکی از گزینه‌های زیر را انتخاب کنید:</b>"
    )
    
    keyboard = [
        [InlineKeyboardButton("✍️ ایجاد تیکت جدید", callback_data="create_ticket")],
        [InlineKeyboardButton("📋 مشاهده تیکت‌های من", callback_data="view_my_tickets")],
        [InlineKeyboardButton("🔙 بازگشت به منوی اصلی", callback_data="start_menu")]
    ]
    
    markup = InlineKeyboardMarkup(keyboard)
    
    if hasattr(update_or_query, 'callback_query') and update_or_query.callback_query:
        await update_or_query.callback_query.edit_message_text(message, reply_markup=markup, parse_mode="HTML")
    elif hasattr(update_or_query, 'message'):
        await update_or_query.message.reply_text(message, reply_markup=markup, parse_mode="HTML")
    else:
        # This is likely a callback query object directly
        await update_or_query.edit_message_text(message, reply_markup=markup, parse_mode="HTML")

async def show_user_tickets(query, context: ContextTypes.DEFAULT_TYPE):
    """Show user's tickets"""
    user_id = query.from_user.id
    tickets = get_user_tickets(user_id)
    
    if not tickets:
        message = (
            "📋 <b>تیکت‌های شما</b>\n\n"
            "❌ شما هنوز هیچ تیکتی ایجاد نکرده‌اید.\n\n"
            "💡 برای ایجاد تیکت جدید، روی دکمه زیر کلیک کنید:"
        )
        keyboard = [
            [InlineKeyboardButton("✍️ ایجاد تیکت جدید", callback_data="create_ticket")],
            [InlineKeyboardButton("🔙 بازگشت", callback_data="support_menu")]
        ]
    else:
        message = f"📋 <b>تیکت‌های شما ({len(tickets)} عدد)</b>\n\n"
        
        keyboard = []
        for i, ticket in enumerate(tickets[:10]):  # Show max 10 tickets
            status_emoji = "🟢" if ticket["status"] == "open" else "🔴"
            replies_count = len(ticket["replies"])
            
            # Format date
            try:
                date_obj = datetime.fromisoformat(ticket["timestamp"])
                date_str = date_obj.strftime("%m/%d")
            except:
                date_str = "N/A"
            
            button_text = f"{status_emoji} {ticket['id']} ({replies_count} پاسخ) - {date_str}"
            keyboard.append([InlineKeyboardButton(button_text, callback_data=f"view_ticket_{ticket['id']}")])
        
        keyboard.append([InlineKeyboardButton("✍️ ایجاد تیکت جدید", callback_data="create_ticket")])
        keyboard.append([InlineKeyboardButton("🔙 بازگشت", callback_data="support_menu")])
    
    markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(message, reply_markup=markup, parse_mode="HTML")

async def show_ticket_details(query, context: ContextTypes.DEFAULT_TYPE, ticket_id: str):
    """Show detailed view of a ticket"""
    ticket = get_ticket_by_id(ticket_id)
    user_id = query.from_user.id
    
    if not ticket:
        await query.edit_message_text("❌ تیکت مورد نظر یافت نشد.", 
                                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data="view_my_tickets")]]))
        return
    
    # Check if user owns this ticket or is admin
    if ticket["user_id"] != user_id and user_id != ADMIN_ID:
        await query.edit_message_text("❌ شما دسترسی به این تیکت را ندارید.", 
                                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data="view_my_tickets")]]))
        return
    
    status_emoji = "🟢 باز" if ticket["status"] == "open" else "🔴 بسته"
    
    try:
        date_obj = datetime.fromisoformat(ticket["timestamp"])
        date_str = date_obj.strftime("%Y/%m/%d %H:%M")
    except:
        date_str = "نامشخص"
    
    message = (
        f"🎫 <b>تیکت #{ticket['id']}</b>\n\n"
        f"📅 تاریخ: <code>{date_str}</code>\n"
        f"📊 وضعیت: {status_emoji}\n"
        f"👤 کاربر: {ticket.get('user_name', 'نامشخص')}\n\n"
        f"💬 <b>پیام اولیه:</b>\n{ticket['message']}\n\n"
    )
    
    if ticket["replies"]:
        message += "💭 <b>پاسخ‌ها:</b>\n\n"
        for reply in ticket["replies"]:
            sender = "🔹 ادمین" if reply["is_admin"] else "🔸 شما"
            try:
                reply_date = datetime.fromisoformat(reply["timestamp"]).strftime("%m/%d %H:%M")
            except:
                reply_date = "N/A"
            
            message += f"{sender} ({reply_date}):\n{reply['text']}\n\n"
    
    keyboard = []
    
    if ticket["status"] == "open":
        if user_id == ADMIN_ID:
            keyboard.append([InlineKeyboardButton("💬 پاسخ دادن", callback_data=f"reply_ticket_{ticket_id}")])
            keyboard.append([InlineKeyboardButton("🔒 بستن تیکت", callback_data=f"close_ticket_{ticket_id}")])
        else:
            keyboard.append([InlineKeyboardButton("💬 پاسخ دادن", callback_data=f"reply_ticket_{ticket_id}")])
    
    if user_id == ADMIN_ID:
        keyboard.append([InlineKeyboardButton("🔙 بازگشت به پنل ادمین", callback_data="admin_tickets")])
    else:
        keyboard.append([InlineKeyboardButton("🔙 بازگشت به تیکت‌ها", callback_data="view_my_tickets")])
    
    markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(message, reply_markup=markup, parse_mode="HTML")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # Reset any previous state to avoid stuck states
    clear_user_flags(context)
    
    # Check if maintenance mode is enabled (except for admin)
    if context.bot_data.get("maintenance_mode", False) and user_id != 7135477742:
        maintenance_message = (
            "🔧 <b>ربات در حال تعمیر و اپدیت است</b> 🔧\n\n"
            "🔄 <b>اپدیت جدید در حال نصب</b> 🔄\n\n"
            "✨ در حال بهبود عملکرد و اضافه قابلیت‌های جدید \n"
            "🚀 به زودی با قابلیت‌های بیشتر برمی‌گردیم\n\n"
            "🕰 <b>لطفاً چند دقیقه دیگر تلاش کنید</b>\n\n"
            "📞 <b>پشتیبانی:</b> @YourSupportBot\n\n"
            "🔥 <b>تپچی پیشرفته</b> - بهترین ربات مدیریت اکانت"
        )
        
        await update.message.reply_text(
            maintenance_message,
            parse_mode="HTML",
            reply_to_message_id=update.message.message_id
        )
        return
    
    main_menu_keyboard = ReplyKeyboardMarkup(
        [
            ["⚡️ مدیریت اکانت ⚡️", "🔄 کنترل همگانی 🔄"],
            ["🛒 خرید اشتراک 🛒", "👤 اطلاعات کاربر 👤"],
            ["📚 آموزش استفاده 📚", "⚖️ راهنما و قوانین ⚖️"],
            ["💰 شارژ حساب 💰", "🔔 پشتیبانی 🔔"]
        ],
        resize_keyboard=True
    )
    
    # Get current date in Persian calendar (if jdatetime is available)
    try:
        import jdatetime
        today = jdatetime.datetime.now().strftime("%Y/%m/%d")
        date_text = f"📅 تاریخ امروز: <code>{today}</code>"
    except ImportError:
        from datetime import datetime
        today = datetime.now().strftime("%Y/%m/%d")
        date_text = f"📅 تاریخ: <code>{today}</code>"
    
    # Create a welcome message with better formatting
    welcome_text = (
        f"✨ <b>به ربات حرفه‌ای تپچی خوش آمدید</b> ✨\n\n"
        f"👋 سلام <a href='tg://user?id={update.message.from_user.id}'>{update.message.from_user.first_name}</a> عزیز\n\n"
        f"🤖 <b>تپچی پیشرفته</b> - ابزار قدرتمند مدیریت اکانت‌های تلگرام\n"
        f"🇮🇷 <b>ویژه کاربران ایرانی</b> - فقط با شماره‌های +98\n\n"
        f"{date_text}\n\n"
        f"🔰 از منوی زیر گزینه مورد نظر خود را انتخاب کنید\n\n"
        f"💡 <b>نکته:</b> اگر در هر مرحله‌ای گیر کردید، دستور /reset را بفرستید."
    )
    
    await update.message.reply_text(
        welcome_text,
        reply_markup=main_menu_keyboard,
        reply_to_message_id=update.message.message_id,
        parse_mode="HTML"
    )
    
async def main_text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Immediately capture and store the user's ID.
    user_id = update.effective_user.id
    logging.debug(f"User ID stored: {user_id}")

    # ==================== TICKET SYSTEM TEXT HANDLERS ====================
    
    # Handle ticket message creation
    if context.user_data.get("awaiting_ticket_message"):
        message_text = update.message.text.strip()
        context.user_data.pop("awaiting_ticket_message", None)
        
        if message_text.lower() in ["لغو", "cancel", "exit"]:
            await update.message.reply_text(
                "❌ ایجاد تیکت لغو شد.",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت به پشتیبانی", callback_data="support_menu")]])
            )
            return
        
        # Create the ticket
        user_name = f"{update.effective_user.first_name or ''} {update.effective_user.last_name or ''}".strip()
        ticket_id = create_ticket(user_id, message_text, user_name)
        
        await update.message.reply_text(
            f"✅ <b>تیکت با موفقیت ایجاد شد!</b>\n\n"
            f"🎫 <b>شماره تیکت:</b> <code>#{ticket_id}</code>\n\n"
            f"💬 <b>پیام شما:</b>\n{message_text}\n\n"
            "🕰 تیکت شما به تیم پشتیبانی ارسال شد و به زودی پاسخ دریافت خواهید کرد.\n\n"
            "📧 برای پیگیری تیکت خود، از بخش پشتیبانی استفاده کنید.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📋 مشاهده تیکت‌های من", callback_data="view_my_tickets")],
                [InlineKeyboardButton("🔙 بازگشت به پشتیبانی", callback_data="support_menu")]
            ]),
            parse_mode="HTML"
        )
        
        # Notify admin about new ticket
        try:
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"🎫 <b>تیکت جدید دریافت شد!</b>\n\n"
                     f"🆔 <b>شماره تیکت:</b> <code>#{ticket_id}</code>\n"
                     f"👤 <b>کاربر:</b> {user_name} (<code>{user_id}</code>)\n\n"
                     f"💬 <b>پیام:</b>\n{message_text}",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("💬 پاسخ دادن", callback_data=f"reply_ticket_{ticket_id}")],
                    [InlineKeyboardButton("🔒 بستن تیکت", callback_data=f"close_ticket_{ticket_id}")],
                    [InlineKeyboardButton("📋 همه تیکت‌ها", callback_data="admin_tickets")]
                ]),
                parse_mode="HTML"
            )
        except Exception as e:
            logging.error(f"Error notifying admin about new ticket: {e}")
        
        return
    
    # Handle ticket reply
    elif context.user_data.get("awaiting_ticket_reply"):
        reply_text = update.message.text.strip()
        ticket_id = context.user_data.get("current_ticket_id")
        
        context.user_data.pop("awaiting_ticket_reply", None)
        context.user_data.pop("current_ticket_id", None)
        
        if not ticket_id:
            await update.message.reply_text("❌ خطا: تیکت یافت نشد.")
            return
        
        if reply_text.lower() in ["لغو", "cancel", "exit"]:
            await update.message.reply_text(
                "❌ پاسخ لغو شد.",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت به تیکت", callback_data=f"view_ticket_{ticket_id}")]])
            )
            return
        
        # Add reply to ticket
        sender_name = f"{update.effective_user.first_name or ''} {update.effective_user.last_name or ''}".strip()
        is_admin = user_id == ADMIN_ID
        
        if add_reply_to_ticket(ticket_id, reply_text, is_admin, sender_name):
            await update.message.reply_text(
                f"✅ <b>پاسخ شما به تیکت #{ticket_id} ارسال شد</b>\n\n"
                f"💬 <b>پاسخ شما:</b>\n{reply_text}",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("💫 مشاهده تیکت", callback_data=f"view_ticket_{ticket_id}")],
                    [InlineKeyboardButton("🔙 بازگشت به تیکت‌ها", callback_data="view_my_tickets" if not is_admin else "admin_tickets")]
                ]),
                parse_mode="HTML"
            )
            
            # Notify the other party about the reply
            ticket = get_ticket_by_id(ticket_id)
            if ticket:
                target_user_id = ADMIN_ID if not is_admin else ticket["user_id"]
                if target_user_id != user_id:  # Don't notify yourself
                    try:
                        notification_text = (
                            f"🔔 <b>پاسخ جدید برای تیکت #{ticket_id}</b>\n\n"
                            f"👤 <b>از:</b> {sender_name}\n\n"
                            f"💬 <b>پیام:</b>\n{reply_text}"
                        )
                        await context.bot.send_message(
                            chat_id=target_user_id,
                            text=notification_text,
                            reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton("💬 پاسخ دادن", callback_data=f"reply_ticket_{ticket_id}")],
                                [InlineKeyboardButton("💫 مشاهده تیکت", callback_data=f"view_ticket_{ticket_id}")]
                            ]),
                            parse_mode="HTML"
                        )
                    except Exception as e:
                        logging.error(f"Error notifying about ticket reply: {e}")
        else:
            await update.message.reply_text("❌ خطا در ارسال پاسخ. لطفاً دوباره تلاش کنید.")
        
        return

# --- Original: Handle per-account forward banner ---
    if context.user_data.get("awaiting_forward_banner") is not None:
        idx = context.user_data.pop("awaiting_forward_banner")
        new_banner = update.message.text.strip()
        accounts = get_tapchi_list(user_id)
        phone_info = accounts[idx]

        if new_banner.startswith("http"):
            phone_info["forward"]["banner"] = new_banner
            save_accounts(user_id, accounts)
            text = f"بنر انتخابی شما تایید شد✅️\nلینک بنر: {new_banner}"
            markup = InlineKeyboardMarkup([
                [InlineKeyboardButton("↪️بازگشت↩️", callback_data=f"forward_panel:{idx}:back")]
            ])
            await update.message.reply_text(text, reply_markup=markup)

            # Call send_forward__banner_from_account to perform forwarding and send the report.
            await send_forward_banner_for_account(phone_info, user_id, from_chat_id, message_id, context)
        else:
            await update.message.reply_text("لینک بنر نامعتبر است. لطفا لینک معتبر ارسال کنید یا ❌️لغو❌️ را بزنید.")
        return
            
# --- Handle waiting state for /send_msg ---
    if context.user_data.get("conversation_state") == "WAITING_FOR_BROADCAST_TEXT":
        text = update.message.text
        count = 0
        all_users = get_all_known_user_ids()  # Make sure this function is defined
        for uid in all_users:
            try:
                await context.bot.send_message(chat_id=uid, text=text)
                count += 1
            except:
                continue
        await update.message.reply_text(f"✅ پیام به {count} نفر ارسال شد.")
        context.user_data.pop("conversation_state", None)
        return              
#@@@
# --- Handle Linkdoni: Receive linkdoni channel link ---
    if context.user_data.get("linkdoni_state") == "awaiting_link_input":
        text = update.message.text.strip()
        if text.lower() in ["لغو", "cancel", "exit"]:
            context.user_data.pop("linkdoni_state", None)
            await update.message.reply_text("فرایند استخراج لغو شد.")
            return
#@@@
        if not text.startswith("https://t.me/"):
            context.user_data.pop("linkdoni_state", None)
            await update.message.reply_text("لینک لینکدونی اشتباه بود❌️")
            return

        context.user_data["linkdoni_link"] = text
        context.user_data["linkdoni_state"] = "awaiting_count"
        await update.message.reply_text(
            "لینک با موفقیت دریافت شد✅️\nچه تعدادی گروه میخواهید استخراج کنید؟\nبین ۱ تا ۲۰۰",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌️لغو❌️", callback_data="cancel_linkdoni")]
            ])
        )
        return

# --- Handle Linkdoni: Receive desired number of group links ---
    if context.user_data.get("linkdoni_state") == "awaiting_count":
        try:
            count = int(update.message.text.strip())
            if not 1 <= count <= 200:
                await update.message.reply_text("لطفا عددی بین ۱ تا ۲۰۰ انتخاب کنید:")
                return
        except:
            context.user_data.pop("linkdoni_state", None)
            await update.message.reply_text("ورودی نامعتبر بود. عملیات لغو شد.")
            return

        context.user_data.pop("linkdoni_state", None)
        link = context.user_data.pop("linkdoni_link", None)
        await update.message.reply_text("جستجو در لینکدونی شروع شد لطفا صبر کنید...")

# --- Start link extraction in background ---
        phone_list = get_tapchi_list(user_id)
        phone = phone_list[0]["phone"]  # You can select based on logic

        asyncio.create_task(run_linkdoni_extraction(
            user_id=user_id,
            phone=phone,
            link=link,
            count=count,
            context=context,
            chat_id=update.effective_chat.id
        ))

        # Do NOT send file here! Let run_linkdoni_extraction send it after generating
        return
                
# ---
    if context.user_data.get("gm_set_banner_forward"):
        user_id = update.effective_user.id
        new_banner = update.message.text.strip()
        set_banner_debug(f"Received link: {new_banner}")

        # Improved validation: ensure it starts correctly and has at least two segments after the base
        if new_banner.startswith("https://t.me/") and len(new_banner.strip("/").split("/")) >= 2:
            set_banner_debug("Link format is valid.")

            accounts = get_tapchi_list(user_id)
            for acc in accounts:
                acc.setdefault("forward", {})["banner"] = new_banner
                set_banner_debug(f"Activated link for account {acc['phone']}")

            save_accounts(user_id, accounts)
            set_banner_debug("Accounts saved with new banner.")

            context.user_data.pop("gm_set_banner_forward", None)
            set_banner_debug("User flag cleared from context.")

            await update.message.reply_text(
                f"بنر جدید برای پیام فوروارد ثبت شد ✅\n{new_banner}",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("↩️بازگشت↩️", callback_data="gm_forward_back")]
                ])
            )
        else:
            set_banner_debug("Link validation failed. Does not match Telegram format.")
            context.user_data.pop("gm_set_banner_forward", None)
            await update.message.reply_text("❌️لینک معتبر نیست❌️")
        return
        
        
# --- Monshi: ثبت پیام جدید منشی معمولی ---
    if context.user_data.get("awaiting_normal_monshi"):
        user_id = update.effective_user.id
        msg = update.message.text.strip()
        context.user_data.pop("awaiting_normal_monshi", None)
        context.user_data["last_normal_monshi_input"] = msg

        await update.message.reply_text(
            f"⚜️پیام انتخابی شما:\n{msg}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅️ثبت این پیام✅️", callback_data="save_normal_monshi")],
                [InlineKeyboardButton("❌️لغو❌️", callback_data="normal_monshi")]
            ])
        )
        return

# --- Monshi: ثبت trigger برای منشی پیشرفته ---
    if context.user_data.get("awaiting_advanced_trigger"):
        user_id = update.effective_user.id
        trigger = update.message.text.strip()
        context.user_data.pop("awaiting_advanced_trigger", None)
        context.user_data["advanced_trigger"] = trigger
        context.user_data["awaiting_advanced_reply"] = True

        await update.message.reply_text(
            f"پیام اول شما:\n\"{trigger}\"\n\n"
            "لطفاً پیام دوم رو ثبت کنید.\n"
            "این پیام به کسی که این کلمه رو ارسال کنه داده میشه:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("↪️بازگشت↩️", callback_data="advanced_monshi")]
            ])
        )
        return

# --- Monshi: ثبت reply برای منشی پیشرفته ---
    if context.user_data.get("awaiting_advanced_reply"):
        user_id = update.effective_user.id
        reply = update.message.text.strip()
        context.user_data.pop("awaiting_advanced_reply", None)
        context.user_data["advanced_reply"] = reply

        trigger = context.user_data.get("advanced_trigger", "پیام تعریف‌نشده")

        await update.message.reply_text(
            f"پیام اول شما:\n\"{trigger}\"\n"
            f"پیام دوم شما:\n\"{reply}\"",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅️ثبت این پیام برای منشی پیشرفته✅️", callback_data="save_advanced_monshi")],
                [InlineKeyboardButton("❌️لغو❌️", callback_data="advanced_monshi")]
            ])
        )
        return
        
        
    # ... rest of your main text handling logic follows ...
    if context.user_data.get("in_set_banner_mode"):
        processed = await process_banner_input(update, context)
        if processed:
            return

# Process new bio input when waiting for ادیت بیو ها
    if context.user_data.get("awaiting_edit_bio"):
        clear_user_flags(context)
        new_bio = update.message.text.strip()
        context.user_data["new_bio"] = new_bio
        context.user_data.pop("awaiting_edit_bio")
        await update.message.reply_text(
            "بیو انتخابی شما:\n" + new_bio,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅️ثبت بیو✅️", callback_data="gm_confirm_edit_bio")],
                [InlineKeyboardButton("↩️بازگشت↩️", callback_data="gm_back")]
            ])
        )
        return

    # Process new names input when waiting for ادیت نام ها
    if context.user_data.get("awaiting_edit_name"):
        # Assume each line is in the format "1: name"
        lines = update.message.text.strip().split("\n")
        new_names = []
        for line in lines:
            parts = line.split(":", 1)
            if len(parts) == 2:
                new_names.append(parts[1].strip())
            else:
                new_names.append(line.strip())
        context.user_data["new_names"] = new_names
        context.user_data.pop("awaiting_edit_name")
        confirmation_text = "نام های انتخابی شما:\n"
        for idx, name in enumerate(new_names, start=1):
            confirmation_text += f"{idx}: {name}\n"
        await update.message.reply_text(
            confirmation_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅️ثبت نام ها✅️", callback_data="gm_confirm_edit_name")],
                [InlineKeyboardButton("↩️بازگشت↩️", callback_data="gm_back")]
            ])
        )
        return
# ... (the rest of your main_text_handler code follows here) ...            
    if context.user_data.get("phone_join_groups") is not None:
        idx = context.user_data.pop("phone_join_groups")
        text = update.message.text.strip()
        if text.lower() in ["لغو", "cancel", "exit"]:
            await update.message.reply_text("فرایند عضویت لغو شد.")
            return
#@@@
        links = []
        get_links_debug("Started link extraction block.")

        # Extract from text (if any)
        if update.message.text:
            stripped_text = update.message.text.strip()
            get_links_debug(f"Text message received: {stripped_text}")
            text_links = re.findall(r'((?:https?://)?t\.me/\S+|@\S+)', stripped_text)
            get_links_debug(f"Extracted {len(text_links)} links from text.")
            links += text_links

        # Also extract from .txt file (uploaded or forwarded)
        if getattr(update.message, "document", None):
            doc = update.message.document
            get_links_debug(f"Document received: {doc.file_name}")
            if doc.file_name.endswith(".txt"):
                try:
                    file = await doc.get_file()
                    file_path = await file.download_to_drive()
                    get_links_debug(f"Downloaded document to: {file_path}")
                    with open(file_path, "r", encoding="utf-8") as f:
                        for i, line in enumerate(f, 1):
                            match = re.search(r'((?:https?://)?t\.me/\S+|@\S+)', line)
                            if match:
                                link = match.group(1)
                                links.append(link)
                                get_links_debug(f"Line {i}: Found link → {link}")
                            else:
                                get_links_debug(f"Line {i}: No valid link.")
                except Exception as e:
                    get_links_debug(f"Error reading file: {e}")

        get_links_debug(f"Total collected links: {len(links)}")
        if not links:
            await update.message.reply_text("لینک اشتباه است.")
            return
            
        user_id = update.effective_user.id
        phone_list = get_tapchi_list(user_id)
        if 0 <= idx < len(phone_list):
            chat_id = update.effective_chat.id
            asyncio.create_task(process_phone_group_join(user_id, idx, links, chat_id, context))
            await update.message.reply_text("عملیات عضویت گروه‌ها در پس‌زمینه آغاز شد.")
            return
        else:
            await update.message.reply_text("اکانت نامعتبر است.")
            return
#@@@
    if context.user_data.get("gm_join_groups"):
        context.user_data.pop("gm_join_groups")
        text = update.message.text.strip() if update.message.text else ""
        links = []
        get_links_debug("Started GM group link extraction")

        # Extract from text
        if text:
            get_links_debug(f"Text received: {text}")
            text_links = re.findall(r'((?:https?://)?t\.me/\S+|@\S+)', text)
            get_links_debug(f"Extracted {len(text_links)} links from text.")
            links += text_links

        # Extract from .txt file
        if getattr(update.message, "document", None):
            doc = update.message.document
            get_links_debug(f"Document received: {doc.file_name}")
            if doc.file_name.endswith(".txt"):
                try:
                    file = await doc.get_file()
                    file_path = await file.download_to_drive()
                    get_links_debug(f"Downloaded document to: {file_path}")
                    with open(file_path, "r", encoding="utf-8") as f:
                        for i, line in enumerate(f, 1):
                            match = re.search(r'((?:https?://)?t\.me/\S+|@\S+)', line)
                            if match:
                                link = match.group(1)
                                links.append(link)
                                get_links_debug(f"Line {i}: Found link → {link}")
                            else:
                                get_links_debug(f"Line {i}: No valid link.")
                except Exception as e:
                    get_links_debug(f"Error reading file: {e}")

        get_links_debug(f"Total GM links collected: {len(links)}")

        if not links:
            await update.message.reply_text("لینک اشتباه است.")
            return

        if text.lower() in ["لغو", "cancel", "exit"]:
            await update.message.reply_text("فرایند عضویت لغو شد.")
            return

        user_id = update.effective_user.id
        chat_id = update.effective_chat.id
        asyncio.create_task(process_gm_group_join(user_id, links, chat_id, context))
        await update.message.reply_text("عملیات عضویت گروه‌ها در پس‌زمینه آغاز شد.")
        return
        
        
        
        
        
    if context.user_data.get("gm_set_banner"):
        await update.message.reply_text("دستور نامشخص!")
        return
    text = update.message.text
    user_id = update.effective_user.id
    if text == "〽️مدیریت اکانت〽️" or text == "⚡️ مدیریت اکانت ⚡️":
        await show_tapchi_menu(update, context)
    elif text == "〽️کنترل همگانی〽️" or text == "🔄 کنترل همگانی 🔄":
        
        await show_general_management_panel(update, context)
#buytest        
    elif text == "🛒خرید اشتراک🛒" or text == "🛒 خرید اشتراک 🛒":
        user_id = update.message.from_user.id
        buttons = []

        if not is_trial_active(user_id):
            buttons.append([InlineKeyboardButton("🔰تپچی تست 6 ساعته رایگان🔰", callback_data="buy_trial:6:0")])
#@@@
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 1 اکانت: 30,000 تومان 🟣", callback_data="buy_subscription:1:30000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 2 اکانت: 60,000 تومان 🟣", callback_data="buy_subscription:2:60000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 3 اکانت: 90,000 تومان 🟣", callback_data="buy_subscription:3:90000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 4 اکانت: 120,000 تومان 🟣", callback_data="buy_subscription:4:120000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 5 اکانت: 150,000 تومان 🟣", callback_data="buy_subscription:5:150000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 6 اکانت: 180,000 تومان 🟣", callback_data="buy_subscription:6:180000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 7 اکانت: 210,000 تومان 🟣", callback_data="buy_subscription:7:210000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 8 اکانت: 240,000 تومان 🟣", callback_data="buy_subscription:8:240000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 9 اکانت: 270,000 تومان 🟣", callback_data="buy_subscription:9:270000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 10 اکانت: 300,000 تومان 🟣", callback_data="buy_subscription:10:300000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 20 اکانت: 600,000 تومان 🟣", callback_data="buy_subscription:20:600000")])

        kb = InlineKeyboardMarkup(buttons)
#@@@        
        await update.message.reply_text(
            "لطفا اشتراک مورد نظر خود را انتخاب کنید:",
            reply_markup=kb,
            reply_to_message_id=get_reply_id(update)
        )
#dataa        
    elif text == "👤 اطلاعات کاربر 👤" or text == "👤اطلاعات کاربر👤":
        bal = get_balance(user_id)
        accounts = get_tapchi_list(user_id)
        num_accounts = len(accounts)
        subs = user_subscriptions.get(str(user_id), [])

        if isinstance(subs, dict):
            subs = [subs]
        tehran = pytz.timezone("Asia/Tehran")
        active_subs = []
        
        # Get current date in Persian calendar
        try:
            import jdatetime
            today = jdatetime.datetime.now().strftime("%Y/%m/%d")
        except ImportError:
            from datetime import datetime
            today = datetime.now().strftime("%Y/%m/%d")
            
        for s in subs:
            expiry_dt = datetime.fromisoformat(s["expiry"])
            # If expiry_dt is naive, localize it to Tehran time.
            if expiry_dt.tzinfo is None:
                expiry_dt = tehran.localize(expiry_dt)
            else:
                expiry_dt = expiry_dt.astimezone(tehran)
            now_dt = datetime.now(tehran)
            if expiry_dt > now_dt:
                active_subs.append(s)
                
        if active_subs:
            days_left = max((datetime.fromisoformat(s["expiry"]).astimezone(tehran) - datetime.now(tehran)).days for s in active_subs)
            total_allowed = sum(s["allowed_accounts"] for s in active_subs)
            
            # Try to format expiry date in Persian calendar
            try:
                import jdatetime
                expiry_date = jdatetime.datetime.fromgregorian(
                    datetime=max(datetime.fromisoformat(s["expiry"]).astimezone(tehran) for s in active_subs)
                ).strftime("%Y/%m/%d")
            except ImportError:
                expiry_date = max(datetime.fromisoformat(s["expiry"]).astimezone(tehran) for s in active_subs).strftime("%Y/%m/%d")
        else:
            days_left = "-"
            total_allowed = 0
            expiry_date = "-"

        # Get user's Telegram info if available
        user_name = update.effective_user.first_name
        if update.effective_user.last_name:
            user_name += " " + update.effective_user.last_name
        username = update.effective_user.username or "-"
        
        # Create a better formatted user information message
        msg = (
            f"📊 <b>اطلاعات کاربری شما</b> 📊\n\n"
            f"👤 <b>اطلاعات شخصی:</b>\n"
            f"• نام: <code>{user_name}</code>\n"
            f"• نام کاربری: @{username}\n"
            f"• شناسه: <code>{user_id}</code>\n\n"
            f"💰 <b>اطلاعات مالی:</b>\n"
            f"• موجودی: <code>{bal:,} تومان</code>\n\n"
            f"🔑 <b>وضعیت اشتراک:</b>\n"
            f"• تاریخ امروز: <code>{today}</code>\n"
            f"• تاریخ انقضا: <code>{expiry_date}</code>\n"
            f"• زمان باقیمانده: <code>{days_left} روز</code>\n\n"
            f"📱 <b>اکانت‌های تلگرام:</b>\n"
            f"• تعداد اکانت‌های فعلی: <code>{num_accounts}</code>\n"
            f"• حداکثر اکانت مجاز: <code>{total_allowed}</code>\n"
            f"• باقیمانده: <code>{max(0, total_allowed - num_accounts)}</code>")

# Show remaining time if user is in 1-hour trial
        if is_trial_active(user_id):
            trials = load_trials()
            trial = trials.get(str(user_id))
            expiry = datetime.fromisoformat(trial["expiry"])
            if expiry.tzinfo is None:
                expiry = tehran.localize(expiry)
            else:
                expiry = expiry.astimezone(tehran)
            now = datetime.now(tehran)
            remaining_minutes = max(0, int((expiry - now).total_seconds() // 60))
            msg += f"\n⏱ زمان باقی مانده از تست: {remaining_minutes} دقیقه"
#@@@
        await update.message.reply_text(
            msg,
            reply_to_message_id=get_reply_id(update),
            parse_mode="HTML"
        )
#@@@        
    elif text == "📚 آموزش استفاده 📚" or text == "🔰اموزش استفاده🔰":
        tutorial_msg = (
            "📚 <b>راهنمای جامع استفاده از ربات تپچی</b> 📚\n\n"
            "<b>1. اضافه کردن حساب:</b>\n"
            "• از دستور <code>/add_account</code> استفاده کنید\n"
            "• شماره تلفن خود را با فرمت <code>+989XXXXXXXXX</code> ارسال کنید\n"
            "• <b>توجه:</b> فقط شماره‌های ایران (+98) پذیرفته می‌شوند\n"
            "• کد دریافتی از تلگرام را وارد نمایید\n\n"
            "<b>2. مدیریت اکانت:</b>\n"
            "• با کلیک روی گزینه <b>⚡️ مدیریت اکانت ⚡️</b> در منوی اصلی، لیست حساب‌های شما نمایش داده می‌شود\n"
            "• با انتخاب هر حساب به پنل مدیریت آن دسترسی پیدا می‌کنید\n"
            "• در این پنل می‌توانید تنظیمات بنر، زمان ارسال پیام، به‌روزرسانی گروه‌ها و وضعیت حساب را مدیریت کنید\n\n"
            "<b>3. تنظیم اکانت برای ارسال بنر:</b>\n"
            "برای تنظیم ارسال بنر دو روش وجود دارد:\n\n"
            "<b>روش اول - از طریق کنترل همگانی:</b>\n"
            "• گزینه <b>🔄 کنترل همگانی 🔄</b> را انتخاب کنید\n"
            "• روی <b>ارسال پیام معمولی/فوروارد به گروه</b> کلیک کنید\n"
            "• زمان ارسال را بین ۱ تا ۶۰ دقیقه تنظیم کنید\n"
            "• بنر خود را ثبت کنید (برای ارسال معمولی متن بنر و برای فوروارد لینک پست را ارسال کنید)\n"
            "• روی <b>بروزرسانی گروه‌ها</b> کلیک کنید تا گروه‌های اکانت شما وارد ربات شود\n"
            "• با کلیک روی <b>روشن/خاموش</b> اکانت‌ها را فعال کنید\n\n"
            "<b>روش دوم - از طریق مدیریت اکانت:</b>\n"
            "• روی <b>⚡️ مدیریت اکانت ⚡️</b> کلیک کنید\n"
            "• شماره اکانت مورد نظر را انتخاب کنید تا وارد پنل مدیریت آن شوید\n"
            "• روی <b>ارسال زمان‌دار</b> کلیک کنید\n"
            "• بین ارسال معمولی و فوروارد یکی را انتخاب کنید\n"
            "• زمان ارسال را بین ۱ تا ۶۰ دقیقه تنظیم کنید\n"
            "• بنر خود را ثبت کنید (برای ارسال معمولی متن بنر و برای فوروارد لینک پست را ارسال کنید)\n"
            "• روی <b>بروزرسانی گروه‌ها</b> کلیک کنید تا گروه‌های اکانت شما وارد ربات شود\n"
            "• با کلیک روی <b>روشن/خاموش</b> اکانت‌ها را فعال کنید\n\n"
            "<b>نکته مهم:</b> در بخش مدیریت اکانت می‌توانید زمان ارسال بعدی، تعداد گروه‌ها و تنظیمات را مشاهده کنید، اما در کنترل همگانی فقط امکان تنظیم وجود دارد.\n\n"
            "<b>4. کنترل همگانی:</b>\n"
            "• با استفاده از گزینه <b>🔄 کنترل همگانی 🔄</b> می‌توانید:\n"
            "• پیام‌های دسته‌جمعی را برای تمامی حساب‌ها تنظیم کنید\n"
            "• وضعیت همه اکانت‌ها را یکجا بررسی کنید\n"
            "• تنظیمات مشترک را برای همه اکانت‌ها اعمال کنید\n\n"
            "<b>⚠️ هشدار:</b> کنترل همگانی باعث تغییر در همه اکانت‌های شما می‌شود. هنگام تغییر نام یا بیو، حتماً مقادیر متفاوتی برای هر اکانت استفاده کنید تا همه اکانت‌ها یکسان نباشند.\n\n"
            "<b>5. پشتیبانی:</b>\n"
            "• برای دریافت راهنمایی بیشتر با پشتیبانی تماس بگیرید\n"
            "• تمامی خدمات فقط برای شماره‌های ایران (+98) ارائه می‌شود\n"
            "در صورت بروز هرگونه مشکل یا نیاز به راهنمایی بیشتر، لطفاً با پشتیبانی ربات صحبت کنید."
        )
#@@@    
        await update.message.reply_text(
            tutorial_msg,
            reply_to_message_id=get_reply_id(update),
            parse_mode="HTML"
        )
#@@@        
    elif text == "⚖️ راهنما و قوانین ⚖️" or text == "📜راهنما و قوانین📜":
        rules_text = (
        "⚖️ <b>راهنما و قوانین استفاده از تپچی</b> ⚖️\n\n"
        "⚠️ <b>توجه ویژه:</b> لطفاً این قوانین را با دقت مطالعه کنید تا از بن شدن یا حذف اکانت‌های شما جلوگیری شود.\n\n"
        "<b>1. استفاده از اکانت‌های ایرانی (+98):</b>\n"
        "• <b>فقط از شماره‌های ایرانی استفاده کنید</b>\n"
        "• احتمال بن شدن اکانت‌های ایرانی بسیار کمتر است\n"
        "• طول عمر اکانت‌های ایرانی در تپچی بیشتر از اکانت‌های خارجی است\n\n"
        
        "<b>2. تنظیم زمان ارسال:</b>\n"
        "• زمان ارسال را بالای <b>10 دقیقه</b> تنظیم کنید\n"
        "• برای امنیت بیشتر، زمان بالای <b>20 دقیقه</b> پیشنهاد می‌شود\n"
        "• زمان کمتر احتمال محدودیت اکانت را افزایش می‌دهد\n\n"
        
        "<b>3. مدیریت اکانت‌های محدود شده:</b>\n"
        "• اگر اکانتی محدود شد (نتوانست پیام ارسال کند)، آن را موقتاً خاموش کنید\n"
        "• پس از رفع محدودیت، می‌توانید دوباره آن را فعال کنید\n"
        "• اکانت‌های با محدودیت دائمی را کنار بگذارید و از اکانت جدید استفاده کنید\n\n"
        
        "<b>4. استفاده تدریجی از اکانت جدید:</b>\n"
        "• با اکانت جدید به تدریج عضو گروه‌ها شوید\n"
        "• از عضویت در تعداد زیادی گروه در روز اول خودداری کنید\n"
        "• تلگرام نسبت به فعالیت‌های ناگهانی اکانت‌های جدید حساس است\n"
        "• ابتدا چند روز فقط عضو گروه‌ها شوید، سپس ارسال بنر را شروع کنید\n\n"
        
        "<b>5. خطای فلود (Flood Error):</b>\n"
        "• تنظیم زمان ارسال بسیار کوتاه می‌تواند منجر به خطای فلود شود\n"
        "• این خطا از طرف تلگرام است و به معنی ارسال بیش از حد پیام در زمان کوتاه است\n"
        "• اگر با وجود امکان ارسال دستی، ربات به گروهی پیام نمی‌فرستد، احتمالاً به دلیل این محدودیت است\n\n"
        
        "<b>🇮🇷 تأکید مجدد:</b> فقط از شماره‌های ایرانی (+98) استفاده کنید. شماره‌های غیر ایرانی به سرعت محدود یا حذف می‌شوند.\n\n"
        
        "🔹 <b>هدف ما:</b> ارائه خدمات با کیفیت و شفافیت کامل است. رعایت این قوانین به حفظ امنیت اکانت‌های شما و بهبود تجربه استفاده از ربات کمک می‌کند."
        )
#@@@        
        await update.message.reply_text(
            rules_text,
            reply_to_message_id=get_reply_id(update),
            parse_mode="HTML"
        )
#@@@        
    elif text == "💰شارژ حساب💰" or text == "💰 شارژ حساب 💰":
        await update.message.reply_text(
            "💰 <b>شارژ حساب</b> 💰\n\n"
            "برای شارژ حساب خود به پشتیبانی پیام دهید:\n"
            "🆔 @Telbot_charge",
            reply_to_message_id=get_reply_id(update),
            parse_mode="HTML"
        )
    elif text == "🔔 پشتیبانی 🔔":
        await show_support_menu(update, context)
    else:        
        await update.message.reply_text(
            "دستور نامشخص!",
            reply_to_message_id=get_reply_id(update)
        )
        
        
        
#117
async def process_phone_group_join(user_id: int, idx: int, links: list, chat_id, context: ContextTypes.DEFAULT_TYPE):
    phone_list = get_tapchi_list(user_id)
    if idx < 0 or idx >= len(phone_list):
        await context.bot.send_message(chat_id, "Invalid account index.")
        return

    acc = phone_list[idx]
    phone = acc['phone']
    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
    lock = session_locks.setdefault(session_path, asyncio.Lock())

    for i, link in enumerate(links, 1):
        async with lock:
            debug_groups(f"[SINGLE JOIN] Lock acquired for session {session_path}. Joining group {i}/{len(links)}.")

            client = None
            try:
                client = TelegramClient(session_path, API_ID, API_HASH)
#7
                await client.connect()

                if not await client.is_user_authorized():
                    await context.bot.send_message(chat_id, f"{phone}: ❌ نشست غیرمجاز است.")
                    await client.disconnect()
                    return

                await client.get_me()
                debug_groups(f"{phone}: Client connected.")

                username = extract_group_username(link)
                if not username:
                    await context.bot.send_message(chat_id, f"{phone}: ❌ لینک نامعتبر: {link}")
                    await client.disconnect()
                    continue

                already = any(username in g.get("link", "") or username in g.get("username", "")
                              for g in acc.get("groups", []))

                if already:
                    await context.bot.send_message(chat_id, f"{phone}: 📌 قبلاً عضو {link} بوده‌ام.")
                    await client.disconnect()
                    continue

                try:
                    await client(JoinChannelRequest(username))
                    await context.bot.send_message(chat_id, f"{phone}: ✅ با موفقیت عضو {link} شدم.")
                except Exception as e:
                    error_str = str(e).lower()
                    if "flood" in error_str or "wait" in error_str:
                        wait_seconds = int(re.search(r'\d+', error_str).group()) if re.search(r'\d+', error_str) else 60
                        await context.bot.send_message(chat_id, f"{phone}: ❌ محدودیت تلگرام. انتظار {wait_seconds} ثانیه...")
                        await client.disconnect()
                        await asyncio.sleep(wait_seconds)
                        continue
                    else:
                        await context.bot.send_message(chat_id, f"{phone}: ❌ خطا در عضویت {link}: {e}")
                        await client.disconnect()
                        await asyncio.sleep(5)
                        continue

                await client.disconnect()
                debug_groups(f"{phone}: Disconnected after joining group {username}.")

            except Exception as ex:
                await context.bot.send_message(chat_id, f"{phone}: ❌ خطای بحرانی: {ex}")
                if client:
                    try:
                        await client.disconnect()
                    except:
                        pass

        debug_groups(f"{phone}: Sleeping 120s before next group...")
        await asyncio.sleep(120)

    # Refresh groups after all joins
    await update_groups_from_telethon(user_id, acc)
    phone_list = get_tapchi_list(user_id)
    updated_acc = next((p for p in phone_list if p.get("phone") == acc.get("phone")), acc)
    save_accounts(user_id, phone_list)

# process_gm_group_join with updated group & session sync
#666



async def process_gm_group_join(user_id: int, links: list, chat_id, context):
    accounts = get_tapchi_list(user_id)
    debug_groups(f"Starting group join for user {user_id} with {len(accounts)} accounts and {len(links)} links.")

    tasks = []

    for idx, acc in enumerate(accounts):
        debug_groups(f"Queueing account {acc['phone']} with delay {idx}s.")
        task = asyncio.create_task(join_groups_one_by_one(user_id, acc, links, chat_id, context, idx))
        tasks.append(task)

    # Correct: just await gather (or return if you're in a handler)
    await asyncio.gather(*tasks, return_exceptions=True)

#imports
from telethon.tl.functions.messages import ImportChatInviteRequest

async def join_groups_one_by_one(user_id: int, acc: dict, links: list, chat_id, context, delay: int):
    await asyncio.sleep(delay)

    phone = acc['phone']
    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
    lock = session_locks.setdefault(session_path, asyncio.Lock())

    for i, link in enumerate(links, 1):
        async with lock:
            debug_groups(f"Lock acquired for session {session_path}. Starting join for group {i}.")

            client = None
            try:
                client = TelegramClient(session_path, API_ID, API_HASH)
#8
                await client.connect()

                if not await client.is_user_authorized():
                    debug_groups(f"{phone}: Unauthorized session.")
                    await context.bot.send_message(chat_id, f"{phone}: ❌ نشست غیرمجاز است.")
                    await client.disconnect()
                    continue

                await client.get_me()
                debug_groups(f"{phone}: Client connected.")

                debug_groups(f"{phone}: Preparing to join group {i}: {link}")
#@@@                
                is_invite = 'joinchat/' in link or 't.me/+' in link or link.startswith('+')
                if is_invite:
                    group_ref = link.split('/')[-1].lstrip('+')
                else:
                    group_ref = extract_group_username(link)
                    if not group_ref:
                        debug_groups(f"{phone}: Invalid group link.")
                        await context.bot.send_message(chat_id, f"{phone}: ❌ لینک نامعتبر: {link}")
                        await client.disconnect()
                        continue
#@@@
                already_joined = any(
                    group_ref in g.get("link", "") or group_ref in g.get("username", "")
                    for g in acc.get("groups", [])
                )

                if already_joined:
                    debug_groups(f"{phone}: Already a member of {group_ref}.")
                    await context.bot.send_message(chat_id, f"{phone}: قبلاً عضو {link} بوده‌ام.")
                    await client.disconnect()
                    continue

                try:
                    debug_groups(f"{phone}: Attempting to join {group_ref}.")
#aaa                    
                    if is_invite:
                        await client(ImportChatInviteRequest(group_ref))
                    else:
                        await client(JoinChannelRequest(group_ref))
                        
                    debug_groups(f"{phone}: Successfully joined {group_ref}.")
                    await context.bot.send_message(chat_id, f"{phone}: ✅ با موفقیت عضو {link} شدم.")

                except Exception as e:
                    msg = str(e).lower()
                    if "flood" in msg or "wait" in msg:
                        wait_seconds = int(re.search(r'\d+', msg).group()) if re.search(r'\d+', msg) else 60
                        debug_groups(f"{phone}: Flood wait detected. Waiting {wait_seconds * 2}s.")
                        await context.bot.send_message(chat_id, f"{phone}: ⚠️ محدودیت {wait_seconds}s. در حال صبر...")
                        await client.disconnect()
                        await asyncio.sleep(wait_seconds * 2)
                        continue
                    else:
                        debug_groups(f"{phone}: Join failed with error: {e}")
                        await context.bot.send_message(chat_id, f"{phone}: ❌ خطا هنگام عضویت: {e}")
                        await client.disconnect()
                        continue

                await client.disconnect()
                debug_groups(f"{phone}: Disconnected after joining.")

            except Exception as ex:
                debug_groups(f"{phone}: Critical error occurred: {ex}")
                await context.bot.send_message(chat_id, f"{phone}: ❌ خطا در اتصال یا عضویت: {ex}")
                if client:
                    try:
                        await client.disconnect()
                    except:
                        pass

        # Sleep AFTER releasing the lock
        debug_groups(f"{phone}: Sleeping 120s before next group...")
        await asyncio.sleep(120)
    
    
    
    
#115        
# GLOBAL STORE
auto_reply_tasks = {}

async def start_auto_reply_for_user(acc, user_id):
    phone = acc["phone"]
    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
    debug_monshi(f"[AUTO-REPLY] Initializing for {phone}")

    client = TelegramClient(session_path, API_ID, API_HASH)
    debug_monshi(f"[AUTO-REPLY] TelegramClient created for {phone}")

    if await safe_connect(client, acc, user_id, context=None):
        debug_monshi(f"[AUTO-REPLY] Safe connect OK for {phone}")
        task = asyncio.create_task(auto_reply_listener(client, acc, user_id))
        auto_reply_tasks[phone] = task
        debug_monshi(f"[AUTO-REPLY] Listener scheduled for {phone}")
    else:
        debug_monshi(f"[AUTO-REPLY] Safe connect failed for {phone}")

        
        

registered_clients = {} 
 # phone -> handler function

async def auto_reply_listener(client: TelegramClient, acc: dict, user_id: int):
    phone = acc.get("phone", "UNKNOWN")
    uid_str = str(user_id)
    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
    loggin_debug(f"[AUTO-REPLY] Searching for session of {phone} in {session_path}")
    lock = get_session_lock(session_path)

    lock_debug(f"[AUTO-REPLY] >>> auto_reply_listener ENTERED for {phone}")
    replied_users = set(all_replied_users.get(phone, []))
#@@@
    while True:
        if not is_auto_reply_enabled_for_account(user_id, phone):
            lock_debug(f"[AUTO-REPLY] Auto-reply disabled for {phone}. Exiting.")
            break

        fix_debug(f"[AUTO-REPLY] Attempting to acquire lock for {phone}...")
        await lock.acquire()
        fix_debug(f"[AUTO-REPLY] Lock acquired for {phone}")
#@@@
        try:
            await client.connect()
            await client.get_me()

            if not await client.is_user_authorized():
                fix_debug(f"[AUTO-REPLY] Not authorized — skipping {phone}")
                await client.disconnect()
                continue

            me = await client.get_me()
#@@@
            if phone not in registered_clients:    

                async def handler(event):
                    if not is_auto_reply_enabled_for_account(user_id, phone):
                        return
                    try:
#                        if event.sender_id == me.id:
#                            return
                        sender = await event.get_sender()
                        if not isinstance(sender, User) or sender.bot or sender.is_self:
                            return

                        sender_id = str(sender.id)
                        msg_text = event.raw_text.strip()
                        

                        adv_data = get_advanced_monshi(uid_str)
                        
                        if msg_text in adv_data:
                            
                            await client.send_message(sender.id, adv_data[msg_text])
                            fix_debug(f"[ADVANCED] Replied to {sender_id} on {phone}")
                            return

                        if sender_id in replied_users:
                            return

                        normal_msgs = get_normal_monshi(uid_str)
                        if normal_msgs:
                            await client.send_message(sender.id, random.choice(normal_msgs))
                            replied_users.add(sender_id)
                            all_replied_users[phone] = list(replied_users)
                            with open(REPLIED_USERS_FILE, "w") as f:
                                json.dump(all_replied_users, f)
                            fix_debug(f"[NORMAL] Replied to {sender_id} on {phone}")
                    except Exception as e:
                        debug_monshi(f"[HANDLER ERROR] {phone}: {e}")
#@@@
                client.add_event_handler(handler, events.NewMessage(incoming=True, func=lambda e: e.is_private))
                registered_clients[phone] = handler
                fix_debug(f"[AUTO-REPLY] Handler registered for {phone}")
            else:
                fix_debug(f"[AUTO-REPLY] Handler already registered for {phone}, skipping...")
                
#@@@
            check_interval = 0.5
            while is_auto_reply_enabled_for_account(user_id, phone):
                has_waiters = getattr(lock, "_waiters", []) or []
                debug_clock(f"[AUTO-REPLY] Holding lock for {phone}. Waiters count: {len(has_waiters)}")
# Check if any other coroutine is waiting for the same lock
                if has_waiters:
                    lock_debug(f"[AUTO-REPLY] Detected other functions waiting. Yielding lock for {phone}")
                    break

                # Sleep briefly before checking again to avoid busy waiting
                await asyncio.sleep(check_interval)

        except Exception as e:
            error_debug(f"[AUTO-REPLY EXCEPTION] {phone}: {e}")

        finally:
            try:
                await client.disconnect()
                lock_debug(f"[AUTO-REPLY] Disconnected client for {phone}")
            except Exception as e:
                fix_debug(f"[AUTO-REPLY] Error disconnecting client: {str(e)}")

            if lock.locked():
                try:
                    lock.release()
                    lock_debug(f"[AUTO-REPLY] Lock released for {phone}")
                except RuntimeError as e:
                    fix_debug(f"[AUTO-REPLY] Error releasing lock: {str(e)}")

            await asyncio.sleep(5)






async def monitor_and_disconnect_on_lock_loss(client, lock, phone):
    try:
        while True:
            await asyncio.sleep(2)
            if not lock.locked():
                debug_monshi(f"[AUTO-REPLY] Lock lost for {phone}, disconnecting.")
                try:
                    if client.is_connected():
                        await client.disconnect()
                except Exception as e:
                    debug_monshi(f"[AUTO-REPLY] Error during disconnect for {phone}: {e}")
                break
    except asyncio.CancelledError:
        debug_monshi(f"[AUTO-REPLY] Monitor task cancelled for {phone}")
        try:
            if client.is_connected():
                await client.disconnect()
        except Exception as e:
            debug_monshi(f"[AUTO-REPLY] Disconnect error on cancel for {phone}: {e}")
                       
#@=_>@=_&@=_@=*_@=_*#=_*#_*=÷/<÷/<>#/&*÷</*#/_*#/<*#/<*÷/<>#/<>#/_>$_<(#/<*#/<(#/<>÷/<[÷/<[$/<[$/<[#/<[=/<[÷>/_÷#<<=×#*=_#</#*/_#/<*##/<*#/<*÷$/<>#/<>=>÷$/<>÷$>/<$/<>÷$/<>÷÷$/<>÷$>/$>÷/<&=*#*##^>××:×*#:#&×&@@:@@^@^>#^#]]]]]]))        
        
from telethon.errors import PersistentTimestampOutdatedError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import PeerChannel     
from telethon.errors import PersistentTimestampOutdatedError
from telethon.tl.functions.updates import GetStateRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import asyncio
from telethon.errors import FloodWaitError, PersistentTimestampOutdatedError
from telethon.tl.types import PeerChannel
from telethon.tl.functions.updates import GetStateRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

                
        
async def ensure_client_synced(client, phone: str):
    from telethon.tl.functions.updates import GetStateRequest
    from telethon.tl.functions.messages import GetDialogsRequest
    from telethon.tl.types import InputPeerEmpty

    try:
        await client(GetStateRequest())
        await client.get_me()
        await client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=1,
            hash=0
        ))
        debug_banner(f"[SYNC] [{phone}] Client state refreshed before sending message")
    except Exception as e:
        debug_banner(f"[SYNC ERROR] [{phone}] Failed during pre-send sync: {e}")        
        
########      SEMAFORE ############
 
import random
import time
from collections import defaultdict
from asyncio import Semaphore

account_semaphores = defaultdict(lambda: Semaphore(10))
send_counters = defaultdict(lambda: {"count": 0, "last_reset": time.time()})

async def run_limited(phone: str, task_func, *args, **kwargs):
    async with account_semaphores[phone]:
        # Check if we've hit the throttle limit BEFORE the next send
        if send_counters[phone]["count"] >= 10:
            delay = random.uniform(1.5, 3.0)
            debug_banner(f"[THROTTLE] [{phone}] Hit 10 sends. Sleeping {delay:.2f}s before continuing...")
            await asyncio.sleep(delay)
            send_counters[phone]["count"] = 0  # reset before resuming

        result = await task_func(*args, **kwargs)
        send_counters[phone]["count"] += 1
        return result
        
        

########      NORMAL JOB  ###########

async def send_banner_to_group(client, group, banner, phone: str):    
    group_id = group.get("id")
    group_link = group.get("link", "UNKNOWN")
    username = group.get("username", None)

    debug_banner(f"[GROUP SEND] [{phone}] Attempting to send to: {group_id} | Link: {group_link}")

    if not group_id:
        debug_banner(f"[SKIP] No group_id provided for [{phone}] — skipping group.")
        return "skipped"

    try:
        await client.send_message(PeerChannel(group_id), banner)
        debug_banner(f"[GROUP SEND SUCCESS] [{phone}] Sent directly to {group_id}")
        return "success"

    except PersistentTimestampOutdatedError:
        debug_banner(f"[SYNC RETRY] [{phone}] PersistentTimestampOutdatedError for group {group_id}. Trying to refresh state once.")
        try:
            from telethon.tl.functions.updates import GetStateRequest
            from telethon.tl.functions.messages import GetDialogsRequest
            from telethon.tl.types import InputPeerEmpty

            await client(GetStateRequest())
            await client.get_me()
            await client(GetDialogsRequest(
                offset_date=None,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=1,
                hash=0
            ))

            await client.send_message(PeerChannel(group_id), banner)
            debug_banner(f"[GROUP SEND SUCCESS AFTER SYNC] [{phone}] Sent to {group_id} after syncing")
            return "success"

        except Exception as retry_error:
            debug_banner(f"[RE-SKIP] [{phone}] Still failing after sync: {retry_error}. Skipping {group_id}.")
            return "skipped"
#@@@
    except FloodWaitError as f:
        debug_banner(f"[FLOOD WAIT] [{phone}] Flood wait of {f.seconds}s for {group_id} — skipping.")
        return "unsuccessful"

    except Exception as e:
        error_str = str(e).lower()
        debug_banner(f"[GROUP SEND FAIL] [{phone}] {group_id} -> {e}")

        if "forbidden" in error_str or "ban" in error_str:
            debug_banner(f"[GROUP BANNED] [{phone}] Access denied for {group_id}")
            return "banned"

        return "unsuccessful"
        


async def send_banner_from_account(phone_info: dict, banner: str, user_id: int) -> tuple:
    phone = phone_info.get("phone")
    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
    client = TelegramClient(session_path, API_ID, API_HASH)

    success_count = 0
    banned_count = 0
    unsuccessful_count = 0

    if not os.path.exists(session_path + ".session"):
        logging.warning(f"[SKIP] Session file not found for {phone}. Skipping.")
        return 0, 0, 0

    try:
        await client.connect()

        if not await client.is_user_authorized():
            logging.warning(f"[UNAUTHORIZED] Account {phone} is not authorized.")
            return 0, 0, 0

        await client.get_me()
        client.session._conn.execute("PRAGMA busy_timeout = 200000")

        #@@@ Safe pre-sync to reduce PersistentTimestampOutdatedError
        try:
            await client(GetStateRequest())
            await client(GetDialogsRequest(
                offset_date=None,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=1,
                hash=0
            ))
            logging.info(f"[SYNC] {phone} state refreshed before sending.")
        except Exception as sync_e:
            logging.warning(f"[SYNC ERROR] Sync step failed for {phone}: {sync_e}")

 #@@@
        for group in phone_info.get("groups", []):
            try:
                result = await send_banner_to_group(client, group, banner, phone)
                if result == "success":
                    success_count += 1
                    await asyncio.sleep(0.5)
                    
                elif result == "banned":
                    banned_count += 1
                else:
                    unsuccessful_count += 1
            except Exception as e:
                logging.warning(f"[EXCEPTION] Failed sending to group: {e}")
                unsuccessful_count += 1

    except Exception as e:
        logging.error(f"[CRITICAL ERROR] Telethon client error for {phone}: {e}")
    finally:
        try:
            await client.disconnect()
        except Exception:
            pass

    return success_count, banned_count, unsuccessful_count


        








#async def send_banner_from_account(phone_info: dict, banner: str, user_id: int) -> tuple:
#    phone = phone_info.get("phone")
#    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
#    client = TelegramClient(session_path, API_ID, API_HASH)

#    success_count = 0
#    banned_count = 0
#    unsuccessful_count = 0

#    if not os.path.exists(session_path + ".session"):
#        debug_banner(f"[SKIP] Session file not found for {phone}. Skipping banner send.")
#        return 0, 0, 0

#    try:
#        await client.connect()

#        if not await client.is_user_authorized():
#            debug_banner(f"Account {phone} is not authorized. Skipping banner send.")
#            return 0, 0, 0

#        await client.get_me()
#        client.session._conn.execute("PRAGMA busy_timeout = 200000")

#        #@@@ Fetch dialogs without triggering full sync
#        dialogs_result = await client(GetDialogsRequest(
#            offset_date=None,
#            offset_id=0,
#            offset_peer=InputPeerEmpty(),
#            limit=1000,
#            hash=0
#        ))

#        dialogs = dialogs_result.dialogs
#        entities = {e.id: e for e in dialogs_result.users + dialogs_result.chats}

#        groups = []

#        for dialog in dialogs:
#            peer = dialog.peer
#            if hasattr(peer, "channel_id"):
#                chat = entities.get(peer.channel_id)
#                if getattr(chat, "megagroup", False):
#                    groups.append({
#                        "id": chat.id,
#                        "link": f"https://t.me/{chat.username}" if getattr(chat, "username", None) else "UNKNOWN",
#                        "username": getattr(chat, "username", None)
#                    })

#        #@@@ Prepare and send banners per group
#        tasks = [
#            asyncio.create_task(send_banner_to_group(client, group, banner, phone))
#            for group in groups
#        ]

#        results = await asyncio.gather(*tasks, return_exceptions=True)
#        for result in results:
#            if isinstance(result, Exception):
#                unsuccessful_count += 1
#            elif result == "success":
#                success_count += 1
#            elif result == "banned":
#                banned_count += 1
#            else:
#                unsuccessful_count += 1

#    except Exception as e:
#        debug_banner(f"Error with Telethon client for phone {phone}: {e}", phone)
#    finally:
#        try:
#            await client.disconnect()
#        except Exception:
#            pass

#    return success_count, banned_count, unsuccessful_count



async def send_banner_for_account(phone_info: dict, user_id: int, context: ContextTypes.DEFAULT_TYPE):
    phone = phone_info.get("phone")
    debug_banner(f"Starting send_banner_for_account for phone: {phone}")

    if not phone:
        logging.warning(f"[SEND BANNER] No phone found in phone_info.")
        debug_banner("[ABORT] No phone found in phone_info.")
        return

    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
    debug_banner(f"Session path resolved: {session_path}")
    lock = get_session_lock(session_path)

    async with lock:
        debug_banner(f"Acquired lock for session: {session_path}")
#@@@
        if not is_subscription_valid(user_id):
            debug_banner(f"User {user_id} does not have a valid subscription.")

            # Turn off banner sending for this account
            phone_info["normal"]["status"] = "off"
            phone_info["normal"]["next_send"] = None
            save_accounts(user_id, get_tapchi_list(user_id))  # Persist the change

            try:
                await context.bot.send_message(
                    chat_id=user_id,
                    text="⛔️ اشتراک شما تمام شد و ارسال پیام برای این اکانت متوقف شد.\nبرای ادامه، لطفاً اشتراک جدید تهیه کنید."
                )
                debug_banner(f"Sent subscription error message and disabled account for user {user_id}.")
            except Exception as e:
                logging.error(f"Could not send subscription error message to {user_id}: {e}")
                debug_banner(f"Failed to send subscription error message: {e}")
            return

        # Now more tolerant like old days
        banners = phone_info.get("normal", {}).get("banners") or []
        if not isinstance(banners, list):
            banners = [banners]  # If somehow banners is a single banner dict

        if not banners:
            debug_banner(f"No banners found for {phone}. Skipping send.")
            return

        banner = banners[0]
        debug_banner(f"Selected banner: {banner}")

        try:
            debug_banner(f"Attempting to send banner for {phone}...")
            success_count, banned_count, unsuccessful_count = await send_banner_from_account(phone_info, banner, user_id)
            debug_banner(f"Banner sent. Success: {success_count}, Banned: {banned_count}, Unsuccessful: {unsuccessful_count}")
        except Exception as e:
            logging.error(f"[SEND BANNER ERROR] Sending banner failed for {phone}: {e}")
            debug_banner(f"[EXCEPTION] Sending banner failed for {phone}: {e}")
            return
#@@@
        total_expected_groups = len(phone_info.get("groups", []))
        corrected_unsuccessful = total_expected_groups - (success_count + banned_count)
        corrected_unsuccessful = max(corrected_unsuccessful, 0)

        timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        summary_text = (
            "✅ عملیات ارسال پیام به پایان رسید.\n"
            f"👍🏻 تعداد گروه‌های موفق: {success_count}\n"
            f"❗️ تعداد گروه‌های ناموفق: {corrected_unsuccessful}\n"
            f"👤 اکانت: {phone_info.get('phone', '(No Phone)')}\n"
            f"📅 تاریخ: {timestamp_str}"
        )

        debug_banner(f"Prepared summary text to send back to user {user_id}")

        try:
            await context.bot.send_message(chat_id=user_id, text=summary_text)
            debug_banner(f"Summary message sent successfully to user {user_id}")
        except Exception as e:
            logging.error(f"Could not send summary message to user {user_id}: {e}")
            debug_banner(f"[EXCEPTION] Failed to send summary message to {user_id}: {e}, phone")

    debug_banner(f"Finished send_banner_for_account for phone: {phone}")

    

########&#*@**@*@&@&@*@&#&#*#*#**#*#*#**#*#:&#^#*×;#*@:#*#:#:#:#&#:#&#;#&#*##&;#*$$&$*÷*#>#&#;#*÷;*##>÷[*÷&÷&÷*÷&÷&÷>÷>÷>÷&÷;#&÷[÷[&÷;÷*÷>÷>÷>]]]        
        
        
#112        





            
#111
async def send_and_check_group(session_path: str, group: dict, user_id: int, chat_id: int, context: ContextTypes.DEFAULT_TYPE, wait_time=3) -> str:
    lock = get_session_lock(session_path)

    async with lock:
        client = TelegramClient(session_path, API_ID, API_HASH)
#12
        await client.connect()

        if not await client.is_user_authorized():
            await client.disconnect()
            return  # Or handle unauthorized session appropriately

        await client.get_me()

        try:
            # 1. Check spambot 3 times
            spambot_ok = await check_spambot_for_account(client, user_id, context)
            if not spambot_ok:
                return "spambot_not_ok"

            # 2. Send “سلام” message
            try:
                sent_msg = await client.send_message(group["id"], "سلام")
                await asyncio.sleep(wait_time)

                # 3. See if the message is still there
                check_msg = await client.get_messages(group["id"], ids=sent_msg.id)
                if check_msg:
                    return "no_forced_join"
                else:
                    return "forced_join_needed"

            except Exception as e:
                error_text = str(e).lower()
                if ("you can't write in this chat" in error_text or
                    "not in the chat" in error_text or
                    "forbidden" in error_text or
                    "permission" in error_text or
                    "restricted" in error_text):
                    return "limited_group"
                else:
                    return "error"

        finally:
            await client.disconnect()
            
async def handle_pv_message_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_subscription_valid(user_id):
        await context.bot.send_message(chat_id=user_id, text="⛔️ شما اشتراکی ندارید")
        return    
    if "awaiting_pv_broadcast" not in context.user_data:
        return  # Not in PV message mode

    text = update.message.text
    user_id = update.effective_user.id

    if "pv_broadcast_messages" not in context.user_data:
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        context.user_data["pv_broadcast_messages"] = []

    messages = context.user_data["pv_broadcast_messages"]

    if len(messages) >= 5:
        await update.message.reply_text("❗️ حداکثر ۵ پیام می‌تونی ثبت کنی.")
        return

    messages.append(text)

    msg_count = len(messages)
    preview = f"پیام {msg_count} شما:\n{text}"

    buttons = []

    if msg_count < 5:
        buttons.append([InlineKeyboardButton("❌️ثبت پیام بعدی❌️", callback_data="gm_add_next_pv")])

    buttons.append([InlineKeyboardButton("✅️همین بسه ارسالش کن✅️", callback_data="gm_send_pv_now")])
    buttons.append([InlineKeyboardButton("↪️بازگشت↩️", callback_data="gm_broadcast_pv")])

    await update.message.reply_text(preview, reply_markup=InlineKeyboardMarkup(buttons))     
#110        
async def process_failed_group(client: TelegramClient, group: dict, account_phone: str, user_id: int, chat_id: int, context: ContextTypes.DEFAULT_TYPE) -> bool:
    result = await send_and_check_group(client, group, user_id, chat_id, context, wait_time=3)
    if result == "spambot_not_ok":
        # Spambot check failed; skip forced join.
        return False
    elif result == "no_forced_join":
        # The "سلام" message is still there; no forced join needed.
        return False
    elif result == "forced_join_needed":
        # Forced join is needed.
        username = extract_group_username(group["link"])
        if not username:
            return False
        try:
            await client(JoinChannelRequest(username))
            return True
        except Exception as e:
            logging.error(f"Forced join failed for group {group.get('link')}: {e}")
            return False
    else:
        return False
                
# Helper function to parse a banner link.
def parse_banner_link(link):
    # Expecting a link format such as "https://t.me/channel/12345"
    try:
        link = link.strip()
        
        # Handle direct t.me links
        if "t.me/" in link or "telegram.me/" in link:
            parts = link.split("/")
        channel = parts[-2]
        message_id = int(parts[-1])
        return channel, message_id
            
        # Handle other formats (might be extended in the future)
        return None, None
    except Exception as e:
        logging.error("Error parsing banner link: " + str(e))
        return None, None
        
def extract_forward_info(message):
    """Extract channel username and message_id from a forwarded message"""
    try:
        if message.forward_from_chat:
            # Get the channel username if available, otherwise use the channel ID as string
            channel = message.forward_from_chat.username or str(message.forward_from_chat.id)
            message_id = message.forward_from_message_id
            return channel, message_id
    except Exception as e:
        logging.error(f"Error extracting forward info: {e}")
        return None, None
        
#110        
#*#>#[÷&÷[@@;&@&@*@&@&@&@&@&@&@&@*×(×,×*![!![×;@>@;@:@##^<#>#@*×,&×>××;××&>×&×>×;×>××;>××&×[×[[×[×[×[×[××[×[×[×[×[×[×[×]]]]]]]]]]]]]]]])]


########   FORWARD JOB ############

async def send_forward_to_group(client, group, channel, message_id, phone: str):
    group_id = group.get("id")
    group_link = group.get("link", "UNKNOWN")
    username = group.get("username", None)

    debug_banner(f"[FORWARD GROUP] [{phone}] Attempting to forward to: {group_id} | Link: {group_link}")

    if not group_id:
        debug_banner(f"[SKIP] No group_id provided for [{phone}] — skipping group.")
        return "skipped"

    try:
        banner_entity = await client.get_entity(channel)
        await client.forward_messages(PeerChannel(group_id), [message_id], banner_entity)
        debug_banner(f"[FORWARD SUCCESS] [{phone}] Forwarded directly to {group_id}")
        return "success"

    except PersistentTimestampOutdatedError:
        debug_banner(f"[SYNC RETRY] [{phone}] PersistentTimestampOutdatedError for group {group_id}. Trying to refresh state once.")
        try:
            from telethon.tl.functions.updates import GetStateRequest
            from telethon.tl.functions.messages import GetDialogsRequest
            from telethon.tl.types import InputPeerEmpty

            await client(GetStateRequest())
            await client.get_me()
            await client(GetDialogsRequest(
                offset_date=None,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=1,
                hash=0
            ))

            banner_entity = await client.get_entity(channel)
            await client.forward_messages(PeerChannel(group_id), [message_id], banner_entity)
            debug_banner(f"[FORWARD SUCCESS AFTER SYNC] [{phone}] Forwarded to {group_id} after syncing")
            return "success"

        except Exception as retry_error:
            debug_banner(f"[RE-SKIP] [{phone}] Still failing after sync: {retry_error}. Skipping {group_id}.")
            return "skipped"

    except FloodWaitError as f:
        debug_banner(f"[FLOOD WAIT] [{phone}] Flood wait of {f.seconds}s for {group_id} — skipping.")
        return "unsuccessful"

    except Exception as e:
        error_str = str(e).lower()
        debug_banner(f"[FORWARD FAIL] [{phone}] {group_id} -> {e}")

        if "forbidden" in error_str or "ban" in error_str:
            debug_banner(f"[GROUP BANNED] [{phone}] Access denied for {group_id}")
            return "banned"

        return "unsuccessful"






######## SEND LINK TO ABOVE #######

async def send_forward_from_account(phone_info: dict, banner: str, user_id: int) -> tuple:
    phone = phone_info.get("phone")
    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
    client = TelegramClient(session_path, API_ID, API_HASH)

    success_count = 0
    banned_count = 0
    unsuccessful_count = 0

    if not os.path.exists(session_path + ".session"):
        debug_banner(f"[SKIP] Session file not found for {phone}. Skipping.")
        return 0, 0, 0

    # Parse forward banner link
    channel, message_id = parse_banner_link(banner)
    
    # Handle channel IDs that might be in the banner text (from forwarded messages)
    if not channel or not message_id:
        # Try to extract channel ID and message ID directly if it's in a special format
        # For example: "فوروارد از کانال با شناسه -1001234567890 و پیام 123"
        try:
            if "شناسه" in banner and "پیام" in banner:
                parts = banner.split("شناسه")[1].split("و پیام")
                if len(parts) == 2:
                    channel_id = parts[0].strip()
                    message_id = int(parts[1].strip())
                    channel = channel_id
        except Exception as e:
            logging.error(f"Error parsing special banner format: {e}")
    
    if not channel or not message_id:
        debug_banner(f"[INVALID LINK] Invalid forward banner: {banner}")
        return 0, 0, 0

    try:
        await client.connect()

        if not await client.is_user_authorized():
            debug_banner(f"[UNAUTHORIZED] Account {phone} is not authorized.")
            return 0, 0, 0

        await client.get_me()
        client.session._conn.execute("PRAGMA busy_timeout = 200000")

        try:
            await client(GetStateRequest())
            await client(GetDialogsRequest(
                offset_date=None,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=1,
                hash=0
            ))
            debug_banner(f"[SYNC] {phone} state refreshed before sending.")
        except Exception as sync_e:
            debug_banner(f"[SYNC ERROR] Sync step failed for {phone}: {sync_e}")
#@@@
        for group in phone_info.get("groups", []):
            try:
                result = await send_forward_to_group(client, group, channel, message_id, phone)
                if result == "success":
                    success_count += 1
                    await asyncio.sleep(0.5)  # Delay after success
                elif result == "banned":
                    banned_count += 1
                else:
                    unsuccessful_count += 1
            except Exception:
                unsuccessful_count += 1

    except Exception as e:
        debug_banner(f"[CRITICAL ERROR] Telethon client error for {phone}: {e}")
    finally:
        try:
            await client.disconnect()
        except Exception:
            pass

    return success_count, banned_count, unsuccessful_count
    
########    REPORT FORWARD  ########    
async def send_forward_for_account(phone_info: dict, user_id: int, context: ContextTypes.DEFAULT_TYPE):
    phone = phone_info.get("phone")
    debug_banner(f"Starting send_forward_for_account for phone: {phone}")

    if not phone:
        logging.warning(f"[SEND FORWARD] No phone found in phone_info.")
        debug_banner("[ABORT] No phone found in phone_info.")
        return

    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
    debug_banner(f"Session path resolved: {session_path}")
    lock = get_session_lock(session_path)

    async with lock:
        debug_banner(f"Acquired lock for session: {session_path}")
#@@@
        if not is_subscription_valid(user_id):
            debug_banner(f"User {user_id} does not have a valid subscription.")

            # Turn off forward sending for this account
            phone_info["forward"]["status"] = "off"
            phone_info["forward"]["next_send"] = None
            save_accounts(user_id, get_tapchi_list(user_id))  # Persist the change

            try:
                await context.bot.send_message(
                    chat_id=user_id,
                    text="⛔️ اشتراک شما تمام شد و ارسال پیام برای این اکانت متوقف شد.\nبرای ادامه، لطفاً اشتراک جدید تهیه کنید."
                )
                debug_banner(f"Sent subscription error message and disabled forward for user {user_id}.")
            except Exception as e:
                logging.error(f"Could not send subscription error message to {user_id}: {e}")
                debug_banner(f"Failed to send subscription error message: {e}")
            return

        banner = phone_info.get("forward", {}).get("banner")
        if not banner:
            debug_banner(f"No forward banner found for {phone}. Skipping send.")
            return

        debug_banner(f"Selected forward banner: {banner}")

        try:
            debug_banner(f"Attempting to forward message for {phone}...")
            success_count, banned_count, unsuccessful_count = await send_forward_from_account(phone_info, banner, user_id)
            debug_banner(f"Forward complete. Success: {success_count}, Banned: {banned_count}, Unsuccessful: {unsuccessful_count}")
        except Exception as e:
            logging.error(f"[SEND FORWARD ERROR] Forward failed for {phone}: {e}")
            debug_banner(f"[EXCEPTION] Forward failed for {phone}: {e}")
            return

        total_expected_groups = len(phone_info.get("groups", []))
        corrected_unsuccessful = max(total_expected_groups - (success_count + banned_count), 0)

        timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        summary_text = (
            "✅ عملیات ارسال پیام به پایان رسید.\n"
            f"👍🏻 تعداد گروه‌های موفق: {success_count}\n"
            f"❗️ تعداد گروه‌های ناموفق: {corrected_unsuccessful}\n"
            f"👤 اکانت: {phone_info.get('phone', '(No Phone)')}\n"
            f"📅 تاریخ: {timestamp_str}"
        )

        debug_banner(f"Prepared summary text to send back to user {user_id}")

        try:
            await context.bot.send_message(chat_id=user_id, text=summary_text)
            debug_banner(f"Summary message sent successfully to user {user_id}")
        except Exception as e:
            logging.error(f"Could not send summary message to user {user_id}: {e}")
            debug_banner(f"[EXCEPTION] Failed to send summary message to {user_id}: {e}, phone")

    debug_banner(f"Finished send_forward_for_account for phone: {phone}")
        
    
    
########    SCHEDULE FORWARD  ###### 

async def schedule_send_forward_banner(phone_info, user_id, context):
    async def forward_banner_task():
        await send_forward_for_account(phone_info, user_id, context)
    await task_queue.put(forward_banner_task)
    
    
########      SENDING JOB  ###########
   
async def sending_job(context: ContextTypes.DEFAULT_TYPE):
    tehran = pytz.timezone("Asia/Tehran")
    now = datetime.now(tehran)
    for user_id_str, accounts in tapchi_accounts.items():
        user_id = int(user_id_str)
        for acc in accounts:
            # Normal message job (existing functionality)
            normal = acc.get("normal", {})
            if normal.get("status") == "on" and normal.get("banners"):
                interval = normal.get("interval")
# If interval is not set, skip this account.
                if interval is None:
                    logging.warning(f"Interval is not set for account {acc.get('phone')}; skipping banner send for this account.")
                    continue
                next_send = normal.get("next_send")
#e                
                if next_send:
                    try:
                        next_dt = datetime.fromisoformat(next_send)
                        if next_dt.tzinfo is None:
                            next_dt = tehran.localize(next_dt)
                        else:
                            next_dt = next_dt.astimezone(tehran)
                    except Exception as e:
                        logging.error(f"Invalid next_send format for account {acc.get('phone')}: {next_send}")
#@@
                        next_dt = now
                    if now >= next_dt:
                        debug_banner(f"Scheduling normal banner send for {acc.get('phone')} (time matched)")
                        normal["next_send"] = (now + timedelta(minutes=interval)).isoformat()
                        await schedule_send_banner(acc, user_id, context)
                    else:
                        debug_banner(f"Skipping normal banner send for {acc.get('phone')} (not time yet)")
                else:
                    debug_banner(f"First time scheduling normal banner send for {acc.get('phone')}")
                    normal["next_send"] = (now + timedelta(minutes=interval)).isoformat()
                    await schedule_send_banner(acc, user_id, context)
                    
            # Forward message job:
            forward = acc.get("forward", {})
            if forward.get("status") == "on" and forward.get("banner"):
                interval = forward.get("interval")
                if interval is None:
                    logging.warning(f"Forward interval not set for account {acc.get('phone')}; skipping forward banner send for this account.")
                    continue
                next_send = forward.get("next_send")
#d                
                if next_send:
                    try:
                        next_dt = datetime.fromisoformat(next_send)
                        if next_dt.tzinfo is None:
                            next_dt = tehran.localize(next_dt)
                        else:
                            next_dt = next_dt.astimezone(tehran)
                    except Exception as e:
                        logging.error(f"Invalid forward next_send format for account {acc.get('phone')}: {next_send}")
                        next_dt = now
                    if now >= next_dt:
                        debug_banner(f"Scheduling forward banner send for {acc.get('phone')} (time matched)")
                        forward["next_send"] = (now + timedelta(minutes=interval)).isoformat()
                        await schedule_send_forward_banner(acc, user_id, context)
                    else:
                        debug_banner(f"Skipping forward banner send for {acc.get('phone')} (not time yet)")
                else:
                    debug_banner(f"First time scheduling forward banner send for {acc.get('phone')}")
                    forward["next_send"] = (now + timedelta(minutes=interval)).isoformat()
                    await schedule_send_forward_banner(acc, user_id, context)
    save_accounts(user_id, accounts)    
  


# ---------------------------
# INLINE CALLBACK HANDLER
# ---------------------------
# New function: calculate upgrade price
#c
def calculate_upgrade_price(current_sub, new_plan_price, total_days=30):
    tehran = pytz.timezone("Asia/Tehran")
    now = datetime.now(tehran)
    expiry = datetime.fromisoformat(current_sub["expiry"])
    if expiry.tzinfo is None:
        expiry = tehran.localize(expiry)
    else:
        expiry = expiry.astimezone(tehran)

    # Calculate complete remaining days (ignoring any fractional day)
    remaining_days = int((expiry - now).total_seconds() / 86400)

    # Use the "price" key if present; if not, default to 0.
    current_price = current_sub.get("price", 0)
    daily_cost = current_price / total_days if total_days else 0
    unused_value = remaining_days * daily_cost
    final_price = new_plan_price - unused_value
    if final_price < 0:
        final_price = 0
    return final_price, remaining_days, unused_value
#109    
async def broadcast_pv_messages(update: Update, context: ContextTypes.DEFAULT_TYPE, messages):
    user_id = update.effective_user.id
    accounts = get_tapchi_list(user_id)

    if not accounts:
        await context.bot.send_message(user_id, "هیچ اکانتی برای شما ثبت نشده.")
        return

    for acc in accounts:
        phone = acc["phone"]
        session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
        client = TelegramClient(session_path, API_ID, API_HASH)
        lock = get_session_lock(session_path)

        async with lock:
            debug_pv(f"[{phone}] Starting PV broadcast with session path: {session_path}")
            if await safe_connect(client, acc, user_id, context):
                try:
                    dialogs = await client.get_dialogs()
                    for d in dialogs:
                        if d.is_user and not getattr(d.entity, "bot", False):
                            for msg in messages:
                                try:
                                    await client.send_message(d.entity.id, msg)
                                    debug_pv(f"[{phone}] Sent message to {d.name}")
                                except Exception as e:
                                    logging.warning(f"[PV SEND FAIL] {phone} to {d.name}: {e}")
                                await asyncio.sleep(1.5)
                except Exception as e:
                    logging.warning(f"[PV DIALOGS FAIL] {phone}: {e}")
                    debug_pv(f"[{phone}] PV DIALOG FAIL: {e}")
                finally:
                    await client.disconnect()

    await context.bot.send_message(user_id, "✅ پیام‌ها به پیوی مخاطبان ارسال شد.")
        
async def inline_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if this is an admin panel callback
    if update.callback_query.data.startswith("admin_"):
        await admin_button_handler(update, context)
        return
    query = update.callback_query
    user_id = query.from_user.id  # Extract user_id before using it
    data = query.data.strip()
    logging.debug(f"Received callback data: {data} from user: {user_id}")

    # ==================== TICKET SYSTEM CALLBACKS ====================
    
    # Support menu
    if data == "support_menu":
        await show_support_menu(query, context)
        return
    
    # Create ticket
    elif data == "create_ticket":
        context.user_data["awaiting_ticket_message"] = True
        await query.edit_message_text(
            "🎫 <b>ایجاد تیکت جدید</b>\n\n"
            "💬 لطفاً متن مشکل، سؤال یا درخواست خود را بنویسید:\n\n"
            "💡 <b>نکته:</b> هرچه جزئیات بیشتری بنویسید، بهتر می‌توانیم کمکتان کنیم.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data="support_menu")]]),
            parse_mode="HTML"
        )
        return
    
    # View user tickets
    elif data == "view_my_tickets":
        await show_user_tickets(query, context)
        return
    
    # View specific ticket
    elif data.startswith("view_ticket_"):
        ticket_id = data.replace("view_ticket_", "")
        await show_ticket_details(query, context, ticket_id)
        return
    
    # Reply to ticket
    elif data.startswith("reply_ticket_"):
        ticket_id = data.replace("reply_ticket_", "")
        context.user_data["awaiting_ticket_reply"] = True
        context.user_data["current_ticket_id"] = ticket_id
        await query.edit_message_text(
            f"💬 <b>پاسخ به تیکت #{ticket_id}</b>\n\n"
            "✍️ لطفاً پاسخ خود را بنویسید:",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data=f"view_ticket_{ticket_id}")]]),
            parse_mode="HTML"
        )
        return
    
    # Close ticket (admin only)
    elif data.startswith("close_ticket_"):
        if user_id == ADMIN_ID:
            ticket_id = data.replace("close_ticket_", "")
            if close_ticket(ticket_id):
                await query.edit_message_text(
                    f"✅ <b>تیکت #{ticket_id} با موفقیت بسته شد</b>\n\n"
                    "📧 کاربر از بسته شدن تیکت مطلع خواهد شد.",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت به پنل", callback_data="admin_tickets")]]),
                    parse_mode="HTML"
                )
                
                # Notify user that ticket is closed
                ticket = get_ticket_by_id(ticket_id)
                if ticket:
                    try:
                        await context.bot.send_message(
                            chat_id=ticket["user_id"],
                            text=f"🔒 <b>تیکت #{ticket_id} بسته شد</b>\n\n"
                                 "✅ مشکل شما حل شده و تیکت بسته شد.\n"
                                 "💬 اگر مشکل جدیدی دارید، تیکت جدید بسازید.",
                            parse_mode="HTML"
                        )
                    except Exception as e:
                        logging.error(f"Error notifying user about closed ticket: {e}")
            else:
                await query.answer("❌ خطا در بستن تیکت", show_alert=True)
        else:
            await query.answer("❌ فقط ادمین می‌تواند تیکت را ببندد", show_alert=True)
        return
    
    # Back to start menu
    elif data == "start_menu":
        await start(update, context)
        return

    # …your if/elif chain here…

    if data == "tapchi_menu":
        await show_tapchi_menu(update.callback_query, context)
        return

    elif data == "start_processing_photos":
        photos = context.user_data.get("profile_photos", [])
        if not photos:
            await query.edit_message_text("⛔️ هیچ عکسی برای ارسال وجود ندارد.")
            return

        await query.edit_message_text(f"✅ دریافت شد. در حال ارسال {len(photos)} عکس...")

        # Distribute photos
        try:
            await distribute_photos_to_accounts(user_id, photos, context)
            await query.message.reply_text("ارسال عکس‌ها با موفقیت انجام شد ✅")
        except Exception as e:
            logging.error(f"Error during photo distribution: {e}")
            await query.message.reply_text("❌ خطا هنگام ارسال عکس‌ها")

        # Clean up ALL photo-related flags
        context.user_data.pop("profile_photos", None)
        context.user_data.pop("awaiting_multi_photos", None)
        context.user_data.pop("gm_edit_photo", None)
        context.user_data.pop("awaiting_photo", None)

    elif data == "cancel_photo_upload":
        for f in context.user_data.get("profile_photos", []):
            try:
                os.remove(f)
            except Exception as e:
                logging.warning(f"Error deleting photo file: {f} - {e}")
        # Clear ALL photo-related flags to ensure we're completely out of photo mode
        context.user_data.pop("profile_photos", None)
        context.user_data.pop("awaiting_multi_photos", None)
        context.user_data.pop("gm_edit_photo", None)
        context.user_data.pop("awaiting_photo", None)
        await query.edit_message_text("⛔️ همه چیز لغو شد. عکس‌ها حذف شدند.")


# --- Global Timebound Panel ---
    if data == "gm_timebound":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        

        # Track that user is in main timebound panel
        context.user_data["gm_mode"] = "timebound"
        context.user_data.pop("inside_timebound", None)  # We're NOT inside a sub-option yet

        await general_timebound_panel(update.callback_query, context)
        return

        context.user_data["gm_mode"] = "timebound"
        await general_timebound_panel(update.callback_query, context)
        return

# --- Global Forward Panel ---
    elif data == "gm_forward":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        

        context.user_data["gm_mode"] = "forward"
        await general_forward_panel(update.callback_query, context)
        return
#linkdoni
# --- Linkdoni Entry Point ---
    elif data == "linkdoni_find_groups":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return

        context.user_data["linkdoni_state"] = "awaiting_link"
#@@@        
        await query.message.edit_text(
            "اطلاعات:\n"
            "اینجا میتونید لینک ی لینکدونی رو به ربات بدید و ربات میره و گروه های داخل لینکدونی رو براتون به عنوان فایل ارسال میکنه.\n\n"
            "مهم: بدونید که ۹۹ درصد گروه‌های توی لینکدونی‌ها خصوصی هستن و بدرد تبلیغات نمیخورن فقط کسایی که بلدن چطوری با این گروه ها تبلیغ انجام بدن اکانت هاشون رو عضو این گروه ها کنن.\n\n"
            "چند نمونه لینکدونی:\n"
            "🟣 https://t.me/linkd\n"
            "🟣 https://t.me/linkdoni\n"
            "🟣 https://t.me/Link4you\n"
            "🟣 https://t.me/linkdoni_sib\n"
            "🟣 https://t.me/linkdonilt1\n"
            "🟣 https://t.me/linkdoniwar2\n"
            "🟣 https://t.me/linkdoni_almaas\n",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("♻️ شروع استخراج لینک از لینکدونی ♻️", callback_data="start_extract_linkdoni")],
                [InlineKeyboardButton("↩️بازگشت↩️", callback_data="gm_back")]
            ]),
            disable_web_page_preview=True
        )
        return

# --- Linkdoni Prompt for URL ---
    elif data == "start_extract_linkdoni":
        context.user_data["linkdoni_state"] = "awaiting_link_input"
        await query.message.edit_text(
            "لطفا لینک لینکدونی که میخواید ازش گروه هارو استخراج کنم رو وارد کنید:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌️لغو❌️", callback_data="cancel_linkdoni")]
            ])
        )
        return
# --- Account Stats Button ---
    elif data == "accounts_state":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        await accounts_state_handler(update, context)
        return
# --- Cancel Linkdoni Flow ---
    elif data == "cancel_linkdoni":
        context.user_data.pop("linkdoni_state", None)
        context.user_data.pop("linkdoni_link", None)
        await query.message.edit_text("فرایند استخراج لغو شد.")
        return        
        
# ✅ Universal back handler: ONLY return to کنترل همگانی
    elif data == "gm_back":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        

        clear_user_flags(context)  # ✅ Clean state before going back
        await show_general_management_panel(update.callback_query, context)
        return
# --- Delete All Groups & Channels Panel ---
    elif data == "gm_delete_all_groups":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        query = update.callback_query
        text = (
            "ℹ️ اطلاع:\n\n"
            "اینجا می‌تونی همه گروه‌ها یا کانال‌هایی که اکانت‌هات توش عضو هستن رو با یک کلیک حذف کنی.\n\n"
            "با زدن دکمه‌ها پایین، مشخص کن که می‌خوای:\n"
            "• ❌ فقط گروه‌ها پاک بشن\n"
            "• ❌ فقط کانال‌ها پاک بشن\n"
            "• ❌ یا هر دو با هم پاک بشن\n\n"
            "‼️ دقت کن: این کار قابل برگشت نیست."
        )

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("❌ حذف فقط گروه‌ها ❌", callback_data="gm_delete_only_groups")],
            [InlineKeyboardButton("❌ حذف فقط کانال‌ها ❌", callback_data="gm_delete_only_channels")],
            [InlineKeyboardButton("❌ حذف گروه‌ها و کانال‌ها ❌", callback_data="gm_delete_all_entities")],
            [InlineKeyboardButton("↪️بازگشت↩️", callback_data="gm_back")]
        ])

        await query.message.edit_text(text, reply_markup=keyboard)

    # --- Confirm Delete Only Groups ---
    elif data == "gm_delete_only_groups":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        query = update.callback_query
        await query.message.edit_text(
            "❗️ مطمئنی که می‌خوای همه گروه‌ها از اکانت‌هات حذف بشن؟\nاین کار برگشت‌پذیر نیست.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ بله، حذف کن ✅", callback_data="gm_confirm_delete_groups")],
                [InlineKeyboardButton("↪️بازگشت↩️", callback_data="gm_delete_all_groups")]
            ])
        )

    # --- Confirm Delete Only Channels ---
    elif data == "gm_delete_only_channels":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        query = update.callback_query
        await query.message.edit_text(
            "❗️ مطمئنی که می‌خوای همه کانال‌ها از اکانت‌هات حذف بشن؟\nاین کار برگشت‌پذیر نیست.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ بله، حذف کن ✅", callback_data="gm_confirm_delete_channels")],
                [InlineKeyboardButton("↪️بازگشت↩️", callback_data="gm_delete_all_groups")]
            ])
        )

# --- Confirm Delete Groups & Channels ---
    elif data == "gm_delete_all_entities":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        query = update.callback_query
        await query.message.edit_text(
            "❗️ مطمئنی که می‌خوای همه گروه‌ها و کانال‌ها از اکانت‌هات حذف بشن؟\nاین کار برگشت‌پذیر نیست.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ بله، حذف کن ✅", callback_data="gm_confirm_delete_all")],
                [InlineKeyboardButton("↪️بازگشت↩️", callback_data="gm_delete_all_groups")]
            ])
        )
#108
# --- Execute Deletion: Only Groups ---
    elif data == "gm_confirm_delete_groups":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return

        query = update.callback_query
        await query.message.edit_text("⏳ در حال حذف گروه‌ها... لطفاً صبر کن.")
        user_id = query.from_user.id
        report_lines = []

        accounts = get_tapchi_list(user_id)
        for acc in accounts:
            phone = acc['phone']
            session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")  # FIXED
            client = TelegramClient(session_path, API_ID, API_HASH)
            lock = get_session_lock(session_path)

            async with lock:
                if await safe_connect(client, acc, user_id, context):
                    try:
                        deleted = 0
                        dialogs = await client.get_dialogs()
                        for d in dialogs:
                            if d.is_group:
                                await client(LeaveChannelRequest(d.entity))
                                deleted += 1
                        report_lines.append(f"{phone}: {deleted} گروه حذف شد")
                    except Exception as e:
                        report_lines.append(f"{phone}: خطا در حذف ({e})")
                    finally:
                        await client.disconnect()

        await query.message.edit_text("✅ عملیات حذف گروه‌ها انجام شد:\n\n" + "\n".join(report_lines))


# --- Execute Deletion: Only Channels ---
    elif data == "gm_confirm_delete_channels":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return

        query = update.callback_query
        await query.message.edit_text("⏳ در حال حذف کانال‌ها... لطفاً صبر کن.")
        user_id = query.from_user.id
        report_lines = []

        accounts = get_tapchi_list(user_id)
        for acc in accounts:
            phone = acc['phone']
            session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")  # FIXED
            client = TelegramClient(session_path, API_ID, API_HASH)
            lock = get_session_lock(session_path)

            async with lock:
                if await safe_connect(client, acc, user_id, context):
                    try:
                        deleted = 0
                        dialogs = await client.get_dialogs()
                        for d in dialogs:
                            if d.is_channel and not d.is_group:
                                await client(LeaveChannelRequest(d.entity))
                                deleted += 1
                        report_lines.append(f"{phone}: {deleted} کانال حذف شد")
                    except Exception as e:
                        report_lines.append(f"{phone}: خطا در حذف ({e})")
                    finally:
                        await client.disconnect()

        await query.message.edit_text("✅ عملیات حذف کانال‌ها انجام شد:\n\n" + "\n".join(report_lines))
        
#106
# --- Execute Deletion: Groups & Channels ---
    elif data == "gm_confirm_delete_all":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return

        query = update.callback_query
        await query.message.edit_text("⏳ در حال حذف گروه‌ها و کانال‌ها... لطفاً صبر کن.")
        user_id = query.from_user.id
        report_lines = []

        accounts = get_tapchi_list(user_id)
        for acc in accounts:
            phone = acc['phone']
            session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")  # FIXED
            client = TelegramClient(session_path, API_ID, API_HASH)
            lock = get_session_lock(session_path)

            async with lock:
                if await safe_connect(client, acc, user_id, context):
                    try:
                        deleted = 0
                        dialogs = await client.get_dialogs()
                        for d in dialogs:
                            if d.is_group or (d.is_channel and not d.is_group):
                                await client(LeaveChannelRequest(d.entity))
                                deleted += 1
                        report_lines.append(f"{phone}: {deleted} مورد حذف شد")

                    except Exception as e:
                        report_lines.append(f"{phone}: خطا در حذف ({e})")
                    finally:
                        await client.disconnect()

        await query.message.edit_text("✅ عملیات حذف انجام شد:\n\n" + "\n".join(report_lines))
        

# --- Global Broadcast to PV Panel ---
    elif data == "gm_broadcast_pv":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        query = update.callback_query
        context.user_data["awaiting_pv_message"] = False
        context.user_data["pv_message_stage"] = 0
        context.user_data["pv_broadcast_messages"] = []

        text = (
            "ℹ️ اطلاع:\n\n"
            "در این بخش می‌تونی یک یا چند پیام بنویسی که به صورت خودکار برای تمام کسانی که به پیوی اکانت‌هات پیام دادن ارسال بشه.\n\n"
            "مثلاً می‌تونی پیام تبلیغاتی، اطلاع‌رسانی یا معرفی خدماتت رو بهشون بفرستی.\n\n"
            "با زدن دکمه زیر می‌تونی پیام اولت رو ثبت کنی."
        )

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("✅️ثبت پیام✅️", callback_data="gm_broadcast_register_1")],
            [InlineKeyboardButton("↪️بازگشت↩️", callback_data="gm_back")]
        ])

        await query.message.edit_text(text, reply_markup=keyboard)

# --- Cancel PV Broadcast ---
    elif data == "gm_broadcast_cancel":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        query = update.callback_query
        context.user_data["awaiting_pv_broadcast"] = False  # FIXED key
        context.user_data["pv_broadcast_messages"] = []
        await query.message.edit_text(
            "❌ ارسال پیام همگانی لغو شد.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("↪️بازگشت↩️", callback_data="gm_broadcast_pv")]
            ])
        )

# --- Register First PV Message ---
    elif data == "gm_broadcast_register_1":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        query = update.callback_query
        context.user_data["awaiting_pv_broadcast"] = True  # FIXED key
        context.user_data["pv_message_stage"] = 1
        context.user_data["pv_broadcast_messages"] = []

        await query.message.edit_text(
            "لطفاً پیام اول خود را وارد کنید:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌️لغو❌️", callback_data="gm_broadcast_cancel")]
            ])
        )

# --- Next Message Step after user input ---
    elif data == "gm_broadcast_next":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        stage = context.user_data.get("pv_message_stage", 1) + 1
        context.user_data["pv_message_stage"] = stage

        if stage > 5:
            await update.callback_query.message.edit_text("❗️حداکثر ۵ پیام قابل ثبت است.")
            return

        await update.callback_query.message.edit_text(
            f"لطفاً پیام {stage} را وارد کنید:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌️لغو❌️", callback_data="gm_broadcast_cancel")]
            ])
        )
#105
# --- Confirm and Send Messages ---
    elif data == "gm_broadcast_confirm":
        debug_pv("Triggered: gm_broadcast_confirm")

        if not is_subscription_valid(user_id):
            debug_pv("User has no subscription")
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return

        query = update.callback_query
        user_id = query.from_user.id
        messages = context.user_data.get("pv_broadcast_messages", [])

        debug_pv(f"Messages to send: {len(messages)}")

        if not messages:
            debug_pv("No messages found in context")
            await query.message.edit_text("هیچ پیامی برای ارسال ثبت نشده است.")
            return

        await query.message.edit_text("⏳ در حال ارسال پیام‌ها به PV ها...")

        accounts = get_tapchi_list(user_id)
        report_lines = []

        for acc in accounts:
            phone = acc["phone"]
            session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
            lock = get_session_lock(session_path)
            client = TelegramClient(session_path, API_ID, API_HASH)

            async with lock:
                debug_pv(f"[{phone}] Lock acquired. Connecting...")
#14
                try:
                    await client.connect()

                    if not await client.is_user_authorized():
                        debug_pv(f"[{phone}] Unauthorized session.")
                        report_lines.append(f"{phone}: نیاز به ورود مجدد.")
                        await client.disconnect()
                        continue

                    await client.get_me()
                    debug_pv(f"[{phone}] Client.connect done.")

                    debug_pv(f"[{phone}] Connected and authorized. Sending messages...")
                    count = 0

                    async for dialog in client.iter_dialogs():
                        if dialog.is_user:
                            debug_pv(f"[{phone}] Found user: {dialog.name}")
                            for msg in messages:
                                try:
                                    await client.send_message(dialog.entity.id, msg)
                                    debug_pv(f"[{phone}] Sent message to {dialog.name}")
                                except Exception as e:
                                    debug_pv(f"[{phone}] Failed sending to {dialog.name}: {e}")
                                await asyncio.sleep(1.5)
                            count += 1

                    report_lines.append(f"{phone}: {count} نفر")

                except Exception as e:
                    debug_pv(f"[{phone}] PV DIALOGS FAIL: {e}")
                    report_lines.append(f"{phone}: خطا ({str(e)})")

                finally:
                    try:
                        await client.disconnect()
                        debug_pv(f"[{phone}] Disconnected.")
                    except:
                        debug_pv(f"[{phone}] Failed to disconnect")

        context.user_data["awaiting_pv_message"] = False
        context.user_data["pv_message_stage"] = 0
        context.user_data["pv_broadcast_messages"] = []

        await query.message.edit_text("✅ پیام‌ها ارسال شدند:\n\n" + "\n".join(report_lines))
        debug_pv("Broadcast complete.")
        
                                                                                              # --- Add Next PV Message ---
    elif data == "gm_add_next_pv":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        query = update.callback_query
        context.user_data["awaiting_pv_broadcast"] = True
        await query.message.edit_text(
            f"لطفاً پیام {len(context.user_data.get('pv_broadcast_messages', [])) + 1} خود را وارد کنید:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌️لغو❌️", callback_data="gm_broadcast_cancel")]
            ])
        )

    # --- Send PV Messages Now ---
    elif data == "gm_send_pv_now":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        query = update.callback_query
        context.user_data["awaiting_pv_broadcast"] = False

        messages = context.user_data.get("pv_broadcast_messages", [])
        if not messages:
            await query.message.edit_text("هیچ پیامی ثبت نشده.")
            return

        await query.message.edit_text("⏳ در حال ارسال پیام‌ها... لطفاً صبر کن.")
        await broadcast_pv_messages(update, context, messages)                                             
    # --- Global Forward Set Banner ---
    elif data == "gm_set_forward_banner":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        context.user_data["gm_set_banner_forward"] = True
        await update.callback_query.message.edit_text(
            "لطفا لینک بنر خود را ارسال کنید:\n"
            "اطلاع داشته باشید که وقتی بنر جدید ثبت کنید بنر قبلی فوروارد شما حذف میشه.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("↪️بازگشت↩️", callback_data="gm_forward_back")]
            ])
        )
        return

    # --- Global Forward Back Button ---
    elif data == "gm_forward_back":
        context.user_data.pop("gm_set_banner_forward", None)
        await general_forward_panel(update.callback_query, context)
        return

# --- Global Forward Set Time ---
    elif data == "gm_forward_set_time":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        await general_set_time(update.callback_query, context, mode="forward")
        return

    elif data.startswith("gm_forward_set_time:"):
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        try:
            interval = int(data.split(":")[1])
            user_id = update.effective_user.id
            accounts = get_tapchi_list(user_id)
            tehran = pytz.timezone("Asia/Tehran")
            now = datetime.now(tehran)

            set_banner_debug(f"Setting forward interval to {interval} for {len(accounts)} accounts")

            for acc in accounts:
                acc.setdefault("forward", {})["interval"] = interval
                acc["forward"]["next_send"] = (now + timedelta(minutes=interval)).isoformat()
                set_banner_debug(f"Interval and next_send set for {acc['phone']}")

            save_accounts(user_id, accounts)
            set_banner_debug("Accounts saved with updated interval and next_send.")

            await update.callback_query.answer(f"زمان فوروارد تنظیم شد: {interval} دقیقه ✅", show_alert=True)
            await general_forward_panel(update.callback_query, context)

        except Exception as e:
            set_banner_debug(f"Error setting time: {e}")
            await update.callback_query.answer("خطا در تنظیم زمان", show_alert=True)
        return
# --- Global Forward Toggle Menu ---
    elif data == "gm_forward_toggle":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ روشن کردن تمامی اکانت ها✅", callback_data="gm_forward_toggle_on")],
            [InlineKeyboardButton("❌ خاموش کردن تمامی اکانت ها❌", callback_data="gm_forward_toggle_off")],
            [InlineKeyboardButton("↩️بازگشت↩️", callback_data="gm_forward_back")]
        ])
        await update.callback_query.message.edit_text("گزینه مورد نظر را انتخاب کنید:", reply_markup=keyboard)
        return

    # --- Global Forward Toggle ON ---
    elif data == "gm_forward_toggle_on":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        user_id = update.effective_user.id
        accounts = get_tapchi_list(user_id)
        for acc in accounts:
            acc["forward"]["status"] = "on"
        save_accounts(user_id, accounts)
        await update.callback_query.answer("همه اکانت‌ها روشن شدند ✅", show_alert=True)
        await general_forward_panel(update.callback_query, context)
        return
#photo
    elif data == "gm_edit_photo":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        context.user_data["awaiting_multi_photos"] = True
        context.user_data["profile_photos"] = []  # initialize buffer
        await update.callback_query.message.edit_text(
            "لطفاً تمامی عکس‌هایی که می‌خواهید اکانت‌ها استفاده کنند را باهم ارسال کنید.\n\n"
            "اطلاع: اگر یک اکانت دارید و ۱۰ عکس ارسال کنید، آن ۱۰ عکس به آن اکانت اضافه می‌شوند، و اگر ۵ اکانت دارید و ۱۰ عکس ارسال کنید، به هر اکانت ۲ عکس اضافه می‌شود.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("↪️بازگشت↩️", callback_data="gm_back")]
            ])
        )
        return
        
# ساعت کنار اسم
    elif data == "Clock_on_the_right":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
            
        await update.callback_query.message.edit_text(
            "اطلاعات درباره ساعت کنار اسم:\n"
            "مثلا اگه اسم شما این باشه\n"
            "Mohammed\n"
            "با گذاشتن ساعت کنارش اینطوری میشه:\n"
            "Mohammed 𝟙𝟚:𝟘𝟘\n"
            "این ساعت زمان واقعی هستش و هر دقیقه بالا میره.\n"
            "برای روشن کردن و فعال سازی روی گزینه روشن شدن بزنید.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⏰️تنظیم ساعت کنار اسم⏰️", callback_data="enable_clock")],
                [InlineKeyboardButton("❌️خاموش کردن ساعت کنار اسم❌️", callback_data="disable_clock")],
                [InlineKeyboardButton("↪️بازگشت↩️", callback_data="back_to_panel")]
            ])
        )
        return
        
# فعالسازی ساعت کنار اسم
    elif data == "enable_clock":
        await update.callback_query.message.edit_text(
            "لطفا فونت ساعت خود را انتخاب کنید:",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("𝟏𝟐:𝟑𝟒", callback_data="clockfont_0"),
                    InlineKeyboardButton("𝟙𝟚:𝟛𝟜", callback_data="clockfont_1"),
                    InlineKeyboardButton("𝟸𝟹:𝟺𝟻", callback_data="clockfont_2"),
                ],
                [
                    InlineKeyboardButton("¹²:³⁴", callback_data="clockfont_3"),
                    InlineKeyboardButton("₂₃:₄₅", callback_data="clockfont_4"),
                    InlineKeyboardButton("【𝟏𝟐:𝟑𝟒】", callback_data="clockfont_5"),
                ],
                [
                    InlineKeyboardButton("✧𝟏𝟐:𝟑𝟒✧", callback_data="clockfont_6"),
                    InlineKeyboardButton("《𝟏𝟐:𝟑𝟒》", callback_data="clockfont_7"),
                    InlineKeyboardButton("꧁𝟙𝟚:𝟛𝟜꧂", callback_data="clockfont_8"),
                ],
                [
                    InlineKeyboardButton("꧁¹²:³⁴꧂", callback_data="clockfont_9"),
                    InlineKeyboardButton("✧【𝟏𝟐:𝟑𝟒】✧", callback_data="clockfont_10"),
                    InlineKeyboardButton("✧𝟙𝟚:𝟛𝟜✧", callback_data="clockfont_11"),
                ],
                [
                    InlineKeyboardButton("༺𝟏𝟐:𝟑𝟒༻", callback_data="clockfont_12"),
                    InlineKeyboardButton("[★𝟸𝟹:𝟺𝟻★]", callback_data="clockfont_13"),
                    InlineKeyboardButton("𓆩₂₃:₄₅𓆪", callback_data="clockfont_14"),
                ],
                [
                    InlineKeyboardButton("《¹²:³⁴》", callback_data="clockfont_15"),
                    InlineKeyboardButton("•̩̩͙𝟏𝟐:𝟑𝟒•̩̩͙", callback_data="clockfont_16"),
                    InlineKeyboardButton("【𝟙𝟚:𝟛𝟜】", callback_data="clockfont_17"),
                ],
                [
                    InlineKeyboardButton("①②:③④", callback_data="clockfont_18"),
                    InlineKeyboardButton("➊➋:➌➍", callback_data="clockfont_19"),
                    InlineKeyboardButton("1 2 :3 4", callback_data="clockfont_20"),
                ],      
                [
                    InlineKeyboardButton("❶２:３４", callback_data="clockfont_21"),
                    InlineKeyboardButton("⦅1⦆⦅2⦆:⦅3⦆⦅4⦆", callback_data="clockfont_22"),
                    InlineKeyboardButton("1̶2̶:3̶4̶", callback_data="clockfont_23"),
                ],   
                [
                    InlineKeyboardButton("『1』『2』:『3』『4』", callback_data="clockfont_24"),
                    InlineKeyboardButton("【1】【2】:【3】【4】", callback_data="clockfont_25"),
                    InlineKeyboardButton("❶❷:３❹", callback_data="clockfont_26"),
                ],                                       
                [
                    InlineKeyboardButton("⏳️ انتخاب فونت تصادفی برای تمامی اکانت ها ⏳️", callback_data="randomize_fonts")
                ],
                [
                    InlineKeyboardButton("↩️ بازگشت", callback_data="back_to_panel")
                ]
            ])
        )
        return
        
# خاموش کردن ساعت کنار اسم
    elif data == "disable_clock":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        await update.callback_query.answer()
        await update.callback_query.message.edit_text("⏳️درحال خاموش کردن ساعت کنار اسم...")

        try:
            # Load user accounts
            accounts = get_tapchi_list(user_id)
            for acc in accounts:
                acc["clock_enabled"] = False
                acc["clock_font"] = 0
                phone = acc.get("phone")

                # Update clock_state.json
                state_file = os.path.join("data", "clock_state.json")
                try:
                    with open(state_file, "r", encoding="utf-8") as f:
                        state_data = json.load(f)
                except FileNotFoundError:
                    state_data = {}

                if str(user_id) not in state_data:
                    state_data[str(user_id)] = {}

                state_data[str(user_id)][phone] = {
                    "clock_font": 0,
                    "status": "off"
                }

                with open(state_file, "w", encoding="utf-8") as f:
                    json.dump(state_data, f, indent=2, ensure_ascii=False)

                # Clear last name on Telegram safely
                session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
                lock = get_session_lock(session_path)
                async with lock:
                    client = TelegramClient(session_path, API_ID, API_HASH)
#15
                    await client.connect()

                    if await client.is_user_authorized():
                        await client.get_me()
                        me = await client.get_me()
                        await client(UpdateProfileRequest(first_name=me.first_name or phone, last_name=""))
                    
                    await client.disconnect()

            save_accounts(user_id, accounts)

            await update.callback_query.message.edit_text("ساعت کنار اسم خاموش شد❌️")
        except Exception as e:
            await update.callback_query.message.edit_text(f"خطا در خاموش کردن ساعت: {e}")
        return
                

# انتخاب فونت ساعت
    elif data.startswith("clockfont_"):
        font_index = int(data.split("_")[1])

        CLOCK_FONT_FILE = "read_clock_font_for_user.json"
        CLOCK_STATE_FILE = os.path.join("data", "clock_state.json")
        TAPCHI_ACCOUNTS_FILE = os.path.join("data", "tapchi_accounts.json")

        try:
            # Update font in global clock font file
            try:
                with open(CLOCK_FONT_FILE, "r", encoding="utf-8") as f:
                    font_data = json.load(f)
            except FileNotFoundError:
                font_data = {}

            font_data[str(user_id)] = font_index

            with open(CLOCK_FONT_FILE, "w", encoding="utf-8") as f:
                json.dump(font_data, f)

            # Load or initialize clock_state.json
            try:
                with open(CLOCK_STATE_FILE, "r", encoding="utf-8") as f:
                    clock_state = json.load(f)
            except FileNotFoundError:
                clock_state = {}

            if str(user_id) not in clock_state:
                clock_state[str(user_id)] = {}

            # Update accounts
            accounts = get_tapchi_list(user_id)
            for acc in accounts:
                acc["clock_enabled"] = True
                acc["clock_font"] = font_index
                phone = acc.get("phone")

                debug_monshi(f"[CLOCK FONT] Font {font_index} set for {phone}")
                asyncio.create_task(clock_updater(acc, user_id))

                clock_state[str(user_id)][phone] = {
                    "clock_font": font_index,
                    "status": "on"
                }

            # Save everything
            with open(CLOCK_STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(clock_state, f, indent=2, ensure_ascii=False)

            save_accounts(user_id, accounts)

        except Exception as e:
            await update.callback_query.message.edit_text(f"خطا در ذخیره فونت ساعت: {e}")
            return

        await update.callback_query.message.edit_text("فونت ساعت انتخاب شد و ساعت کنار اسم فعال شد ✅")
        return
        
# انتخاب تصادفی فونت ساعت برای همه اکانت‌ها
    elif data == "randomize_fonts":
        import random

        CLOCK_STATE_FILE = os.path.join("data", "clock_state.json")

        try:
            # Load or init clock_state
            try:
                with open(CLOCK_STATE_FILE, "r", encoding="utf-8") as f:
                    clock_state = json.load(f)
            except FileNotFoundError:
                clock_state = {}

            if str(user_id) not in clock_state:
                clock_state[str(user_id)] = {}

            accounts = get_tapchi_list(user_id)
            total_fonts = 26
            font_pool = list(range(total_fonts))
            used_fonts = set()
            prev_fonts = {
                acc.get("phone"): clock_state.get(str(user_id), {}).get(acc.get("phone"), {}).get("clock_font")
                for acc in accounts
            }

            random.shuffle(font_pool)

            for acc in accounts:
                phone = acc.get("phone")
                prev_font = prev_fonts.get(phone)

                # Exclude fonts used this round and the previous one (if possible)
                available_fonts = [f for f in font_pool if f not in used_fonts and f != prev_font]
                if not available_fonts:
                    available_fonts = [f for f in font_pool if f != prev_font]
                if not available_fonts:
                    available_fonts = font_pool.copy()

                chosen_font = random.choice(available_fonts)
                used_fonts.add(chosen_font)

                acc["clock_enabled"] = True
                acc["clock_font"] = chosen_font

                debug_monshi(f"[RANDOM FONT] Font {chosen_font} set for {phone}")
                asyncio.create_task(clock_updater(acc, user_id))

                clock_state[str(user_id)][phone] = {
                    "clock_font": chosen_font,
                    "status": "on"
                }

            with open(CLOCK_STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(clock_state, f, indent=2, ensure_ascii=False)

            save_accounts(user_id, accounts)

            await update.callback_query.message.edit_text("فونت‌های ساعت به صورت تصادفی برای همه اکانت‌ها تنظیم شد ✅")
        except Exception as e:
            await update.callback_query.message.edit_text(f"خطا در تنظیم فونت تصادفی: {e}")
        return

#auto_reply_inline
    elif data == "Auto_reply":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        await update.callback_query.message.edit_text(
            text=(
                "اطلاعات درباره منشی اکانت:\n\n"
                "• منشی اکانت معمولی: اینجا میتونید تنظیم کنید که مثلا وقتی کسی برای اولین بار به یکی از اکانت‌های شما پیام بده "
                "پیامی که اینجا ثبت می‌کنید براش فرستاده میشه.\n\n"
                "• منشی اکانت پیشرفته: اینجا میتونید ثبت کنید که مثلا وقتی کسی مثلاً \"تپچی\" رو توی پیوی شما ارسال کنه "
                "\"لیست قیمت‌ها\" براش ارسال بشه."
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⚜️منشی اکانت معمولی⚜️", callback_data="normal_monshi")],
                [InlineKeyboardButton("⚜️منشی اکانت پیشرفته⚜️", callback_data="advanced_monshi")],
                [InlineKeyboardButton("✅️روشن کردن منشی اکانت✅️", callback_data="enable_monshi")],
                [InlineKeyboardButton("❌️خاموش کردن منشی اکانت❌️", callback_data="disable_monshi")],
                [InlineKeyboardButton("↪️بازگشت↩️", callback_data="back_to_panel")]
            ])
        )
        return
# #@@@
#    elif data == "enable_monshi":
#        if not is_subscription_valid(user_id):
#            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
#            return        
#        user_id = update.effective_user.id
#        set_auto_reply_status(user_id, True)
#        await update.callback_query.answer("منشی خودکار روشن شد✅️", show_alert=True)
#        await start_auto_reply_for_all_clients()  # Immediately trigger activation
#        return

#@@@
    elif data == "enable_monshi":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        user_id = update.effective_user.id
        set_auto_reply_status(user_id, True)
        await update.callback_query.answer("منشی خودکار روشن شد✅️", show_alert=True)

        accounts = get_tapchi_list(user_id)
        for acc in accounts:
            phone = acc.get("phone")
            if phone:
                session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
                lock = get_session_lock(session_path)

                if not lock.locked():
                    registered_clients.pop(phone, None)
                    task = asyncio.create_task(start_auto_reply_for_user(acc, user_id))
                    auto_reply_tasks[phone] = task

        return

    elif data == "disable_monshi":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        user_id = update.effective_user.id
        set_auto_reply_status(user_id, False)
        await update.callback_query.answer("منشی خودکار خاموش شد❌️", show_alert=True)
        return

# بازگشت به کنترل همگانی
    elif data == "back_to_panel":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        await show_general_management_panel(update.callback_query, context)
        return
        
# منشی اکانت معمولی
    elif data == "normal_monshi":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        user_id_str = str(user_id)
        messages = get_normal_monshi(user_id_str)
        buttons = []

        if messages:
            text = "پیام‌های فعلی منشی خودکار معمولی شما:\n\n"
            for i, msg in enumerate(messages):
                text += f"پیام {i + 1} شما:\n{msg}\n\n"
                buttons.append([InlineKeyboardButton(f"❌️حذف پیام {i + 1}❌️", callback_data=f"delete_normal_monshi_{i}")])
            text += "اطلاع: به صورت تصادفی یکی از این پیام‌ها به اولین نفری که به اکانت شما پیام بده ارسال میشه."
            buttons.insert(0, [InlineKeyboardButton("✅️اضافه کردن پیام منشی معمولی✅️", callback_data="add_normal_monshi")])
            buttons.append([InlineKeyboardButton("❌️حذف تمامی پیام‌ها❌️", callback_data="clear_normal_monshi")])
        else:
            text = "❌️پیامی برای این بخش ثبت نکردید.\n\nمیتونید پیام‌های منشی خودکار معمولی رو ثبت کنید."
            buttons = [[InlineKeyboardButton("✅️اضافه کردن پیام منشی معمولی✅️", callback_data="add_normal_monshi")]]

        buttons.append([InlineKeyboardButton("↪️بازگشت↩️", callback_data="Auto_reply")])

        await update.callback_query.message.edit_text(
            text=text,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        return
        
# ثبت پیام جدید منشی معمولی
    elif data == "add_normal_monshi":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        context.user_data["awaiting_normal_monshi"] = True

        await update.callback_query.message.edit_text(
            text="لطفا پیامی که میخواید به عنوان منشی خودکار اکانت ثبت بشه رو ارسال کنید:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌️لغو❌️", callback_data="normal_monshi")]
            ])
        )
        return
        
# حذف تمام پیام‌های منشی معمولی
    elif data == "clear_normal_monshi":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        clear_normal_monshi(str(user_id))
        await update.callback_query.message.edit_text(
            text="✅️ تمام پیام‌های منشی معمولی با موفقیت حذف شدند.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("↩️ بازگشت به منشی معمولی", callback_data="normal_monshi")]
            ])
        )
        return
        
# حذف یک پیام خاص منشی معمولی
    elif data.startswith("delete_normal_monshi_"):
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        index = int(data.split("_")[-1])
        success = delete_normal_monshi(str(user_id), index)

        if success:
            await update.callback_query.message.edit_text(
                text=f"پیام شماره {index + 1} با موفقیت حذف شد❌️",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("↩️ بازگشت به منشی معمولی", callback_data="normal_monshi")]
                ])
            )
        else:
            await update.callback_query.answer("مشکلی در حذف پیام وجود دارد", show_alert=True)
        return
# منشی اکانت پیشرفته
#    elif data == "advanced_monshi":
#        user_id_str = str(user_id)
#        adv_data = get_advanced_monshi(user_id_str)
#        buttons = []
#        text = ""

#        if adv_data:
#            text = "پیام‌های شما برای منشی اکانت پیشرفته:\n\n"
#            for i, (trigger, reply) in enumerate(adv_data.items()):
#                text += f"{i + 1}: \"{trigger}\" ⬇️\n\n«{reply}»\n\n"
#                buttons.append([InlineKeyboardButton(f"❌️حذف پیام {i + 1}❌️", callback_data=f"delete_advanced_monshi_{i}")])
#            text += "اطلاعات: مثلا اگه یکی \"سلام\" رو ارسال کنه میتونید پیام مخصوص اون رو ثبت کنید تا به صورت خودکار براش ارسال بشه."
#            buttons.insert(0, [InlineKeyboardButton("✅️اضافه کردن پیام منشی پیشرفته✅️", callback_data="add_advanced_monshi")])
#            buttons.append([InlineKeyboardButton("❌️حذف تمامی پیام‌ها❌️", callback_data="clear_advanced_monshi")])
#        else:
#            text = "❌️پیامی برای این بخش ثبت نکردید.\n\nاطلاعات: مثلا اگه یکی \"سلام\" رو ارسال کنه میتونید پیام مخصوص اون رو ثبت کنید تا به صورت خودکار براش ارسال بشه."
#            buttons = [[InlineKeyboardButton("✅️اضافه کردن پیام منشی پیشرفته✅️", callback_data="add_advanced_monshi")]]

#        buttons.append([InlineKeyboardButton("↪️بازگشت↩️", callback_data="Auto_reply")])

#        await update.callback_query.message.edit_text(
#            text=text,
#            reply_markup=InlineKeyboardMarkup(buttons)
#        )
#        return


# منشی اکانت پیشرفته
    elif data == "advanced_monshi":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        user_id_str = str(user_id)
        adv_data = get_advanced_monshi(user_id_str)
        buttons = []
        text = ""

        if adv_data:
            text = "پیام‌های شما برای منشی اکانت پیشرفته:\n\n"
            for i, (trigger, reply) in enumerate(adv_data.items()):
                text += f"{i + 1}: \"{trigger}\" ⬇️\n\n«{reply}»\n\n"
                buttons.append([InlineKeyboardButton(f"❌️حذف پیام {i + 1}❌️", callback_data=f"delete_advanced_monshi_{i}")])
            text += "اطلاعات: مثلا اگه یکی \"سلام\" رو ارسال کنه میتونید پیام مخصوص اون رو ثبت کنید تا به صورت خودکار براش ارسال بشه."
            buttons.insert(0, [InlineKeyboardButton("✅️اضافه کردن پیام منشی پیشرفته✅️", callback_data="add_advanced_monshi")])
            buttons.append([InlineKeyboardButton("❌️حذف تمامی پیام‌ها❌️", callback_data="clear_advanced_monshi")])
        else:
            text = "❌️پیامی برای این بخش ثبت نکردید.\n\nاطلاعات: مثلا اگه یکی \"سلام\" رو ارسال کنه میتونید پیام مخصوص اون رو ثبت کنید تا به صورت خودکار براش ارسال بشه."
            buttons = [[InlineKeyboardButton("✅️اضافه کردن پیام منشی پیشرفته✅️", callback_data="add_advanced_monshi")]]

        buttons.append([InlineKeyboardButton("↪️بازگشت↩️", callback_data="Auto_reply")])
# --- Safely edit callback message to avoid "message not modified" error ---
        new_text = text
        new_markup = InlineKeyboardMarkup(buttons)

        if (
            update.callback_query.message.text != new_text or
            update.callback_query.message.reply_markup != new_markup
        ):
            await update.callback_query.message.edit_text(
                text=new_text,
                reply_markup=new_markup
            )
        else:
            debug_banner("[EDIT SKIPPED] Message text and markup are unchanged.")

        return

# اضافه کردن پیام جدید به منشی پیشرفته - مرحله اول (trigger)
    elif data == "add_advanced_monshi":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        context.user_data["awaiting_advanced_trigger"] = True

        await update.callback_query.message.edit_text(
            text="لطفاً پیام اول رو وارد کنید:\n\n"
                 "اطلاع: این پیام یعنی پیامی که یکی به اکانت شما ارسال میکنه مثلا میگه \"قیمت\"",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("↪️بازگشت↩️", callback_data="advanced_monshi")]
            ])
        )
        return

# مرحله دوم - گرفتن پاسخ (reply)
    elif "awaiting_advanced_reply" in context.user_data:
        await update.callback_query.answer("لطفا پیام دوم را به صورت متنی وارد کنید.")
        return

# ذخیره نهایی پیام پیشرفته
    elif data == "save_advanced_monshi":
        trigger = context.user_data.get("advanced_trigger")
        reply = context.user_data.get("advanced_reply")

        if trigger and reply:
            add_advanced_monshi(user_id, trigger, reply)
            await update.callback_query.message.edit_text(
                text="✅️ پیام شما با موفقیت ذخیره شد.",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("↩️ بازگشت به منشی پیشرفته", callback_data="advanced_monshi")]
                ])
            )
        else:
            await update.callback_query.answer("مشکلی در ثبت پیام وجود دارد", show_alert=True)

        context.user_data.pop("advanced_trigger", None)
        context.user_data.pop("advanced_reply", None)
        return

# حذف یک پیام خاص از منشی پیشرفته
    elif data.startswith("delete_advanced_monshi_"):
        index = int(data.split("_")[-1])
        adv_data = list(get_advanced_monshi(user_id).items())

        if 0 <= index < len(adv_data):
            trigger = adv_data[index][0]
            delete_advanced_monshi(user_id, trigger)
            await update.callback_query.message.edit_text(
                text=f"پیام شماره {index + 1} با موفقیت حذف شد❌️",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("↩️ بازگشت به منشی پیشرفته", callback_data="advanced_monshi")]
                ])
            )
        else:
            await update.callback_query.answer("مشکلی در حذف پیام وجود دارد", show_alert=True)
        return

# حذف همه پیام‌های منشی پیشرفته
    elif data == "clear_advanced_monshi":
        clear_advanced_monshi(user_id)
        await update.callback_query.message.edit_text(
            text="✅️ تمامی پیام‌های منشی پیشرفته با موفقیت حذف شدند.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("↩️ بازگشت به منشی پیشرفته", callback_data="advanced_monshi")]
            ])
        )
        return
                                                                                    # ذخیره نهایی پیام منشی معمولی
    elif data == "save_normal_monshi":
        msg = context.user_data.get("last_normal_monshi_input")

        if msg:
            success = add_normal_monshi(str(user_id), msg)
            if success:
                await update.callback_query.message.edit_text(
                    text="✅️ پیام شما با موفقیت ذخیره شد.",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("↩️ بازگشت به منشی معمولی", callback_data="normal_monshi")]
                    ])
                )
            else:
                await update.callback_query.answer("شما قبلاً ۵ پیام ثبت کرده‌اید", show_alert=True)

        context.user_data.pop("last_normal_monshi_input", None)
        return
                      
    # --- Global Forward Toggle OFF ---
    elif data == "gm_forward_toggle_off":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        user_id = update.effective_user.id
        accounts = get_tapchi_list(user_id)
        for acc in accounts:
            acc["forward"]["status"] = "off"
        save_accounts(user_id, accounts)
        await update.callback_query.answer("همه اکانت‌ها خاموش شدند ❌", show_alert=True)
        await general_forward_panel(update.callback_query, context)
        return

# --- Identification Feature ---
    if data == "gm_identify":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug("Handling gm_identify")
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("✅️شروع کن✅️", callback_data="gm_identify_start")]
        ])
        await update.callback_query.message.edit_text(
            "روی گزینه زیر بزنید تا شناسایی عضویت های اجباری تمامی اکانت هاتون شروع بشه:",
            reply_markup=keyboard
        )
        return

    # --- Identification Feature ---
    if data == "gm_identify":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug("Handling gm_identify")
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("✅️شروع کن✅️", callback_data="gm_identify_start")]
        ])
        await update.callback_query.message.edit_text(
            "روی گزینه زیر بزنید تا شناسایی عضویت های اجباری تمامی اکانت هاتون شروع بشه:",
            reply_markup=keyboard
        )
        return 

    if data == "gm_identify_start":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug("Handling gm_identify_start")
        await update.callback_query.answer("شناسایی در حال شروع است!", show_alert=True)
        await update.callback_query.message.edit_text("شناسایی عضویت های اجباری در پس زمینه شروع شد!")
        asyncio.create_task(start_identification(context, update.callback_query.from_user.id))
        return

# --- For ادیت بیو ها ---
    if data == "gm_edit_bio":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        

        # ❗ Clear any leftover gm_mode so back doesn't misroute
        context.user_data.pop("gm_mode", None)

        # Display prompt for new bio
        await update.callback_query.message.edit_text(
            "بیو مورد نظر خود را اینجا ارسال کنید:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("↩️بازگشت↪️", callback_data="gm_back")]
            ])
        )
        context.user_data["awaiting_edit_bio"] = True
        return

    # Existing branch for confirming edit bio
    if data == "gm_confirm_edit_bio":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        new_bio = context.user_data.get("new_bio", "")
        if not new_bio:
            await update.callback_query.answer("هیچ بیویی وارد نشده است.", show_alert=True)
            return
        # Call your function to update the bio for all accounts
        await update.callback_query.message.edit_text(
            "بیو انتخابی شما ثبت شد و به زودی در تمامی اکانت ها ثبت میشود✅️"
        )
        await update_bio_for_accounts(update.callback_query.from_user.id, new_bio, context)
        return

# --- Existing branch for editing names ---
    if data == "gm_edit_name":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        

        # ❗ Make sure this isn't mistaken for coming from a sub-panel like timebound
        context.user_data.pop("gm_mode", None)

        # Display prompt for entering names; expected format: each line like "1: name"
        await update.callback_query.message.edit_text(
            "نام های مورد نظر را به صورت زیر ارسال کنید:\n1: name\n2: name\n3: name",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("↩️بازگشت↩️", callback_data="gm_back")]
            ])
        )
        context.user_data["awaiting_edit_name"] = True
        return

    if data == "gm_confirm_edit_name":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        new_names = context.user_data.get("new_names", [])
        if not new_names:
            await update.callback_query.answer("هیچ نامی وارد نشده است.", show_alert=True)
            return
        # Call your function to update the names (update only as many accounts as names provided)
        await update.callback_query.message.edit_text(
            "نام های انتخابی شما ثبت شد و به زودی در تمامی اکانت ها ثبت می‌شود✅️"
        )
        await update_name_for_accounts(update.callback_query.from_user.id, new_names, context)
        return

# Existing branch for account selection in مدیریت اکانت
    if data.startswith("tapchi_select:"):
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug("Handling tapchi_select")

        user_id = update.callback_query.from_user.id
        if not is_subscription_valid(user_id):
            await update.callback_query.answer("❌️اشتراک شما تمام شد❌️\nبرای ادامه کار با ربات اشتراک جدید خریداری کنید.", show_alert=True)
            return

        try:
            idx = int(data.split(":")[1])
            logging.debug(f"Selected account index: {idx}")
            phone_list = get_tapchi_list(user_id)
            if idx < 0 or idx >= len(phone_list):
                logging.debug("Invalid account index in tapchi_select")
                await update.callback_query.answer("ایندکس نامعتبر", show_alert=True)
                return
            phone_info = phone_list[idx]
            await show_phone_management(update.callback_query, context, idx, phone_info)
        except Exception as e:
            logging.error(f"Error handling tapchi_select: {e}")
            await update.callback_query.answer("خطا در انتخاب اکانت", show_alert=True)
        return

        

    # --- Branch for account selection in مدیریت اکانت ---
    if data.startswith("tapchi_select:"):
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug("Handling tapchi_select")
        try:
            idx = int(data.split(":")[1])
            logging.debug(f"Selected account index: {idx}")
            user_id = update.callback_query.from_user.id
            phone_list = get_tapchi_list(user_id)
            if idx < 0 or idx >= len(phone_list):
                logging.debug("Invalid account index in tapchi_select")
                await update.callback_query.answer("ایندکس نامعتبر", show_alert=True)
                return
            phone_info = phone_list[idx]
            await show_phone_management(update.callback_query, context, idx, phone_info)
        except Exception as e:
            logging.error(f"Error handling tapchi_select: {e}")
            await update.callback_query.answer("خطا در انتخاب اکانت", show_alert=True)
        return

    # --- Branch for phone management menu buttons ---
    if data.startswith("phone_menu:"):
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug("Handling phone_menu")
        parts = data.split(":")
        if len(parts) < 3:
            await update.callback_query.answer("دستور نامشخص", show_alert=True)
            return
        try:
            idx = int(parts[1])
        except Exception as e:
            logging.error(f"Error parsing index in phone_menu: {e}")
            await update.callback_query.answer("ایندکس نامشخص", show_alert=True)
            return
        option = parts[2]
        user_id = update.callback_query.from_user.id
        phone_list = get_tapchi_list(user_id)
        if idx < 0 or idx >= len(phone_list):
            await update.callback_query.answer("ایندکس نامشخص", show_alert=True)
            return
        phone_info = phone_list[idx]
        if option == "schedule":
            logging.debug("Handling phone_menu schedule option")
            await show_schedule_menu(update.callback_query, context, idx, phone_info)
            return
        elif option == "join_groups":
            logging.debug("Handling phone_menu join_groups option")
            context.user_data["phone_join_groups"] = idx
            await update.callback_query.message.edit_text("لطفا لینک گروه‌ها را ارسال کنید.\nبرای لغو: لغو")
            return
        elif option == "groups":
            logging.debug("Handling phone_menu groups option")
            await show_phone_groups(update.callback_query, context, idx, phone_info)
            return
        elif option == "back":
            logging.debug("Handling phone_menu back option")
            await show_tapchi_menu(update.callback_query, context)
            return
        else:
            await update.callback_query.answer("دستور نامشخص", show_alert=True)
            return
# e.g., "gm_timebound_set_time:5" => minute = 5            
    if data.startswith("gm_timebound_set_time:"):
        try:
            minute = int(data.split(":")[1])
        except Exception as e:
            logging.error(f"Error parsing gm_timebound_set_time: {e}")
            await update.callback_query.answer("خطا در تنظیم زمان", show_alert=True)
            return

        user_id = update.callback_query.from_user.id
        phone_list = get_tapchi_list(user_id)
        for acc in phone_list:
            acc["normal"]["interval"] = minute
        save_accounts(user_id, phone_list)

        await update.callback_query.answer(
            f"فاصله زمانی برای ارسال پیام همگانی روی {minute} دقیقه تنظیم شد ✅",
            show_alert=True
        )

        await general_timebound_panel(update.callback_query, context)
        return

    # ... (other branches follow here) ...
# --- Branch for deletion confirmation ---
    if data.startswith("tapchi_ask_delete:"):
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug("Handling tapchi_ask_delete")
        try:
            idx = int(data.split(":")[1])
            logging.debug(f"Parsed idx: {idx}")
        except Exception as e:
            logging.debug(f"Error parsing index in tapchi_ask_delete: {e}")
            await update.callback_query.answer("ایندکس نامشخص", show_alert=True)
            return
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("❌️حذف اکانت❌️", callback_data=f"tapchi_delete:{idx}")],
            [InlineKeyboardButton("↪️بازگشت↩️", callback_data="tapchi_menu")]
        ])
        await update.callback_query.message.edit_text("مطمئنید می‌خواهید اکانت را حذف کنید؟", reply_markup=keyboard)
        return

# --- Branch for actual deletion ---
    if data.startswith("tapchi_delete:"):
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug("Handling tapchi_delete")
        try:
            idx = int(data.split(":")[1])
            logging.debug(f"Parsed idx: {idx}")
        except Exception as e:
            logging.debug(f"Error parsing index in tapchi_delete: {e}")
            await update.callback_query.answer("ایندکس نامشخص", show_alert=True)
            return

        user_id = update.callback_query.from_user.id
        phone_list = get_tapchi_list(user_id)
        if idx < 0 or idx >= len(phone_list):
            logging.debug("Index out of range in tapchi_delete")
            await update.callback_query.answer("ایندکس خارج از محدوده", show_alert=True)
            return

        account = phone_list[idx]
        phone = account.get("phone")
        session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
        lock = get_session_lock(session_path)

        async with lock:
            try:
                # Log out and disconnect from Telegram session
                client = TelegramClient(session_path, API_ID, API_HASH)
                await client.connect()
                if await client.is_user_authorized():
                    await client.log_out()
                await client.disconnect()

                # Delete local session files
                for ext in [".session", ".session-journal"]:
                    path = session_path + ext
                    if os.path.exists(path):
                        os.remove(path)

                logging.debug(f"Logged out and deleted session for phone: {phone}")
            except Exception as e:
                logging.error(f"Error logging out/deleting session for {phone}: {e}")

# --- Clean up related phone entries in JSON files ---
            for json_file in ["clock_state.json", "auto_reply_status.json"]:
                file_path = os.path.join("data", json_file)
                try:
                    if os.path.exists(file_path):
                        with open(file_path, "r", encoding="utf-8") as f:
                            data = json.load(f)

                        user_key = str(user_id)
                        user_data = data.get(user_key)

                        if not user_data:
                            continue

                        if json_file == "auto_reply_status.json":
                            # Remove phone from 'accounts' list under the user
                            if "accounts" in user_data and phone in user_data["accounts"]:
                                user_data["accounts"].remove(phone)
                                logging.debug(f"Removed {phone} from {json_file} (accounts list)")

                            # Remove the entire user block if 'accounts' is now empty
                            if not user_data["accounts"]:
                                del data[user_key]

                        elif json_file == "clock_state.json":
                            # Remove phone from nested dictionary under user ID
                            if phone in user_data:
                                del user_data[phone]
                                logging.debug(f"Removed {phone} from {json_file}")

                            # Remove the user entry if no phones remain
                            if not user_data:
                                del data[user_key]

                        # Save the updated JSON back to file
                        with open(file_path, "w", encoding="utf-8") as f:
                            json.dump(data, f, indent=2, ensure_ascii=False)

                except Exception as e:
                    logging.error(f"Error updating {json_file} for {phone}: {e}")

            # --- Remove account from tapchi account list ---
            del phone_list[idx]
            save_accounts(user_id, phone_list)
            logging.debug(f"Deleted account at index: {idx} for phone: {phone}")

        # --- Confirm deletion to the user in chat ---
        await update.callback_query.message.edit_text(f"اکانت {phone} حذف شد❌️")
        return

# --- Branch for minute selection via interval picker ---
    if data.startswith("interval_pick:"):
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug("Handling interval_pick")
        parts = data.split(":")
        if len(parts) != 4:
            await update.callback_query.answer("داده نامعتبر", show_alert=True)
            return
        panel_type = parts[1]  # expected to be "normal_panel" or "forward_panel"
        try:
            idx = int(parts[2])
            minute = int(parts[3])
        except Exception as e:
            logging.error(f"Error parsing interval_pick data: {e}")
            await update.callback_query.answer("داده نامعتبر", show_alert=True)
            return
        logging.debug(f"Interval picked: {minute} minutes for account index {idx} and panel {panel_type}")
        user_id = update.callback_query.from_user.id
        phone_list = get_tapchi_list(user_id)
        if idx < 0 or idx >= len(phone_list):
            await update.callback_query.answer("ایندکس نامشخص", show_alert=True)
            return
        phone_info = phone_list[idx]
        if panel_type == "normal_panel":
            phone_info["normal"]["interval"] = minute
            save_accounts(user_id, phone_list)
            await update.callback_query.answer(f"زمان ارسال روی {minute} دقیقه تنظیم شد.", show_alert=True)
            await show_normal_panel(update.callback_query, context, idx, phone_list[idx])
        elif panel_type == "forward_panel":
            phone_info["forward"]["interval"] = minute
            save_accounts(user_id, phone_list)
            await update.callback_query.answer(f"زمان ارسال روی {minute} دقیقه تنظیم شد.", show_alert=True)
            await show_forward_panel(update.callback_query, context, idx, phone_info)
        else:
            await update.callback_query.answer("داده نامعتبر", show_alert=True)
        return

    # --- Branch for going back from interval picker ---
    if data.startswith("back_interval_picker:"):
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug("Handling back_interval_picker")
        parts = data.split(":")
        if len(parts) < 3:
            await update.callback_query.answer("داده نامعتبر", show_alert=True)
            return
        panel_type = parts[1]  # expected to be "normal_panel" or "forward_panel"
        try:
            idx = int(parts[2])
        except Exception as e:
            logging.error(f"Error parsing index in back_interval_picker: {e}")
            await update.callback_query.answer("ایندکس نامشخص", show_alert=True)
            return
        user_id = update.callback_query.from_user.id
        phone_list = get_tapchi_list(user_id)
        if idx < 0 or idx >= len(phone_list):
            await update.callback_query.answer("ایندکس نامشخص", show_alert=True)
            return
        phone_info = phone_list[idx]
        if panel_type == "normal_panel":
            await show_normal_panel(update.callback_query, context, idx, phone_list[idx])
        elif panel_type == "forward_panel":
            await show_forward_panel(update.callback_query, context, idx, phone_info)
        else:
            await update.callback_query.answer("داده نامعتبر", show_alert=True)
        return

    # --- Branch for special group buttons ---
    if data in {"gm_timebound", "gm_join_groups", "gm_account_status",  "gm_set_banner"}:
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug(f"Handling special group: {data}")
        if data == "gm_timebound":
            
            await general_timebound_panel(update.callback_query, context)
            return
        elif data == "gm_join_groups":
            context.user_data["gm_join_groups"] = True
            logging.debug("Set gm_join_groups to True")
            await update.callback_query.message.edit_text(
                "لطفا لینک گروه‌هایی را که می‌خواهید همه اکانت‌ها در آن عضو شوند ارسال کنید."
            )
            return
            
        elif data == "gm_account_status":
            user_id = update.callback_query.from_user.id
            logging.debug("Handling gm_account_status")
            wait_msg = await update.callback_query.message.reply_text(
                "چک کردن وضعیت اکانت های شما درحال بررسی است ممكن است چند دقیقه طول بکشد..."
            )
            asyncio.create_task(check_all_status_and_update(wait_msg, user_id, context))
            await update.callback_query.answer()
            return
# --- Set banner inside timebound ---
        elif data == "gm_set_banner":
            if not is_subscription_valid(user_id):
                await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
                return
            
            logging.debug("Handling gm_set_banner")

            # ✅ Tell gm_back we're inside timebound submenu
            context.user_data["inside_timebound"] = True

            context.user_data["in_set_banner_mode"] = True
            context.user_data["banner_adding_for"] = ("gm", "gm")

            await update.callback_query.message.edit_text(
                "بنر خود را وارد کنید:",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("↪️بازگشت↩️", callback_data="gm_back")]
                ])
            )
            return

# --- NEW FIX: Handle gm_update_all_groups callback ---
    if data == "gm_update_all_groups":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug("Handling gm_update_all_groups")
        user_id = update.callback_query.from_user.id

        # Respond immediately to prevent UI freeze
        await query.answer("در حال بروزرسانی تمام گروه‌ها...", show_alert=True)

        async def update_all_user_groups(user_id, context):
            accounts = get_tapchi_list(user_id)
            updated_accounts = []
            failed_phones = []

            for phone_info in accounts:
                try:
                    groups = await asyncio.wait_for(
                        update_groups_from_telethon(user_id, phone_info),
                        timeout=20
                    )
                    phone_info["groups"] = groups
                    updated_accounts.append(phone_info)
                except asyncio.TimeoutError:
                    fix_debug(f"[GROUP UPDATE TIMEOUT] {phone_info.get('phone')}")
                    failed_phones.append(phone_info.get("phone"))
                except Exception as e:
                    fix_debug(f"[UPDATE GROUPS] Failed for {phone_info.get('phone')}: {e}")
                    failed_phones.append(phone_info.get("phone"))

            if updated_accounts:
                save_accounts(user_id, updated_accounts)

            if failed_phones:
                failed_msg = "برخی اکانت‌ها آپدیت نشدند:\n" + "\n".join(failed_phones)
                await context.bot.send_message(chat_id=user_id, text=failed_msg)

            await context.bot.send_message(
                chat_id=user_id,
                text="✅ گروه‌های همه اکانت‌ها بروزرسانی شدند." if updated_accounts else "❌ هیچ گروهی بروزرسانی نشد."
            )

        # Run updates in the background
        asyncio.create_task(update_all_user_groups(user_id, context))
        return

# --- NEW FIX: Handle gm_timebound_toggle callback ---
    if data == "gm_timebound_toggle":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        

        logging.debug("Handling gm_timebound_toggle")

        # ✅ Mark this as a sub-option of timebound
        context.user_data["back_to"] = "gm_timebound"

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("✅️روشن کردن تمامی اکانت‌ ها✅️", callback_data="gm_toggle_all:on")],
            [InlineKeyboardButton("❌️خاموش کردن تمامی اکانت‌ ها❌️", callback_data="gm_toggle_all:off")],
            [InlineKeyboardButton("↪️بازگشت↩️", callback_data="gm_back")]
        ])

        await update.callback_query.message.edit_text("گزینه مورد نظر را انتخاب کنید:", reply_markup=keyboard)
        return
#all
    if data.startswith("gm_toggle_all:"):
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        mode = data.split(":")[1]
        logging.debug(f"Handling gm_toggle_all with mode: {mode}")
        user_id = update.callback_query.from_user.id
        phone_list = get_tapchi_list(user_id)
        if mode == "on":
            for acc in phone_list:
                acc["normal"]["status"] = "on"
                interval = acc["normal"].get("interval") or 60
                acc["normal"]["next_send"] = (datetime.now() + timedelta(minutes=interval)).isoformat()
            save_accounts(user_id, phone_list)
            await update.callback_query.answer("تمامی اکانت‌ها روشن شدند✅️", show_alert=True)
        elif mode == "off":
            for acc in phone_list:
                acc["normal"]["status"] = "off"
                acc["normal"]["next_send"] = None
            save_accounts(user_id, phone_list)
            await update.callback_query.answer("تمامی اکانت ها خاموش شدند❌️", show_alert=True)
        await show_general_management_panel(update.callback_query, context)
        return
# --- Set time (inside timebound) ---
    if data == "gm_timebound_interval_show":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        

        set_banner_debug("Handling gm_timebound_interval_show")

        # ✅ Mark as inside timebound submenu
        context.user_data["inside_timebound"] = True
        set_banner_debug("Marked 'inside_timebound' as True in user_data")

        await general_set_time(update.callback_query, context)
        set_banner_debug("Called general_set_time with mode='timebound'")
        return

    if data == "confirm_new_banner_gm":
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug("Handling confirm_new_banner_gm")
        new_banner = context.user_data.get("temp_banner", "")
        if new_banner:
            user_id = update.callback_query.from_user.id
            accounts = get_tapchi_list(user_id)
            for acc in accounts:
                acc["normal"]["banners"] = [new_banner]
            save_accounts(user_id, accounts)
            await update.callback_query.answer("بنر جدید برای همه اکانت‌ها ثبت شد.", show_alert=True)
            await show_general_management_panel(update.callback_query, context)
            context.user_data.pop("temp_banner", None)
        else:
            await update.callback_query.answer("بنر خالی است!", show_alert=True)
        return

    if data.startswith("banner_mgr:"):
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug("Handling banner_mgr")
        parts = data.split(":")
        if len(parts) != 4:
            await update.callback_query.answer("داده نامعتبر", show_alert=True)
            return
        panel_mode = parts[1]
        try:
            idx = int(parts[2])
            logging.debug(f"Parsed idx in banner_mgr: {idx}")
        except Exception as e:
            logging.debug(f"Error parsing index in banner_mgr: {e}")
            await update.callback_query.answer("ایندکس نامشخص", show_alert=True)
            return
        action = parts[3]
        if action == "delall":
            logging.debug("Handling banner_mgr delall")
            await process_banner_deletion(update.callback_query, context, idx, panel_mode)
            return
        elif action == "add":
            logging.debug("Handling banner_mgr add")
            context.user_data["in_set_banner_mode"] = True
            context.user_data["banner_adding_for"] = (idx, panel_mode)
            await update.callback_query.message.edit_text(
                "بنر خود را وارد کنید:",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("↪️بازگشت↩️", callback_data=f"{panel_mode}:{idx}:back")]])
            )
            return
#confirm banner
    if data.startswith("confirm_new_banner:"):
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        try:
            idx = int(data.split(":")[1])
        except Exception:
            await update.callback_query.answer("داده نامشخص", show_alert=True)
            return
        user_id = update.callback_query.from_user.id
        phone_list = get_tapchi_list(user_id)
        phone_info = phone_list[idx]
        new_banner = context.user_data.get("temp_banner", "")
        if new_banner:
            phone_info["normal"]["banners"] = [new_banner]
            save_accounts(user_id, phone_list)
            await update.callback_query.answer("بنر جدید ثبت شد.", show_alert=True)
            await show_banner_manager(update.callback_query, context, idx, "normal_panel")
            context.user_data.pop("temp_banner", None)
        else:
            await update.callback_query.answer("بنر خالی است!", show_alert=True)
        return
#status
    if data.startswith("tapchi_status:"):        
        logging.debug("Handling tapchi_status")

        user_id = update.callback_query.from_user.id
        if not is_subscription_valid(user_id):
            await update.callback_query.answer("❌️اشتراک شما تمام شد❌️\nبرای ادامه کار با ربات اشتراک جدید خریداری کنید.", show_alert=True)
            return

        try:
            idx = int(data.split(":")[1])
            logging.debug(f"Parsed idx: {idx}")
        except Exception as e:
            logging.debug(f"Error parsing index in tapchi_status: {e}")
            await update.callback_query.answer("ایندکس نامشخص", show_alert=True)
            return
        user_id = update.callback_query.from_user.id
        phone_list = get_tapchi_list(user_id)
        if idx < 0 or idx >= len(phone_list):
            logging.debug("Index out of range in tapchi_status")
            await update.callback_query.answer("ایندکس خارج از محدوده", show_alert=True)
            return
        wait_msg = await update.callback_query.message.reply_text(
            "چک کردن وضعیت اکانت درحال بررسی است لطفا صبر کنید..."
        )
        asyncio.create_task(check_individual_status_and_update(wait_msg, user_id, idx, context))
        await update.callback_query.answer()
        return
        
#schedule_menu:
    if data.startswith("schedule_menu:"):
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug("Handling schedule_menu")
        parts = data.split(":")
        if len(parts) < 3:
            await update.callback_query.answer("دستور نامشخص!", show_alert=True)
            return
        try:
            idx = int(parts[1])
            logging.debug(f"Parsed idx in schedule_menu: {idx}")
        except Exception as e:
            logging.debug(f"Error parsing idx in schedule_menu: {e}")
            await update.callback_query.answer("ایندکس نامشخص", show_alert=True)
            return
        option = parts[2]
        user_id = update.callback_query.from_user.id
        phone_list = get_tapchi_list(user_id)
        if idx < 0 or idx >= len(phone_list):
            logging.debug("Index out of range in schedule_menu")
            await update.callback_query.answer("ایندکس نامشخص", show_alert=True)
            return
        if option == "normal":
            logging.debug("Handling schedule_menu normal option")
            await show_normal_panel(update.callback_query, context, idx, phone_list[idx])
            return
        elif option == "forward":
            logging.debug("Handling schedule_menu forward option")
            await show_forward_panel(update.callback_query, context, idx, phone_list[idx])
            return
        elif option == "back":
            logging.debug("Handling schedule_menu back option")
            await show_tapchi_menu(update.callback_query, context)
            return
        else:
            logging.debug(f"Unknown option in schedule_menu: {option}")
            await update.callback_query.answer("دستور نامشخص!", show_alert=True)
            return
    # ----- Normal Panel Branch -----
    if data.startswith("normal_panel:"):
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        logging.debug("Handling normal_panel")
        parts = data.split(":")
        if len(parts) < 3:
            await update.callback_query.answer("دستور نامشخص!", show_alert=True)
            return
        try:
            idx = int(parts[1])
            logging.debug(f"Parsed idx in normal_panel: {idx}")
        except Exception as e:
            logging.debug(f"Error parsing idx in normal_panel: {e}")
            await update.callback_query.answer("ایندکس نامشخص", show_alert=True)
            return
        user_id = update.callback_query.from_user.id
        phone_list = get_tapchi_list(user_id)
        if idx < 0 or idx >= len(phone_list):
            logging.debug("Index out of range in normal_panel")
            await update.callback_query.answer("ایندکس نامشخص", show_alert=True)
            return
        phone_info = phone_list[idx]
        action = parts[2]
        logging.debug(f"Handling normal_panel action: {action}")
        if action == "set_time":
            await update.callback_query.answer()
            await show_interval_picker(update.callback_query, context, idx, "normal_panel")
            return
        elif action == "set_banner":
            context.user_data["in_set_banner_mode"] = True
            context.user_data["banner_adding_for"] = (idx, "normal_panel")
            await update.callback_query.message.edit_text(
                "بنر خود را وارد کنید:",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("↪️بازگشت↩️", callback_data=f"normal_panel:{idx}:back")]
                ])
            )
            return
#333
#333 --- FIX: Non-blocking group refresh for single account ---
        elif action == "refresh":
            # Respond immediately to prevent button freeze
            await update.callback_query.answer("در حال بروزرسانی گروه‌ها...", show_alert=True)

            async def refresh_single_account(user_id, phone_info, idx, context):
                try:
                    groups = await update_groups_from_telethon(user_id, phone_info)
                    phone_info["groups"] = groups

                    # Refresh updated account in DB
                    phone_list = get_tapchi_list(user_id)
                    phone_list[idx] = phone_info
                    save_accounts(user_id, phone_list)

                    await context.bot.send_message(
                        chat_id=user_id,
                        text=f"✅ گروه‌های اکانت {phone_info.get('phone', 'نامشخص')} بروزرسانی شدند."
                    )

                    # Optional: refresh panel automatically after update
                    await show_normal_panel(update.callback_query, context, idx, phone_list[idx])

                except Exception as e:
                    fix_debug(f"[REFRESH ACCOUNT] Failed for {phone_info.get('phone')}: {e}")
                    await context.bot.send_message(
                        chat_id=user_id,
                        text="❌ بروزرسانی گروه‌ها با خطا مواجه شد."
                    )

            asyncio.create_task(refresh_single_account(user_id, phone_info, idx, context))
            return
#turning on
        elif action == "turn_on":
            phone_list = get_tapchi_list(user_id)
            phone_info = phone_list[idx]  # get the fresh version

            if phone_info["normal"]["status"] == "on":
                phone_info["normal"]["status"] = "off"
                phone_info["normal"]["next_send"] = None
                await update.callback_query.answer("اکانت خاموش شد.", show_alert=True)
            else:
#@@@                
                phone_info["normal"]["status"] = "on"
                interval = phone_info["normal"].get("interval") or 60
                phone_info["normal"]["next_send"] = (datetime.now() + timedelta(minutes=interval)).isoformat()
                await update.callback_query.answer("اکانت روشن شد.", show_alert=True)

            save_accounts(user_id, phone_list)
            await show_normal_panel(update.callback_query, context, idx, phone_list[idx])
            return
#back            
        elif action == "back":
            context.user_data.pop("in_set_banner_mode", None)
            context.user_data.pop("banner_adding_for", None)
            await update.callback_query.answer()
            await show_normal_panel(update.callback_query, context, idx, phone_list[idx])
            return
        else:
            await update.callback_query.answer("دستور نامشخص!", show_alert=True)
            return

    # ----- Forward Panel Branch -----
    elif data.startswith("forward_panel:"):
        if not is_subscription_valid(user_id):
            await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
            return        
        # Expected data format: forward_panel:{idx}:{action}
        parts = data.split(":")
        try:
            idx = int(parts[1])
        except Exception as e:
            await update.callback_query.answer("ایندکس نامعتبر", show_alert=True)
            return
        action = parts[2]
        user_id = update.callback_query.from_user.id
        phone_info = get_tapchi_list(user_id)[idx]
        
        if action == "set_time":
            await update.callback_query.answer()
            await show_interval_picker(update.callback_query, context, idx, "forward_panel")
            return
#forward banner        
        elif action == "set_banner":
            if not is_subscription_valid(user_id):
                await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
                return            
            banner = phone_info["forward"]["banner"]
            if banner:
                text = f"بنر فعلی شما:\nلینک بنر شما: {banner}"
            else:
                text = "❌️شما هیچ بنر فورواردی ثبت نکرده اید❌️"
            markup = InlineKeyboardMarkup([
                [InlineKeyboardButton("✅️ثبت بنر فوروارد✅️", callback_data=f"forward_panel:{idx}:register_banner")],
                [InlineKeyboardButton("↪️بازگشت↩️", callback_data=f"forward_panel:{idx}:back")]
            ])
            await update.callback_query.message.edit_text(text, reply_markup=markup)
            return
#register banner        
        elif action == "register_banner":
            if not is_subscription_valid(user_id):
                await query.answer("⛔️ شما اشتراکی ندارید", show_alert=True)
                return            
            text = "اگر قصد اضافه کردن بنر فوروارد دارید لطفا لینک بنر خود را ارسال کنید(فقط لینک):"
            markup = InlineKeyboardMarkup([
                [InlineKeyboardButton("❌️لغو❌️", callback_data=f"forward_panel:{idx}:cancel_banner")]
            ])
            context.user_data["awaiting_forward_banner"] = idx
            await update.callback_query.message.edit_text(text, reply_markup=markup)
            return
        
        elif action == "cancel_banner":
            await show_forward_panel(update.callback_query, context, idx, phone_info)
            return
#make sure to add this # above it and make sure the Indentation is like this one     
        elif action == "toggle":
            if phone_info["forward"]["status"] == "on":
                phone_info["forward"]["status"] = "off"
                phone_info["forward"]["next_send"] = None
            else:
                phone_info["forward"]["status"] = "on"
                phone_info["normal"]["status"] = "off"
                interval = phone_info["forward"].get("interval", 5)
                phone_info["forward"]["next_send"] = (datetime.now() + timedelta(minutes=interval)).isoformat()

            phone_list = get_tapchi_list(user_id)
            save_accounts(user_id, phone_list)
            await show_forward_panel(update.callback_query, context, idx, phone_info)
            return
#222
        elif action == "refresh":
            groups = await update_groups_from_telethon(user_id, phone_info)
            phone_info["groups"] = groups

            # Refresh updated account from DB
            phone_list = get_tapchi_list(user_id)
            phone_list[idx] = phone_info
            save_accounts(user_id, phone_list)

            await update.callback_query.answer("گروه‌ها به‌روز شدند.", show_alert=True)
            await show_forward_panel(update.callback_query, context, idx, phone_info)
            return
        
        elif action == "back":
            await show_schedule_menu(update.callback_query, context, idx, phone_info)
            return
        else:
            await update.callback_query.answer("دستور نامشخص!", show_alert=True)
            return

    # Other callback branches go here...

    if data.startswith("code_digit:"):        
        digit = data.split(":")[1]
        logging.debug(f"Handling code_digit, digit: {digit}")
        current_code = context.user_data.get("code_digits", "")
        current_code += digit
        context.user_data["code_digits"] = current_code
        await update_code_keypad(update.callback_query, context)
        return
    elif data == "code_confirm":
        logging.debug("Handling code_confirm")
        await confirm_code_entry(update.callback_query, context)
        return
#codeclear        
    elif data == "code_clear":
        logging.debug("Handling code_clear")
        context.user_data["code_digits"] = ""
        await update_code_keypad(update.callback_query, context)
        return
#buy_trial
    elif data.startswith("buy_trial:"):
        logging.debug("Handling buy_trial")
        user_id = str(update.callback_query.from_user.id)

# Check if trial is already active or was used before
        if is_trial_active(user_id) or has_used_trial_before(user_id):
            await update.callback_query.answer("شما قبلاً تست تپچی را گرفته‌اید!", show_alert=True)
            return

# Set 1-hour expiry
        tehran = pytz.timezone("Asia/Tehran")
        now = datetime.now(tehran)
        expiry = now + timedelta(hours=6)

        # Mark trial as used and save it
        trials = load_trials()
        trials[str(user_id)] = {
            "expiry": expiry.isoformat(),
            "used": True
        }
        save_trials(trials)

        # Optionally add to subscriptions for compatibility
        if user_id not in user_subscriptions:
            user_subscriptions[user_id] = []
        user_subscriptions[user_id].append({
            "expiry": expiry.isoformat(),
            "allowed_accounts": 1,
            "is_trial": True
        })
        save_subscriptions()

        # Confirmation message
        await update.callback_query.message.edit_text("✅ تپچی تست 6 ساعته فعال شد. می‌تونید از منوی اصلی اکانت اضافه کنید.")

        # Auto-expire in 1 hour
        context.job_queue.run_once(end_trial_job, 3600, chat_id=int(user_id), name=f"trial_{user_id}")
        return
       


#buy_subscription        
    elif data.startswith("buy_subscription:"):
        logging.debug("Handling buy_subscription")
        try:
            parts = data.split(":")
            allowed = int(parts[1])
            price = int(parts[2])
            logging.debug(f"Parsed subscription: allowed={allowed}, price={price}")
        except Exception as e:
            logging.debug(f"Error parsing buy_subscription data: {e}")
            await update.callback_query.answer("Invalid subscription data", show_alert=True)
            return
#userid
        user_id = update.callback_query.from_user.id
        current_subs = user_subscriptions.get(str(user_id), [])

        if isinstance(current_subs, dict):
            current_subs = [current_subs]
        elif isinstance(current_subs, str):
            try:
                current_subs = json.loads(current_subs)
                if isinstance(current_subs, dict):
                    current_subs = [current_subs]
                elif not isinstance(current_subs, list):
                    current_subs = []
            except:
                current_subs = []
        elif not isinstance(current_subs, list):
            current_subs = []

        current_max_allowed = 0
        tehran = pytz.timezone("Asia/Tehran")
        now = datetime.now(tehran)
#b
        for sub in current_subs:
            expiry = datetime.fromisoformat(sub["expiry"])
            if expiry.tzinfo is None:
                expiry = tehran.localize(expiry)
            else:
                expiry = expiry.astimezone(tehran)
            now = datetime.now(tehran)
            if now < expiry:
                current_max_allowed = max(current_max_allowed, sub.get("allowed_accounts", 0))

        if allowed <= current_max_allowed:
            logging.debug("Subscription not upgradeable")
            await update.callback_query.answer(
                "❌️این پلن رو نمیتونید خریداری کنید،فقط بالاتر از پلن فعلیتون رو میتونید بخرید.❌️",
                show_alert=True
            )
            return

        await update.callback_query.answer(
            "پلن شما قابل خرید است، لطفاً ادامه دهید...",
            show_alert=True
        )

        confirmation_text = ("🔰پلن انتخابی شما:\n"
                             "📅مدت زمان: 30 روز\n"
                             f"🚀تعداد اکانت : برای {allowed} اکانت\n"
                             f"💰قیمت: {price:,} تومان\n\n"
                             "💳 روش پرداخت را انتخاب کنید:")
        context.user_data["pending_subscription"] = {"allowed": allowed, "price": price, "duration": 30}
        
        # Get user balance
        user_balance = get_balance(user_id)
        keyboard_buttons = []
        
        # Add balance payment option if user has enough balance
        if user_balance >= price:
            keyboard_buttons.append([InlineKeyboardButton("💰 پرداخت از موجودی کیف پول", callback_data="confirm_subscription")])
        
        # Always add ZarinPal payment option
        keyboard_buttons.append([InlineKeyboardButton("💳 پرداخت آنلاین (زرین‌پال)", callback_data="pay_zarinpal")])
        keyboard_buttons.append([InlineKeyboardButton("↪️بازگشت↩️", callback_data="back_to_subscription")])
        
        keyboard = InlineKeyboardMarkup(keyboard_buttons)
        await update.callback_query.message.edit_text(confirmation_text, reply_markup=keyboard)
        return

    if data == "confirm_subscription":
        logging.debug("Handling confirm_subscription")
        pending = context.user_data.get("pending_subscription")
        if not pending:
            await update.callback_query.answer("No pending subscription.", show_alert=True)
            return
        allowed = pending["allowed"]
        price = pending["price"]
        duration = pending["duration"]
        user_id = update.callback_query.from_user.id
        bal = get_balance(user_id)
        subs = user_subscriptions.get(str(user_id), [])
        tehran = pytz.timezone("Asia/Tehran")
        active_subs = []
#a        
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

        for s in subs:
            expiry_dt = datetime.fromisoformat(s["expiry"])
            if expiry_dt.tzinfo is None:
                expiry_dt = tehran.localize(expiry_dt)
            else:
                expiry_dt = expiry_dt.astimezone(tehran)
            now_dt = datetime.now(tehran)
            if expiry_dt > now_dt:
                active_subs.append(s)
        if active_subs and active_subs[0]["allowed_accounts"] < allowed:
            current_sub = active_subs[0]
            final_price, remaining_days, unused_value = calculate_upgrade_price(current_sub, price)
            upgrade_text = (
                "🔰گزارش تپچی های فعلی شما:\n\n"
                f"♻️پلن قبلی تپچی: {current_sub['allowed_accounts']} اکانت یک ماهه\n"
                f"📆روز های باقی مانده از تپچی قبلی: {remaining_days} روز\n"
                f"💰مانده مبلغ از تپچی قبلی: {unused_value:,.0f}T\n"
                f"👤قیمت تپچی فعلی که کاربر می‌خواهد بخرد: {price:,.0f}T\n\n"
                f"🚀قیمت نهایی برای {allowed} تپچی یک ماهه:\n"
                f"{price:,.0f} - {unused_value:,.0f} = {final_price:,.0f}T\n\n"
                f"✅️مبلغ مورد نیاز برای خرید {allowed} تپچی: {final_price:,.0f}T\n\n"
                "💳 روش پرداخت را انتخاب کنید:"
            )
            
            # Get user balance for upgrade
            user_balance = get_balance(user_id)
            keyboard_buttons = []
            
            # Add balance payment option if user has enough balance
            if user_balance >= final_price:
                keyboard_buttons.append([InlineKeyboardButton("💰 پرداخت از موجودی کیف پول", callback_data="confirm_upgrade_subscription")])
            
            # Always add ZarinPal payment option for upgrades
            keyboard_buttons.append([InlineKeyboardButton("💳 پرداخت آنلاین (زرین‌پال)", callback_data="pay_upgrade_zarinpal")])
            keyboard_buttons.append([InlineKeyboardButton("↪️بازگشت↩️", callback_data="back_to_subscription")])
            
            keyboard = InlineKeyboardMarkup(keyboard_buttons)
            context.user_data["pending_upgrade_subscription"] = {
                "allowed": allowed,
                "final_price": final_price,
                "duration": duration,
                "unused_value": unused_value,
                "base_price": price,
                "current_sub": current_sub
            }
            await update.callback_query.message.edit_text(upgrade_text, reply_markup=keyboard)
            return
        if bal < price:
            diff = price - bal
            insufficient_text = (f"مبلغ مورد نیاز: {price:,} تومان\n"
                                 f"موجودی حساب: {bal:,} تومان\n"
                                 f"شما به {diff:,} تومان نیاز دارید.\n"
                                 "برای شارژ حساب به ادمین پیام بدید.")
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("💰شارژ حساب 💰", callback_data="charge_account")],
                [InlineKeyboardButton("↪️بازگشت↩️", callback_data="back_to_subscription")]
            ])
            await update.callback_query.message.edit_text(insufficient_text, reply_markup=keyboard)
            return
        cut_balance(user_id, price)
        expiry = datetime.utcnow() + timedelta(days=duration)
        sub = {"allowed_accounts": allowed, "expiry": expiry.isoformat(), "price": price}
        if isinstance(subs, dict):
            subs = [subs]
        subs.append(sub)
        user_subscriptions[str(user_id)] = subs
        save_subscriptions()
        success_text = f"شما با موفقیت پلن تپچی یک ماهه برای {allowed} اکانت رو خریداری کردید🎉"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📲اضافه کردن اکانت 📲", callback_data="goto_tapchi")],
            [InlineKeyboardButton("↪️بازگشت↩️", callback_data="back_to_subscription")]
        ])
        await update.callback_query.message.edit_text(success_text, reply_markup=keyboard)
        context.user_data.pop("pending_subscription", None)
        return
#@@@
    if data == "confirm_upgrade_subscription":
        logging.debug("Handling confirm_upgrade_subscription")
        upgrade = context.user_data.get("pending_upgrade_subscription")
        if not upgrade:
            await update.callback_query.answer("No pending upgrade.", show_alert=True)
            return

        user_id = update.callback_query.from_user.id
        final_price = upgrade["final_price"]
        bal = get_balance(user_id)

        if bal < final_price:
            diff = final_price - bal
            insufficient_text = (f"مبلغ مورد نیاز: {final_price:,.0f}T\n"
                                 f"موجودی حساب: {bal:,}T\n"
                                 f"شما به {diff:,.0f}T نیاز دارید.\n"
                                 "برای شارژ حساب به ادمین پیام بدید.")
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("💰شارژ حساب 💰", callback_data="charge_account")],
                [InlineKeyboardButton("↪️بازگشت↩️", callback_data="back_to_subscription")]
            ])
            await update.callback_query.message.edit_text(insufficient_text, reply_markup=keyboard)
            return

        # Deduct balance
        cut_balance(user_id, final_price)

        # Load and fix old subscriptions
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

        tehran = pytz.timezone("Asia/Tehran")
        now = datetime.now(tehran)
        for s in subs:
            expiry = datetime.fromisoformat(s["expiry"])
            if expiry.tzinfo is None:
                expiry = tehran.localize(expiry)
            if expiry > now:
                s["allowed_accounts"] = upgrade["allowed"]
                s["price"] = s["price"] + final_price
                s["expiry"] = (now + timedelta(days=upgrade["duration"])).isoformat()
                break
        else:
            # No active sub found, create new one
            expiry = datetime.utcnow() + timedelta(days=upgrade["duration"])
            new_sub = {
                "allowed_accounts": upgrade["allowed"],
                "expiry": expiry.isoformat(),
                "price": upgrade["base_price"]
            }
            subs.append(new_sub)

        user_subscriptions[str(user_id)] = subs
        save_subscriptions()

        success_text = f"شما با موفقیت پلن تپچی یک ماهه برای {upgrade['allowed']} اکانت رو خریداری کردید🎉"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📲اضافه کردن اکانت 📲", callback_data="goto_tapchi")],
            [InlineKeyboardButton("↪️بازگشت↩️", callback_data="back_to_subscription")]
        ])
        await update.callback_query.message.edit_text(success_text, reply_markup=keyboard)
        context.user_data.pop("pending_upgrade_subscription", None)
        return
#back        
    if data == "back_to_subscription":
        logging.debug("Handling back_to_subscription")
        context.user_data.pop("pending_subscription", None)

        user_id = update.callback_query.from_user.id
        buttons = []

        # Only show trial option if it's not active
        if not is_trial_active(user_id):
            buttons.append([
                InlineKeyboardButton("🔰تپچی تست 6 ساعته رایگان🔰", callback_data="buy_trial:6:0")
            ])
#@@@
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 1 اکانت: 30,000 تومان 🟣", callback_data="buy_subscription:1:30000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 2 اکانت: 60,000 تومان 🟣", callback_data="buy_subscription:2:60000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 3 اکانت: 90,000 تومان 🟣", callback_data="buy_subscription:3:90000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 4 اکانت: 120,000 تومان 🟣", callback_data="buy_subscription:4:120000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 5 اکانت: 150,000 تومان 🟣", callback_data="buy_subscription:5:150000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 6 اکانت: 180,000 تومان 🟣", callback_data="buy_subscription:6:180000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 7 اکانت: 210,000 تومان 🟣", callback_data="buy_subscription:7:210000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 8 اکانت: 240,000 تومان 🟣", callback_data="buy_subscription:8:240000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 9 اکانت: 270,000 تومان 🟣", callback_data="buy_subscription:9:270000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 10 اکانت: 300,000 تومان 🟣", callback_data="buy_subscription:10:300000")])
        buttons.append([InlineKeyboardButton("🟣 تپچی یک ماهه برای 20 اکانت: 600,000 تومان 🟣", callback_data="buy_subscription:20:600000")])

        kb = InlineKeyboardMarkup(buttons)

        await update.callback_query.edit_message_text(
            text="لطفاً یک پلن اشتراک را انتخاب کنید:",
            reply_markup=kb
        )
        return
    elif data == "pay_zarinpal":
        logging.debug("Handling pay_zarinpal")
        await handle_zarinpal_payment(update, context)
        return
    elif data.startswith("verify_zarinpal:"):
        logging.debug("Handling verify_zarinpal")
        await handle_zarinpal_verification(update, context)
        return
    elif data == "pay_upgrade_zarinpal":
        logging.debug("Handling pay_upgrade_zarinpal")
        await handle_upgrade_zarinpal_payment(update, context)
        return
    elif data == "charge_account":
        logging.debug("Handling charge_account")
        await update.callback_query.message.edit_text("برای شارژ حساب خود به پشتیبانی پیام دهید:\n🆔 @Telbot_charge")
        return
    elif data == "goto_tapchi":
        logging.debug("Handling goto_tapchi")
        await show_tapchi_menu(update.callback_query, context)
        return
    elif data == "gm_back":
        logging.debug("Handling gm_back")
        await update.callback_query.answer()
        await show_general_management_panel(update.callback_query, context)
        return
        #end of inline_callback_handler
        

                
async def end_trial_job(context):
    user_id = str(context.job.chat_id)

    # Remove from trial file
    trials = load_trials()
    if user_id in trials:
        del trials[user_id]
        save_trials(trials)

    # Optional: Also clean from user_subscriptions
    if user_id in user_subscriptions:
        user_subscriptions[user_id] = [sub for sub in user_subscriptions[user_id] if not sub.get("is_trial")]
        save_subscriptions()

    try:
        await context.bot.send_message(
            chat_id=int(user_id),
            text="⏰ مدت تپچی تست 6 ساعته شما به پایان رسید."
        )
    except Exception as e:
        logging.warning(f"Failed to notify user {user_id} about trial end: {e}")
        
async def process_group_forced_join(client, group, user_id, context):    
        

    # continue with forced join logic
    try:
        entity = await client.get_entity(group["id"])
    except Exception as e:
        return None
    try:
        await client.send_message(entity, "سلام")
    except Exception as e:
        if "can't write" in str(e).lower():
            return None
    await asyncio.sleep(1)
    try:
        messages = await client.get_messages(entity, limit=20)
    except Exception:
        messages = []
    forced = False
    join_link = None
    for msg in messages:
        text = msg.message or ""
        if ("برای ارسال پیام" in text or "عضو شوید" in text):
            forced = True
        if hasattr(msg.sender, "username") and msg.sender.username:
            if msg.sender.username.lower() == "digianti2bot":
                forced = True
        if msg.reply_markup and msg.reply_markup.rows:
            for row in msg.reply_markup.rows:
                for btn in row.buttons:
                    if btn.url:
                        join_link = btn.url
                        break
                if join_link:
                    break
        if forced and join_link:
            break
    if forced and join_link:
        try:
            if "t.me/" in join_link:
                username = join_link.split("t.me/")[-1]
                await client(JoinChannelRequest(username))
            else:
                await client(JoinChannelRequest(join_link))
            await asyncio.sleep(1)
            await client.send_message(entity, "سلام")
            return (group["link"], True)
        except Exception as join_error:
            return (group["link"], False)
    else:
        return None
async def remove_blacklisted_groups_for_account(user_id: int, account_index: int, context):
    accounts = get_tapchi_list(user_id)
    if account_index < 0 or account_index >= len(accounts):
        return

    account = accounts[account_index]
    blacklist = account.get("blacklist", [])

    # Remove blacklist groups
    account["groups"] = [group for group in account.get("groups", []) if group not in blacklist]
    account.pop("blacklist", None)
    save_accounts(user_id, phone_list)

    # Notify user when done
    try:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ اکانت {account['phone']} آپدیت شد و گروه‌های لیمیت شده حذف شدند."
        )
    except Exception as e:
        logging.error(f"Error sending message: {e}")
#104        
async def start_identification(context: ContextTypes.DEFAULT_TYPE, user_id: int):
    overall_forced_groups_count = 0
    overall_banned_count = 0
    accounts = get_tapchi_list(user_id)

    for acc in accounts:
        await update_groups_from_telethon(user_id, acc)

        session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{acc['phone']}")
        lock = get_session_lock(session_path)

        async with lock:
            client = TelegramClient(session_path, API_ID, API_HASH)

            if not await safe_connect(client, acc, user_id, context):
                continue

            if not await client.is_user_authorized():
                continue

#            spambot_ok = await check_spambot_for_account(client, user_id, context)
#            if not spambot_ok:
#                await context.bot.send_message(
#                    chat_id=user_id,
#                    text=f"⚠️ اکانت {acc['phone']} محدود شده و عملیات عضویت اجباری برای آن اجرا نخواهد شد."
#                )
#                try:
#                    await client.disconnect()
#                except Exception:
#                    pass
#                continue

            forced_groups_count = 0
            banned_count = 0

            for group in acc.get("groups", []):
                try:
                    entity = await client.get_entity(group["id"])

                    # Step 1: Send first message
                    sent_msg = await client.send_message(entity, "سلام")
                    await asyncio.sleep(2)

                    # Step 2: Try to fetch it again
                    check_msg = await client.get_messages(entity, ids=sent_msg.id)
                    if check_msg:
                        # Message still exists => no forced join needed
                        continue

                    # Step 3: Try to detect join button
                    messages = await client.get_messages(entity, limit=20)
                    join_link = None
                    for msg in messages:
                        if msg.reply_markup and msg.reply_markup.rows:
                            for row in msg.reply_markup.rows:
                                for btn in row.buttons:
                                    if btn.url and "t.me/" in btn.url:
                                        join_link = btn.url
                                        break
                                if join_link:
                                    break
                        if join_link:
                            break

                    if join_link:
                        try:
                            username = join_link.split("t.me/")[-1]
                            await client(JoinChannelRequest(username))
                            await asyncio.sleep(2)
                            await client.send_message(entity, "سلام")

                            forced_groups_count += 1
                            overall_forced_groups_count += 1

                            await context.bot.send_message(
                                chat_id=user_id,
                                text=(f"♻️ گزارش عضویت اجباری:\n"
                                      f"اکانت: {acc['phone']}\n"
                                      f"گروه: {group['link']}\n\n"
                                      "عضویت اجباری تکمیل شد و از این به بعد می‌توانید در این گروه پیام ارسال کنید ✅️")
                            )
                        except Exception as join_error:
                            error_text = str(join_error).lower()
                            if "can't send message" in error_text and "admin" in error_text:
                                banned_count += 1
                                overall_banned_count += 1
                        await asyncio.sleep(5)

                except Exception:
                    continue

            await context.bot.send_message(
                chat_id=user_id,
                text=(f"شناسایی عضویت اجباری برای اکانت {acc['phone']} تکمیل شد.\n"
                      f"از این به بعد می‌توانید در {forced_groups_count} گروه پیام ارسال کنید.\n"
                      f"تعداد گروه‌هایی که اکانت شمارو بن کردند: {banned_count}")
            )

            try:
                await client.disconnect()
            except Exception:
                pass

    await context.bot.send_message(
        chat_id=user_id,
        text=(f"عملیات عضویت اجباری برای گروه‌ها به اتمام رسید ✅️\n"
              f"تعداد کل گروه‌هایی که از این پس می‌توانید پیام ارسال کنید: {overall_forced_groups_count}\n"
              f"تعداد کل گروه‌هایی که اکانت‌ها بن شدند: {overall_banned_count}")
    )  







async def balance_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
            
    if len(context.args) < 1:
        await update.message.reply_text("Usage: /balance <user_id>")
        return
    try:
        user_id = context.args[0]
        bal = user_balances.get(str(user_id), 0)
        await update.message.reply_text(f"Balance for {user_id}: {bal}")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")
        
        
        

async def charge_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != ADMIN_ID:
        await update.message.reply_text("دسترسی غیرمجاز!")
        return
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /charge <user_id> <amount>")
        return
    try:
        user_id = context.args[0]
        amount = int(context.args[1])
        add_balance(int(user_id), amount)
        new_bal = get_balance(int(user_id))
        await update.message.reply_text(f"New balance for {user_id} => {new_bal}T")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")        
    
#103    
async def distribute_photos_to_accounts(user_id, photo_paths, context):
    debug_photo(f"Starting distribute_photos_to_accounts for user {user_id}")
    accounts = get_tapchi_list(user_id)
    if not accounts:
        await context.bot.send_message(user_id, "هیچ اکانتی برای شما ثبت نشده است.")
        debug_photo("No accounts found for user.")
        return

    chunk_size = max(1, math.ceil(len(photo_paths) / len(accounts)))
    chunks = [photo_paths[i:i + chunk_size] for i in range(0, len(photo_paths), chunk_size)]
    debug_photo(f"Chunked {len(photo_paths)} photos into {len(chunks)} chunks of size ~{chunk_size}")

    for idx, acc in enumerate(accounts):
        if idx >= len(chunks):
            debug_photo(f"No photo chunk for index {idx}, skipping...")
            break

        phone = acc.get("phone")
        session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
        lock = get_session_lock(session_path)

        debug_photo(f"Waiting for lock on session: {session_path}")
        async with lock:
            debug_photo(f"Lock acquired for: {phone}")
            client = TelegramClient(session_path, API_ID, API_HASH)

            if await safe_connect(client, acc, user_id, context):
                debug_photo(f"Connected to client for: {phone}")
                try:
                    for photo in chunks[idx]:
                        debug_photo(f"Processing photo: {photo}")
                        try:
                            with open(photo, "rb") as f:
                                input_file = await asyncio.wait_for(
                                    client.upload_file(f), timeout=15
                                )
                            debug_photo("Uploaded photo successfully")

                            await asyncio.wait_for(
                                client(UploadProfilePhotoRequest(file=input_file)), timeout=15
                            )
                            debug_photo(f"Updated profile photo for: {phone}")

                            await asyncio.sleep(2)

                        except asyncio.TimeoutError:
                            logging.warning(f"[PHOTO TIMEOUT] {phone} -> Timeout during photo: {photo}")
                            debug_photo(f"Timeout on photo: {photo}")
                        except Exception as e_photo:
                            logging.warning(f"[PHOTO UPLOAD FAIL] {phone} -> {e_photo}")
                            debug_photo(f"Upload failed for {photo}: {e_photo}")

                except Exception as e:
                    logging.warning(f"[PHOTO FAIL] {phone} -> {e}")
                    debug_photo(f"General failure for {phone}: {e}")

                finally:
                    try:
                        await client.disconnect()
                        debug_photo(f"Disconnected client for: {phone}")
                    except:
                        debug_photo(f"Error during disconnect for: {phone}")

    debug_photo("Finished processing all accounts.")
    await context.bot.send_message(user_id, "عکس‌های شما ذخیره شدند و در حال تنظیم برای اکانت‌ها هستند✅️")
    
async def end_trial_job(context: ContextTypes.DEFAULT_TYPE):
    user_id = context.job.name.split("_")[1]
    user_id = int(user_id)

    subs = user_subscriptions.get(str(user_id), {})
    if subs.get("is_trial"):
        del user_subscriptions[str(user_id)]
        save_subscriptions()
        await context.bot.send_message(
            chat_id=context.job.chat_id,
            text="تپچی تست شما تمام شد❌️\nبرای کار با ادامه با ربات باید اشتراک تپچی خریداری کنید\nبرای خرید اشتراک در صفحه اصلی روی خرید اشتراک بزنید."
        )    
        
# Global tracker (place this at the top of your script)
active_clock_updaters = set()

async def clock_updater(acc, user_id):
    if not is_subscription_valid(user_id):
        debug_clock(f"[{acc.get('phone', '?')}] No active subscription — skipping clock update.")
        return
    phone = acc.get("phone")
    debug_clock(f"START clock_updater for {phone}")

    if not phone:
        logging.warning(f"[CLOCK] No phone found in account data")
        debug_clock(f"[ABORT] No phone in account")
        return
#@@@
    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
    loggin_debug(f"Using session path for clock updater: {session_path}")
#@@@    
    clock_fonts = [
        ["𝟎","𝟏","𝟐","𝟑","𝟒","𝟓","𝟔","𝟕","𝟖","𝟗"], ["𝟘","𝟙","𝟚","𝟛","𝟜","𝟝","𝟞","𝟟","𝟠","𝟡"], ["𝟎","𝟏","𝟐","𝟑","𝟒","𝟓","𝟔","𝟕","𝟖","𝟗"],
        ["⁰","¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹"], ["₀","₁","₂","₃","₄","₅","₆","₇","₈","₉"], ["𝟎","𝟏","𝟐","𝟑","𝟒","𝟓","𝟔","𝟕","𝟖","𝟗"],
        ["𝟎","𝟏","𝟐","𝟑","𝟒","𝟓","𝟔","𝟕","𝟖","𝟗"], ["𝟎","𝟏","𝟐","𝟑","𝟒","𝟓","𝟔","𝟕","𝟖","𝟗"], ["𝟘","𝟙","𝟚","𝟛","𝟜","𝟝","𝟞","𝟟","𝟠","𝟡"],
        ["⁰","¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹"], ["𝟎","𝟏","𝟐","𝟑","𝟒","𝟓","𝟔","𝟕","𝟖","𝟗"], ["𝟘","𝟙","𝟚","𝟛","𝟜","𝟝","𝟞","𝟟","𝟠","𝟡"],
        ["𝟎","𝟏","𝟐","𝟑","𝟒","𝟓","𝟔","𝟕","𝟖","𝟗"], ["𝟎","𝟏","𝟐","𝟑","𝟒","𝟓","𝟔","𝟕","𝟖","𝟗"], 
["₀","₁","₂","₃","₄","₅","₆","₇","₈","₉"],

        ["⁰","¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹"], ["𝟎","𝟏","𝟐","𝟑","𝟒","𝟓","𝟔","𝟕","𝟖","𝟗"], ["𝟘","𝟙","𝟚","𝟛","𝟜","𝟝","𝟞","𝟟","𝟠","𝟡"],
        ["⓪","①","②","③","④","⑤","⑥","⑦","⑧","⑨"],
        
        ["⓿","➊","➋","➌","➍","➎","➏","➐","➑","➒"],
        
        ["０","１","２","３","４","５","６","７","８","９"],
        
        ["ʘ","❶","２","３","４","❺","❻","❼","➇","９"],
        
        ["⦅0⦆","⦅1⦆","⦅2⦆","⦅3⦆","⦅4⦆","⦅5⦆","⦅6⦆","⦅7⦆","⦅8⦆","⦅9⦆"],
        
        ["0̶","1̶","2̶","3̶","4̶","5̶","6̶","7̶","8̶","9̶"],
        
        ["『0』","『1』","『2』","『3』","『4』","『5』","『6』","『7』","『8』","『9』"],
        
        ["【0】","【1】","【2】","【3】","【4】","【5】","【6】","【7】","【8】","【9】"],
        
        ["Ѳ","❶","❷","３","❹","５","６","❼","➇","➈"]
        
        
    ]

    wrappers = [
        ("", ""), ("", ""), ("", ""), ("", ""), ("", ""),
        ("【", "】"), ("✧", "✧"), ("《", "》"), ("꧁", "꧂"), ("꧁", "꧂"),
        ("✧【", "】✧"), ("✧", "✧"), ("༺", "༻"), ("[★", "★]"), ("𓆩", "𓆪"),
        ("《", "》"), ("•̩̩͙ ", " •̩̩͙"), ("【", "】"),("", ""), ("", ""), ("", ""), ("", ""), ("", ""),("","")
    ]

    while acc.get("clock_enabled", False):
        lock = get_session_lock(session_path)

        async with lock:
            debug_clock("Acquired lock for clock update")

            client = TelegramClient(session_path, API_ID, API_HASH)
#16
            if not os.path.exists(session_path + ".session"):
                error_debug(f"[CLOCK] Session file missing for {phone} — skipping.")
                return

            await client.connect()

            if not await client.is_user_authorized():
                await client.disconnect()
                debug_clock("Client not authorized")
                continue

            await client.get_me()
            client.session.auto_save = False

            debug_clock("Attempting safe_connect()")
            if not await safe_connect(client, acc, user_id, context=None):
                debug_clock("safe_connect() failed")
                await client.disconnect()
                continue

            debug_clock("Connected successfully")
#@@@
            try:
                # Read from clock_state.json every minute
                try:
                    with open("data/clock_state.json", "r", encoding="utf-8") as f:
                        clock_state = json.load(f)
                    user_state = clock_state.get(str(user_id), {})
                    phone_state = user_state.get(phone, {})
                    status = phone_state.get("status", "off")
                    font_index = phone_state.get("clock_font", 0)
                    debug_clock(f"Loaded from clock_state.json: font={font_index}, status={status}")
                except Exception as e:
                    debug_clock(f"Error reading clock_state.json for {phone}: {e}")
                    status = "off"
                    font_index = 0

                if status != "on":
                    debug_clock(f"[CLOCK] Clock is OFF in clock_state.json for {phone}. Skipping update.")
                    break

                font_index = max(0, min(font_index, len(clock_fonts) - 1))
                debug_clock(f"Clock font index: {font_index}")

                tehran = pytz.timezone("Asia/Tehran")
                now = datetime.now(tehran)
                time_str = now.strftime("%H:%M")
                debug_clock(f"Current time: {time_str}")
#@@@
                digits = clock_fonts[font_index]
                if isinstance(digits, str):
                    # Regular case: 10 single Unicode characters
                    digit_map = str.maketrans("0123456789", digits)
                    translated_time = time_str.translate(digit_map)
                else:
                    # Wrapped/multi-character font case: list of strings
                    translated_time = ''.join(digits[int(c)] if c.isdigit() else c for c in time_str)

                # SAFE WRAPPER selection
                wrapper_index = font_index % len(wrappers)
                left, right = wrappers[wrapper_index]

                final_time = f"{left}{translated_time}{right}"
                debug_clock(f"Final clock string: {final_time}")

                if not await client.is_user_authorized():
                    logging.warning(f"[CLOCK LOGIN FAIL] {phone} is not authorized")
                    debug_clock(f"Client not authorized. Exiting loop for {phone}")
                    await client.disconnect()
                    break
# Get current user info
                me = await client.get_me()
                if not me:
                    logging.warning(f"[CLOCK FAIL] get_me() returned None for {phone}")
                    debug_clock("get_me() returned None. Aborting.")
                    await client.disconnect()
                    break

                debug_clock(f"Current name -> First: '{me.first_name}' | Last: '{me.last_name}'")

                # Prepare names
                first_name = me.first_name or phone
                current_last = (me.last_name or "").strip()

                # Only update if time has changed
                if current_last != final_time:
                    await client(UpdateProfileRequest(first_name=first_name, last_name=final_time))
                    debug_clock(f"Profile updated for {phone}")
                else:
                    debug_clock(f"No update needed for {phone} — already set")

                phone_list = get_tapchi_list(user_id)
                for i, a in enumerate(phone_list):
                    if a.get("phone") == phone:
                        phone_list[i] = acc
                        break
                save_accounts(user_id, phone_list)
                debug_clock("Account saved")

            except Exception as e:
                logging.warning(f"[CLOCK NAME FAIL] {phone} -> {e}")
                error_debug(f"Exception in clock update: {e}")
#@@@
            finally:
                await client.disconnect()
                debug_clock(f"Disconnected client for {phone}")

# Sleep OUTSIDE the lock
        tehran = pytz.timezone("Asia/Tehran")
        next_minute = (datetime.now(tehran) + timedelta(minutes=1)).replace(second=0, microsecond=0)
        sleep_time = (next_minute - datetime.now(tehran)).total_seconds()
        debug_clock(f"Sleeping until next minute: {sleep_time:.2f}s")
        await asyncio.sleep(sleep_time)

#@@@ Final cleanup after while loop ends
    active_clock_updaters.discard(phone)
    debug_banner(f"[CLEANUP] Removed {phone} from active_clock_updaters")

from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler
from telethon import TelegramClient
from telethon.tl.types import Channel, User
import os

async def accounts_state_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    await query.answer()
    await query.message.edit_text("درحال بررسی آمار تمامی اکانت های شما...")

    accounts = get_tapchi_list(user_id)
    stats_text = ""

    for acc in accounts:
        phone = acc.get("phone")
        session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
        lock = get_session_lock(session_path)

        async with lock:
            debug_clock(f"[ACCOUNTS STATE] Lock acquired for {phone}")

            try:
                client = TelegramClient(session_path, API_ID, API_HASH)
#17
                await client.connect()

                if not await client.is_user_authorized():
                    debug_clock(f"[ACCOUNTS STATE] {phone} not authorized. Skipping.")
                    await client.disconnect()
                    continue

                await client.get_me()

                dialogs = await client.get_dialogs()

                group_count = sum(1 for d in dialogs if isinstance(d.entity, Channel) and d.entity.megagroup)
                channel_count = sum(1 for d in dialogs if isinstance(d.entity, Channel) and d.entity.broadcast)
                private_count = sum(1 for d in dialogs if isinstance(d.entity, User))

                stats_text += f"""اکانت: {phone}
تعداد گروه ها: {group_count}
تعداد کانال ها: {channel_count}
تعداد پیوی ها: {private_count}
~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"""

                await client.disconnect()

            except Exception as e:
                debug_clock(f"[ACCOUNTS STATE] Error for {phone}: {e}")
                stats_text += f"""اکانت: {phone}
خطا در اتصال یا خواندن اطلاعات
~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"""

    if not stats_text:
        stats_text = "هیچ اکانتی یافت نشد یا قابل بررسی نبود."

    await query.message.edit_text(stats_text[:4096])




async def run_linkdoni_extraction(user_id, phone, link, count, context, chat_id):
    session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
    lock = get_session_lock(session_path)
    collected_links = set()

    async with lock:
        client = TelegramClient(session_path, API_ID, API_HASH)
#18
        await client.connect()

        if not await client.is_user_authorized():
            await context.bot.send_message(chat_id, f"{phone}: ❌ نشست غیرمجاز است.")
            await client.disconnect()
            return

        await client.get_me()

#@@@
        try:
            entity = await client.get_entity(link)
            offset_id = 0
            total_msgs = 0
            while len(collected_links) < count and total_msgs < 10000:
                history = await client(GetHistoryRequest(
                    peer=entity,
                    offset_id=offset_id,
                    offset_date=None,
                    add_offset=0,
                    limit=100,
                    max_id=0,
                    min_id=0,
                    hash=0
                ))
                messages = history.messages
                if not messages:
                    break
                for msg in messages:
                    if msg.message:
                        found = re.findall(r'(https?://t\.me/\S+|@[\w\d_]+)', msg.message)
                        for l in found:
                            if len(collected_links) >= count:
                                break
#@@@
                            if l.startswith("http"):
                                collected_links.add(l)
                offset_id = messages[-1].id
                total_msgs += len(messages)

        except Exception as e:
            await context.bot.send_message(chat_id, f"{phone}: ❌ خطا در استخراج لینک‌ها: {e}")
            await client.disconnect()
            return

        await client.disconnect()

    # Handle case: no links found
    if not collected_links:
        await context.bot.send_message(chat_id, f"{phone}: ⚠️ هیچ لینکی پیدا نشد.")
        return

    # Save to .txt
    file_path = f"/tmp/group_links_{user_id}.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"Amount: {len(collected_links)}\n")
        for i, link in enumerate(collected_links, 1):
            f.write(f"{i}: {link}\n")

    # Send the file
    with open(file_path, "rb") as f:
        await context.bot.send_document(
            chat_id=chat_id,
            document=f,
            filename="group_links.txt",
            caption="استخراج لینک از لینکدونی با موفقیت انجام شد✅️\n"
                    "🔰میتونید این فایل رو به بخش عضو شدن در گروه ها بدید..."
        )

    # Optionally clean up the file
    # os.remove(file_path)    
                
#102             
async def update_name_for_accounts(user_id, names, context):
    debug_clock(f"Starting update_name_for_accounts for user_id: {user_id}")
    accounts = get_tapchi_list(user_id)
    debug_clock(f"Loaded {len(accounts)} accounts from DB")

    for i, acc in enumerate(accounts):
        if i >= len(names):
            debug_clock(f"No more names to assign. Breaking loop at index {i}")
            break

        name = names[i]
        debug_clock(f"Target name [{i}]: {name}")

        first, *rest = name.split(" ", 1)
        first_name = first
        debug_clock(f"Split first name: '{first_name}'")

        session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{acc['phone']}")
        debug_clock(f"Session path resolved: {session_path}")

        lock = get_session_lock(session_path)
        async with lock:
            client = TelegramClient(session_path, API_ID, API_HASH)
            debug_clock(f"Client created for {acc['phone']}")

            if await safe_connect(client, acc, user_id, context):
                debug_clock(f"Safe connect success for {acc['phone']}")
                try:
                    me = await client.get_me()
                    if me is None:
                        debug_clock(f"Could not fetch profile for {acc['phone']}, skipping...")
                        continue

                    current_last_name = me.last_name or ""
                    debug_clock(f"Current last name for {acc['phone']}: '{current_last_name}'")

                    await client(UpdateProfileRequest(
                        first_name=first_name,
                        last_name=current_last_name  # Keep old last name untouched
                    ))

                    debug_clock(f"Successfully updated first name for {acc['phone']}")

                    await asyncio.sleep(1)

                except Exception as e:
                    logging.warning(f"[NAME FAIL] {acc['phone']} -> {e}")
                    debug_clock(f"Exception during name update for {acc['phone']}: {e}")

                finally:
                    await client.disconnect()
                    debug_clock(f"Client disconnected for {acc['phone']}")
            else:
                debug_clock(f"Safe connect failed for {acc['phone']}")

    debug_clock("Completed update_name_for_accounts")
    
#101         
async def update_bio_for_accounts(user_id, new_bio, context):
    accounts = get_tapchi_list(user_id)
    for acc in accounts:
        phone = acc.get("phone")
        if not phone:
            continue

        session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
        lock = get_session_lock(session_path)

        async with lock:
            client = TelegramClient(session_path, API_ID, API_HASH)
            if await safe_connect(client, acc, user_id, context):
                try:
                    await client(UpdateProfileRequest(about=new_bio))
                    await asyncio.sleep(1)
                except Exception as e:
                    logging.warning(f"[BIO FAIL] {phone} -> {e}")
                finally:
                    await client.disconnect()
                        
async def handle_text_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
            
    if context.user_data.get("profile_photos") and update.message.text.lower().strip() in ["تمام", "اتمام", "پایان"]:
        await update.message.reply_text("عکس‌های شما ذخیره شد و به زودی به تمامی اکانت‌های شما ارسال می‌شود ✅️")
        
        # Distribute to accounts
        await distribute_photos_to_accounts(update.message.from_user.id, context.user_data["profile_photos"], context)
        
        # ✅ CLEANUP FLAGS
        context.user_data.pop("profile_photos", None)
        context.user_data.pop("awaiting_multi_photos", None)
        context.user_data.pop("gm_edit_photo", None)  # optional

        return  # <-- this is important to stop further fallthrough
        

#async def handle_photo_upload(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    
#            
#    if not update.message.photo:
#        return await update.message.reply_text("عکس پیدا نشد.")

#    # Get the highest resolution photo
#    photo_file = await update.message.photo[-1].get_file()

#    # Generate a unique filename
#    photo_id = f"{uuid.uuid4()}.jpg"
#    save_dir = "data/photos/uploaded"
#    os.makedirs(save_dir, exist_ok=True)
#    save_path = os.path.join(save_dir, photo_id)

#    # Save the photo to disk
#    await photo_file.download_to_drive(save_path)

#    # Store the full path for later use
#    context.user_data.setdefault("profile_photos", []).append(save_path)
#@@@
#    await update.message.reply_text(
#        "عکس دریافت شد، می‌تونید عکس‌های بیشتری ارسال کنید یا بنویسید  [ تمام ]  برای اعمال."
#    )
                
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def handle_photo_upload(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if we're actually expecting a photo
    if not context.user_data.get("awaiting_multi_photos") and not context.user_data.get("gm_edit_photo"):
        # User sent a photo without being in photo upload mode - just ignore
        return
        
    if not update.message.photo:
        return await update.message.reply_text("عکس پیدا نشد.")

    # Save photo
    photo_file = await update.message.photo[-1].get_file()
    photo_id = f"{uuid.uuid4()}.jpg"
    save_dir = "data/photos/uploaded"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, photo_id)
    await photo_file.download_to_drive(save_path)

    # Store path
    context.user_data.setdefault("profile_photos", []).append(save_path)
    photo_count = len(context.user_data["profile_photos"])

    # Prepare inline keyboard
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅️همین کافیه شروعش کن", callback_data="start_processing_photos")],
        [InlineKeyboardButton("⛔️لغو", callback_data="cancel_photo_upload")]
    ])

    await update.message.reply_text(f"📲 تعداد عکس دریافتی: {photo_count}\n\nمی‌توانید عکس‌های بیشتری ارسال کنید یا با دکمه‌های زیر ادامه دهید.", reply_markup=keyboard)
    
 
         
async def unified_text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip() if update.message.text else ""
    # ... your logic follows

# ✅ Handle 'تمام شد' for photo uploads
    if context.user_data.get("awaiting_multi_photos") and text.lower() in ["تمام", "اتمام", "پایان"]:
        await update.message.reply_text("عکس‌های شما ذخیره شد و به زودی به تمامی اکانت‌های شما ارسال می‌شود ✅️")
        await distribute_photos_to_accounts(update.message.from_user.id, context.user_data["profile_photos"], context)

        # Clean up
        context.user_data.pop("profile_photos", None)
        context.user_data.pop("awaiting_multi_photos", None)
        context.user_data.pop("gm_edit_photo", None)
        return

# Existing: handle name editing
    if context.user_data.get("awaiting_edit_name"):
        names = [line.split(":", 1)[1].strip() for line in text.splitlines() if ":" in line]
        context.user_data["new_names"] = names
        context.user_data["awaiting_edit_name"] = False

        preview = "\n".join([f"{i+1}: {name}" for i, name in enumerate(names)])
        await update.message.reply_text(
            f"نام‌های انتخابی شما:\n{preview}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ثبت نام‌ها ✅️", callback_data="gm_confirm_edit_name")],
                [InlineKeyboardButton("↩️بازگشت↩️", callback_data="gm_back")]
            ])
        )
        return

# Existing: handle bio editing
    if context.user_data.get("awaiting_edit_bio"):
        
                    
        bio = text
        context.user_data["new_bio"] = bio
        context.user_data["awaiting_edit_bio"] = False

        await update.message.reply_text(
            f"بیو انتخابی شما:\n{bio}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ثبت بیو ✅️", callback_data="gm_confirm_edit_bio")],
                [InlineKeyboardButton("↩️بازگشت↩️", callback_data="gm_back")]
            ])
        )
        return

    if context.user_data.get("profile_photos"):
        
                    
        if text.lower() in ["تمام", "اتمام", "پایان"]:
            context.user_data["awaiting_multi_photos"] = False
            await update.message.reply_text("عکس‌های شما ذخیره شد و به زودی به تمامی اکانت‌های شما ارسال می‌شود ✅️")
            await distribute_photos_to_accounts(update.message.from_user.id, context.user_data["profile_photos"], context)
            return
        return await handle_text_input(update, context)

    # fallback
    return await main_text_handler(update, context)
    
async def handle_pv_message_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id  # must be defined first!

    if not is_subscription_valid(user_id):
        await context.bot.send_message(chat_id=user_id, text="⛔️ شما اشتراکی ندارید")
        return    

    if not context.user_data.get("awaiting_pv_broadcast"):
        return  # Not in PV message mode

    text = update.message.text

    if "pv_broadcast_messages" not in context.user_data:
        context.user_data["pv_broadcast_messages"] = []

    messages = context.user_data["pv_broadcast_messages"]

    if len(messages) >= 5:
        await update.message.reply_text("❗️ حداکثر ۵ پیام می‌تونی ثبت کنی.")
        return

    messages.append(text)

    msg_count = len(messages)
    preview = f"پیام {msg_count} شما:\n{text}"

    buttons = []
    if msg_count < 5:
        buttons.append([InlineKeyboardButton("✏️ ثبت پیام بعدی", callback_data="gm_add_next_pv")])

    buttons.append([InlineKeyboardButton("✅️ همین بسه، ارسالش کن", callback_data="gm_send_pv_now")])
    buttons.append([InlineKeyboardButton("↩️ بازگشت", callback_data="gm_broadcast_pv")])

    await update.message.reply_text(preview, reply_markup=InlineKeyboardMarkup(buttons))
                              
async def conditional_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):    
    user_id = update.effective_user.id
    
    # Add a command to reset all states if user gets stuck
    if update.message and update.message.text and update.message.text.strip().lower() == "/reset":
        clear_user_flags(context)
        await update.message.reply_text("🔄 تمام حالت‌های ربات ریست شد. می‌توانید از ابتدا شروع کنید.")
        return
    
    # Check if this is admin input
    if await handle_admin_text_input(update, context):
        return
    
    # Check maintenance mode (except for admin)
    if context.bot_data.get("maintenance_mode", False) and user_id != 7135477742:
        await update.message.reply_text(
            "🔧 ربات در حال تعمیر است. لطفاً بعداً تلاش کنید.",
            parse_mode="HTML"
        )
        return
        
    if context.user_data.get("awaiting_pv_broadcast"):
        await handle_pv_message_input(update, context)
    else:
        await unified_text_handler(update, context)        

# This must be defined BEFORE it's used
#auto_reply_launcher

async def start_auto_reply_for_all_clients():
    fix_debug("[AUTO-REPLY] reached start_auto_reply_for_all_clients ")
#@@@
    session_dir = SESSION_DIR  # This uses the actual configured path
    if not os.path.exists(session_dir):
        fix_debug("[AUTO-REPLY] Session directory missing.")
        return

    for fname in os.listdir(session_dir):
        if not fname.startswith("session_") or not fname.endswith(".session"):
            continue

        parts = fname[len("session_"):].rsplit("_", 1)
        if len(parts) != 2:
            continue

        try:
            user_id = int(parts[0])
            phone = parts[1].rsplit(".session", 1)[0]
            session_path = os.path.join(session_dir, f"session_{user_id}_{phone}")
            lock = get_session_lock(session_path)

            accounts = get_tapchi_list(user_id)
            acc = next((a for a in accounts if a.get("phone") == phone), None)
            if not acc:
                continue
#@@@
            auto_reply_enabled = is_auto_reply_enabled_for_account(user_id, phone)

            # If task exists and is running but auto-reply is disabled, cancel it
            if not auto_reply_enabled:
                if phone in auto_reply_tasks and not auto_reply_tasks[phone].done():
                    fix_debug(f"[AUTO-REPLY] Stopping {phone}, user disabled auto-reply")
                    auto_reply_tasks[phone].cancel()
                    auto_reply_tasks.pop(phone, None)
                else:
                    fix_debug(f"[AUTO-REPLY] Skipped {phone}, auto-reply disabled for user {user_id}")
                continue

#@@@ Always restart the auto-reply task to ensure fresh state
            if phone in auto_reply_tasks:
                if not auto_reply_tasks[phone].done():
                    fix_debug(f"[AUTO-REPLY] Cancelling existing task for {phone}")
                    auto_reply_tasks[phone].cancel()
                    try:
                        await auto_reply_tasks[phone]  # Wait for cleanup
                        fix_debug(f"[AUTO-REPLY] Task finished cleanly for {phone}")
                    except asyncio.CancelledError:
                        fix_debug(f"[AUTO-REPLY] Task was cancelled for {phone}")
                    except Exception as e:
                        fix_debug(f"[AUTO-REPLY] Error while waiting for task to finish: {e}")
                auto_reply_tasks.pop(phone, None)
                await asyncio.sleep(5)

            # Start it fresh if not locked
            if not lock.locked():
                registered_clients.pop(phone, None)
                task = asyncio.create_task(start_auto_reply_for_user(acc, user_id))
                auto_reply_tasks[phone] = task
                fix_debug(f"[AUTO-REPLY] Started for {phone}")
            else:
                fix_debug(f"[AUTO-REPLY] Skipped {phone}, lock is held")

        except Exception as e:
            fix_debug(f"[AUTO-REPLY] Error processing {fname}: {e}")
                                                                                   
            
import os
import json
import asyncio

async def start_clock_for_all_users():
    debug_clock("[CLOCK] === Starting clock updater for enabled accounts ===")

    started_count = 0

    CLOCK_STATE_FILE = os.path.join("data", "clock_state.json")

    try:
        with open(CLOCK_STATE_FILE, "r", encoding="utf-8") as f:
            state_data = json.load(f)
        debug_clock(f"[CLOCK] Loaded clock_state.json with {len(state_data)} users")
    except FileNotFoundError:
        debug_clock(f"[CLOCK] ERROR: {CLOCK_STATE_FILE} not found.")
        return
    except Exception as e:
        debug_clock(f"[CLOCK] ERROR reading {CLOCK_STATE_FILE}: {e}")
        return

    for user_id_str, phones in state_data.items():
        user_id = int(user_id_str)
        try:
            user_accounts = get_tapchi_list(user_id)
            debug_clock(f"[CLOCK] Checking user {user_id} with {len(phones)} phones")
        except Exception as e:
            debug_clock(f"[CLOCK] ERROR loading accounts for user {user_id}: {e}")
            continue

        for phone, phone_state in phones.items():
            status = phone_state.get("status", "off")
            debug_clock(f"[CLOCK] - {phone} status = {status}")

            if status != "on":
                continue

            acc = next((a for a in user_accounts if str(a.get("phone")) == phone), None)
            if not acc:
                debug_clock(f"[CLOCK] WARNING: No matching account found for {phone}")
                continue
#@@@
            if phone not in active_phones:
                debug_clock(f"[CLOCK] Launching updater for {phone}")
                asyncio.create_task(run_clock_resilient(acc, user_id))
                started_count += 1
            else:
                debug_clock(f"[CLOCK] Skipped already running updater for {phone}")

    if started_count == 0:
        debug_clock("[CLOCK] No valid accounts with status 'on' found.")
        
    else:
        debug_clock(f"[CLOCK] Successfully started clock for {started_count} account(s).")
        
  
        
              
                    
                          
                                
                                            
active_phones = set()

async def run_clock_resilient(acc, user_id):
    phone = acc.get("phone", "?")

    if not phone:
        debug_clock("[RESILIENT] No phone found in acc object")
        return

    if phone in active_phones:
        debug_clock(f"[RESILIENT] Skipping duplicate run for {phone}")
        return

    active_phones.add(phone)
    retry_count = 0

    try:
        while True:
            try:
                debug_clock(f"[RESILIENT] Starting clock_updater for {phone}")
                await clock_updater(acc, user_id)
                retry_count = 0  # Reset on success
            except asyncio.CancelledError:
                debug_clock(f"[RESILIENT] Task cancelled for {phone}")
                break
            except Exception as e:
                retry_count += 1
                logging.error(f"[CLOCK CRASH] {phone} -> {e} (retry {retry_count})")
                debug_clock(f"[CLOCK] {phone} has failed {retry_count} times")

                if retry_count >= 3:
                    debug_clock(f"[CLOCK] Too many failures for {phone}, disabling clock.")
                    disable_clock_in_json(user_id, phone)
                    break

                await asyncio.sleep(60)  # wait before retry
            else:
                # Normal loop exit
                break
    finally:
        active_phones.discard(phone)
        debug_clock(f"[RESILIENT] Removed {phone} from active_phones")

                    
                                     
                                                                                
clock_tasks = {}     

                            
async def restart_dead_clocks(context):
    try:
        with open("data/clock_state.json", "r", encoding="utf-8") as f:
            state_data = json.load(f)
    except Exception as e:
        debug_clock(f"[RESTART JOB] Failed to load clock_state.json: {e}")
        return

    for user_id_str, phones in state_data.items():
        user_id = int(user_id_str)
        accounts = get_tapchi_list(user_id)

        for phone, state in phones.items():
            if state.get("status") != "on":
                continue

            acc = next((a for a in accounts if a.get("phone") == phone), None)
            if not acc:
                continue

            if phone in active_phones:
                debug_clock(f"[RESTART JOB] Skipped — already running for {phone}")
                continue

            # Optional: cancel old dead task
            old_task = clock_tasks.get(phone)
            if old_task and not old_task.done():
                old_task.cancel()
                debug_clock(f"[RESTART JOB] Cancelled stale task for {phone}")

            task = asyncio.create_task(run_clock_resilient(acc, user_id))
            clock_tasks[phone] = task
            debug_clock(f"[RESTART JOB] Restarted task for {phone}")
                                
  
                    
                                                        
                    
def disable_clock_in_json(user_id, phone):
    CLOCK_STATE_FILE = os.path.join("data", "clock_state.json")

    try:
        with open(CLOCK_STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        logging.error(f"[CLOCK] Failed to load clock state file: {e}")
        return

    user_key = str(user_id)
    if user_key in data and phone in data[user_key]:
        data[user_key][phone]["status"] = "off"
        try:
            with open(CLOCK_STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            debug_clock(f"[CLOCK] Clock for {phone} disabled in clock_state.json")
        except Exception as e:
            logging.error(f"[CLOCK] Failed to write clock state: {e}")                       
                                        
                                                                                
# --- MONSHI LISTENER STARTUP ---


        
async def start_auto_reply_async():
    debug_monshi("[AUTO-REPLY INIT] Starting auto-reply for all clients...")
    await start_auto_reply_for_all_clients()
        
async def monshi_keepalive_job(context: ContextTypes.DEFAULT_TYPE):
    # Re-import to ensure latest logic is used dynamically
    try:
        # Re-activate auto-reply listeners for all enabled accounts
        await start_auto_reply_for_all_clients()
    except Exception as e:
        logging.error(f"Error in monshi_keepalive_job: {e}")
    
import logging
from telegram.ext import ApplicationBuilder, PicklePersistence, CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, ContextTypes, filters










def run_session(session_file: str):
    filename = os.path.basename(session_file)
    session_id = filename.replace(".session", "")

    if os.path.getsize(session_file) < 1024:  # Basic corruption check
        print(f"[{session_id}] Skipping corrupted or empty session.")
        return

    print(f"Session found: {session_file}")

    class TaggedWriter:
        def __init__(self, tag, stream):
            self.tag = tag
            self.stream = stream

        def write(self, message):
            if message.strip():
                self.stream.write(f"[{self.tag}] {message}")
            else:
                self.stream.write(message)

        def flush(self):
            self.stream.flush()

    sys.stdout = TaggedWriter(session_id, sys.__stdout__)
    sys.stderr = TaggedWriter(session_id, sys.__stderr__)

    # IMPORTANT: Use session name, not path
    client = TelegramClient(session_id, API_ID, API_HASH)
    client.session.save()  # Ensure the session is initialized and persisted

    async def session_main():
        try:
            await client.connect()
            if not await client.is_user_authorized():
                print("❌ Unauthorized session.")
                return

            me = await client.get_me()
            phone = me.phone if me.phone.startswith('+') else f'+{me.phone}'
            user_id = me.id

            print(f"✅ Session started for {phone} (user_id={user_id})")
            print("Parallel access started for this session")

            while True:
                await asyncio.sleep(3600)

        except Exception as e:
            print(f"❗ Error in session: {e}")
            traceback.print_exc()
        finally:
            await client.disconnect()

    try:
        asyncio.run(session_main())
    except Exception as e:
        print(f"❗ UNHANDLED ERROR in run_session: {e}")
        traceback.print_exc()

def launch_all_sessions():
    for file in os.listdir(SESSION_DIR):
        if file.endswith(".session") and not file.endswith(".session-journal"):
            session_path = os.path.join(SESSION_DIR, file)
            p = multiprocessing.Process(target=run_session, args=(session_path,))
            p.start()

def launch_all_sessions():
    for file in os.listdir(SESSION_DIR):
        if file.endswith(".session") and not file.endswith(".session-journal"):
            session_path = os.path.join(SESSION_DIR, file)
            p = multiprocessing.Process(target=run_session, args=(session_path,))
            p.start() 
#def launch_all_sessions():
#    for file in os.listdir(SESSION_DIR):
#        if file.endswith(".session") and not file.endswith(".session-journal"):
#            session_path = os.path.join(SESSION_DIR, file)
#            session_id = file.replace(".session", "")

#            log_dir = "/opt/vpsbot/logs"
#            os.makedirs(log_dir, exist_ok=True)  # <-- Create logs directory if it doesn't exist

#            log_file_path = os.path.join(log_dir, f"{session_id}.log")
#            log_file = open(log_file_path, "a")

#            def safe_run(path):
#                try:
#                    run_session(path)
#                except Exception as e:
#                    print(f"[{path}] ❗ FATAL: Could not launch session: {e}")
#                    import traceback
#                    traceback.print_exc()

#            p = multiprocessing.Process(
#                target=safe_run,
#                args=(session_path,),
#            )
#            p.daemon = False
#            p.start()

            
                        
                                    
                                                
                                                            
                                                                        
                                                                                    
                                                                                                
                                                                                                            
                                                                                                                        
                                                                                                                                    
                                                                                                                                                
                                                                                                                                                            
                                                                                                                                                                                    
##################################################################### SELF FUNCTIONS#######
######### SELF FUNCTIONS #######
######### SELF FUNCTIONS #######
######### SELF FUNCTIONS #######
######### SELF FUNCTIONS #######
######### SELF FUNCTIONS #######
######### SELF FUNCTIONS ####### ############################################################
########## SELF IMPORTS ########

from telegram.ext import MessageHandler, filters
from telethon import TelegramClient
from telegram import Update
from telegram.ext import ContextTypes
from telethon.tl.functions.contacts import ResolveUsernameRequest


########### DEBUGS ############

SELF_USER_ID_DEBUG = False

def debug_self_user_id(msg):
    if SELF_USER_ID_DEBUG:
        print(f"[SELF USER ID DEBUG] {msg}", flush=True)

async def username_lookup_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    match = re.search(r"Username\s+@(\w+)", text, re.IGNORECASE)
    if not match:
        debug_self_user_id("[HANDLER] No matching pattern found in message.")
        return

    username = match.group(1)
    user_id = update.message.from_user.id
    debug_self_user_id(f"[HANDLER] Extracted username: {username} from user: {user_id}")

    accounts = get_tapchi_list(user_id)
    if not accounts:
        debug_self_user_id("[HANDLER] No accounts found for this user.")
        await update.message.reply_text("⛔️ شما اکانتی متصل ندارید.")
        return

    for account in accounts:
        phone = account["phone"]
        session_path = os.path.join(SESSION_DIR, f"session_{user_id}_{phone}")
        debug_self_user_id(f"[SESSION] Trying session for phone: {phone} -> Path: {session_path}")

        lock = get_session_lock(session_path)

        async with lock:
            client = TelegramClient(session_path, API_ID, API_HASH)

            try:
                debug_self_user_id(f"[SESSION] Connecting client for {phone}")
                await client.connect()

                debug_self_user_id(f"[SESSION] Connected. Checking authorization for {phone}")
                is_auth = await client.is_user_authorized()
                debug_self_user_id(f"[SESSION] is_user_authorized() for {phone} returned: {is_auth}")

                me = None
                try:
                    me = await client.get_me()
                    debug_self_user_id(f"[SESSION] Initial get_me() returned: {me} for {phone}")
                except Exception as e:
                    debug_self_user_id(f"[SESSION] get_me() raised exception for {phone}: {e}")

                if me is None:
                    debug_self_user_id(f"[SESSION] get_me() is None. Trying get_dialogs() warm-up for {phone}")
                    try:
                        _ = await client.get_dialogs(limit=1)
                        me = await client.get_me()
                        debug_self_user_id(f"[SESSION] get_me() after warm-up: {me} for {phone}")
                    except Exception as warmup_error:
                        debug_self_user_id(f"[SESSION] Warm-up failed for {phone}: {warmup_error}")
                        await client.disconnect()
                        continue

                if me is None:
                    debug_self_user_id(f"[SESSION] Still no valid get_me() after warm-up. Skipping {phone}")
                    await client.disconnect()
                    continue

                debug_self_user_id(f"[SESSION] Connected as: {me.username or me.id} for {phone}")

                try:
                    debug_self_user_id(f"[LOOKUP] Resolving username with ResolveUsernameRequest: @{username}")
                    result = await client(ResolveUsernameRequest(username))
                    user_id_resolved = result.users[0].id
                    debug_self_user_id(f"[LOOKUP] Resolved ID: {user_id_resolved} for @{username}")
                    await update.message.reply_text(
                        f"*User ID:* `{user_id_resolved}`",
                        parse_mode="Markdown",
                        reply_to_message_id=update.message.message_id
                    )
                    await client.disconnect()
                    return  # ✅ Success

                except UsernameNotOccupiedError:
                    debug_self_user_id(f"[LOOKUP] Username @{username} does not exist.")
                    await client.disconnect()
                    continue

                except Exception as ee:
                    debug_self_user_id(f"[LOOKUP] Error resolving @{username} for {phone}: {ee}")
                    await client.disconnect()
                    continue

            except Exception as outer:
                debug_self_user_id(f"[ERROR] Connection error for {phone}: {outer}")
                try:
                    await client.disconnect()
                except Exception as dc_err:
                    debug_self_user_id(f"[ERROR] Disconnect failed for {phone}: {dc_err}")
                continue
#@@@
    debug_self_user_id(f"[FAILURE] All sessions failed to resolve @{username}")
    await update.message.reply_text(
        "*User ID not found ⛔*",
        parse_mode="Markdown",
        reply_to_message_id=update.message.message_id
    )


           
                      
                                 
                                            
                                                       
                                                                  
                                                                             
                                                                                        
                                                                                                   
############################################################ ###### END SELF FUNCTIONS ######
 ###### END SELF FUNCTIONS ######
 ###### END SELF FUNCTIONS ######
 ###### END SELF FUNCTIONS ######
 ###### END SELF FUNCTIONS ######
 ###### END SELF FUNCTIONS ######
 ###### END SELF FUNCTIONS ###### ############################################################                                                                                                                         
#async def on_startup(app):
#    try:
#        load_data_debug("Starting on_startup sequence...")

#        for i in range(5):
#            task = app.create_task(task_worker())
#            load_data_debug(f"task_worker {i+1} created")
#            task.add_done_callback(lambda t: load_data_debug(f"task_worker {i+1} exited: {t.exception()}"))

#        monitor = app.create_task(monitor_task_queue())
#        load_data_debug("monitor_task_queue task created")
#        monitor.add_done_callback(lambda t: load_data_debug(f"monitor_task_queue exited: {t.exception()}"))

#        # Schedule auto-reply task
#        def wrapper(ctx):
#            load_data_debug("Scheduling start_auto_reply_async()")
#            app.create_task(start_auto_reply_async())

#        app.job_queue.run_once(wrapper, when=1)

#        load_data_debug("on_startup sequence finished.")
#    except Exception as e:
#        load_data_debug(f"[FATAL ERROR in on_startup] {e}")
#        import traceback
#        traceback.print_exc()            
    




   

import asyncio
import psutil
import logging
from telegram import __version__  # Import necessary modules for the Telegram bot
from telegram.ext import ApplicationBuilder, CommandHandler, ConversationHandler
from telegram.ext import PicklePersistence
from telegram.ext import filters
import time

# Function to log memory usage
def log_memory_usage(stage=""):
    process = psutil.Process()  # Get current process
    mem_info = process.memory_info()
    rss = mem_info.rss / (1024 * 1024)  # Convert to MB
    vms = mem_info.vms / (1024 * 1024)  # Convert to MB
    memory_msg = f"[MEMORY] {stage} - RSS: {rss:.2f} MB, VMS: {vms:.2f} MB"
    print(memory_msg, flush=True)
    
    # Log to admin logs with glass-like design
    admin_log(f"حافظه: {rss:.2f} MB (RSS), {vms:.2f} MB (VMS) - {stage}", "INFO")

# Function to log memory usage every 30 seconds
async def log_memory_periodically():
    while True:
        log_memory_usage("Memory usage update")  # Log the memory usage every time
        await asyncio.sleep(30)  # Sleep for 30 seconds before logging again

# Your existing on_startup function with added memory tracking
async def on_startup(app):
    async def deferred_start():
        load_data_debug("[STARTUP] Deferring startup tasks...")
        log_memory_usage("Startup Begin")  # Log memory at startup
        
        # Initialize admin panel data
        app.bot_data["uptime"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.bot_data["daily_messages"] = 0
        app.bot_data["active_today"] = 0
        app.bot_data["new_today"] = 0
        app.bot_data["active_accounts"] = 0
        app.bot_data["limited_accounts"] = 0
        
        # Create admin logs directory
        os.makedirs("data/admin_logs", exist_ok=True)
        
        # Log startup with glass-like design
        admin_log("🚀 ربات تپچی با موفقیت راه‌اندازی شد", "INFO")

        for i in range(6):
            task = asyncio.create_task(task_worker())
            load_data_debug(f"[STARTUP] task_worker {i+1} started")
            admin_log(f"کارگر وظایف {i+1} راه‌اندازی شد", "INFO")

        log_memory_usage(f"After starting {i+1} tasks")  # Log memory after tasks

    asyncio.create_task(deferred_start())

    # Start logging memory usage every 30 seconds
    asyncio.create_task(log_memory_periodically())
# Your existing on_startup function with added memory tracking

# ==================== ZARINPAL PAYMENT HANDLERS ====================

async def handle_zarinpal_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle ZarinPal payment request"""
    query = update.callback_query
    user_id = query.from_user.id
    
    # Get pending subscription data
    pending = context.user_data.get("pending_subscription")
    if not pending:
        await query.answer("❌ اطلاعات خرید یافت نشد. لطفاً دوباره تلاش کنید.", show_alert=True)
        return
    
    allowed = pending["allowed"]
    price = pending["price"]
    duration = pending["duration"]
    
    try:
        # Prepare payment data
        amount = price  # Amount in Tomans
        description = f"خرید اشتراک تپچی {duration} روزه برای {allowed} اکانت"
        
        # Use bot's webhook URL for callback (you should set this to your actual domain)
        callback_url = f"https://your-domain.com/zarinpal_callback"  # Replace with your actual callback URL
        
        # Get user info for metadata
        user = query.from_user
        mobile = user.username if user.username else None
        email = None
        order_id = f"sub_{user_id}_{int(datetime.now().timestamp())}"
        
        # Create payment request
        success, result = zarinpal.create_payment_request(
            amount=amount,
            description=description,
            callback_url=callback_url,
            mobile=mobile,
            order_id=order_id
        )
        
        if success:
            authority = result.get("authority")
            payment_url = zarinpal.get_payment_url(authority)
            
            # Store pending payment data
            store_pending_payment(
                authority=authority,
                user_id=user_id,
                amount=amount,
                subscription_data={
                    "allowed": allowed,
                    "price": price,
                    "duration": duration
                }
            )
            
            # Show payment instructions
            payment_text = (
                "💳 <b>پرداخت آنلاین زرین‌پال</b>\n\n"
                f"📊 مبلغ قابل پرداخت: <code>{amount:,}</code> تومان\n"
                f"🔗 شناسه پرداخت: <code>{authority}</code>\n\n"
                "🚀 برای ادامه روی دکمه زیر کلیک کنید و به درگاه پرداخت منتقل شوید.\n\n"
                "⚠️ <b>توجه:</b> پس از پرداخت موفق، به همین بخش بازگردید و روی دکمه تأیید پرداخت کلیک کنید."
            )
            
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("💳 ورود به درگاه پرداخت", url=payment_url)],
                [InlineKeyboardButton("✅ تأیید پرداخت", callback_data=f"verify_zarinpal:{authority}")],
                [InlineKeyboardButton("↪️ بازگشت", callback_data="back_to_subscription")]
            ])
            
            await query.edit_message_text(payment_text, reply_markup=keyboard, parse_mode="HTML")
            
        else:
            error_code = result.get("errors", [{}])[0].get("code", -1) if result.get("errors") else -1
            error_message = zarinpal.format_error_message(error_code)
            
            await query.edit_message_text(
                f"❌ <b>خطا در ایجاد درخواست پرداخت</b>\n\n"
                f"📝 پیام خطا: {error_message}\n\n"
                "لطفاً دوباره تلاش کنید یا با پشتیبانی تماس بگیرید.",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("🔄 تلاش مجدد", callback_data="pay_zarinpal"),
                    InlineKeyboardButton("↪️ بازگشت", callback_data="back_to_subscription")
                ]]),
                parse_mode="HTML"
            )
            
    except Exception as e:
        logging.error(f"Error in ZarinPal payment request: {e}")
        await query.edit_message_text(
            "❌ <b>خطای سیستمی</b>\n\n"
            "متأسفانه خطایی در سیستم پرداخت رخ داده است.\n"
            "لطفاً چند دقیقه دیگر تلاش کنید.",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🔄 تلاش مجدد", callback_data="pay_zarinpal"),
                InlineKeyboardButton("↪️ بازگشت", callback_data="back_to_subscription")
            ]]),
            parse_mode="HTML"
        )

async def handle_zarinpal_verification(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle ZarinPal payment verification"""
    query = update.callback_query
    user_id = query.from_user.id
    
    # Extract authority from callback data
    authority = query.data.split(":")[-1]
    
    # Get pending payment data
    payment_data = get_pending_payment(authority)
    if not payment_data:
        await query.answer("❌ اطلاعات پرداخت یافت نشد.", show_alert=True)
        return
    
    if payment_data["user_id"] != user_id:
        await query.answer("❌ این پرداخت متعلق به شما نیست.", show_alert=True)
        return
    
    try:
        amount = payment_data["amount"]
        subscription_data = payment_data["subscription_data"]
        
        # Verify payment with ZarinPal
        success, result = zarinpal.verify_payment(amount, authority)
        
        if success:
            ref_id = result.get("ref_id")
            card_pan = result.get("card_pan", "نامشخص")
            
            # Check if this is an upgrade or regular subscription
            if subscription_data.get("type") == "upgrade":
                # Handle upgrade payment
                allowed = subscription_data["allowed"]
                final_price = subscription_data["final_price"]
                duration = subscription_data["duration"]
                current_sub = subscription_data["current_sub"]
                
                # Process upgrade similar to confirm_upgrade_subscription
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
                
                # Process like the original upgrade logic
                tehran = pytz.timezone("Asia/Tehran")
                now = datetime.now(tehran)
                for s in subs:
                    expiry = datetime.fromisoformat(s["expiry"])
                    if expiry.tzinfo is None:
                        expiry = tehran.localize(expiry)
                    else:
                        expiry = expiry.astimezone(tehran)
                    
                    if expiry > now:
                        # Cancel the old subscription by setting expiry to now
                        s["expiry"] = now.isoformat()
                        break
                
                # Add new subscription
                expiry = datetime.utcnow() + timedelta(days=duration)
                sub = {
                    "allowed_accounts": allowed,
                    "expiry": expiry.isoformat(),
                    "price": final_price,
                    "payment_method": "zarinpal",
                    "ref_id": ref_id,
                    "authority": authority
                }
                subs.append(sub)
                user_subscriptions[str(user_id)] = subs
                save_subscriptions()
                
                success_text = (
                    "🎉 <b>ارتقاء اشتراک موفق</b>\n\n"
                    f"✅ اشتراک {duration} روزه برای {allowed} اکانت با موفقیت ارتقاء یافت.\n"
                    f"💳 شماره تراکنش: <code>{ref_id}</code>\n"
                    f"🔢 کارت پرداخت: <code>{card_pan}</code>\n\n"
                    "🚀 اکنون می‌توانید از تمام ویژگی‌های پلن جدید استفاده کنید."
                )
                
                # Log successful upgrade payment
                admin_log(f"ZarinPal upgrade payment successful: User {user_id}, Amount {amount}, RefID {ref_id}", "INFO")
                
            else:
                # Handle regular subscription payment
                allowed = subscription_data["allowed"]
                price = subscription_data["price"]
                duration = subscription_data["duration"]
                
                # Add subscription
                subs = user_subscriptions.get(str(user_id), [])
                if isinstance(subs, dict):
                    subs = [subs]
                    
                expiry = datetime.utcnow() + timedelta(days=duration)
                sub = {
                    "allowed_accounts": allowed, 
                    "expiry": expiry.isoformat(), 
                    "price": price,
                    "payment_method": "zarinpal",
                    "ref_id": ref_id,
                    "authority": authority
                }
                subs.append(sub)
                user_subscriptions[str(user_id)] = subs
                save_subscriptions()
                
                success_text = (
                    "🎉 <b>پرداخت موفق</b>\n\n"
                    f"✅ اشتراک {duration} روزه برای {allowed} اکانت با موفقیت فعال شد.\n"
                    f"💳 شماره تراکنش: <code>{ref_id}</code>\n"
                    f"🔢 کارت پرداخت: <code>{card_pan}</code>\n\n"
                    "🚀 اکنون می‌توانید اکانت‌های خود را اضافه کنید و از خدمات تپچی استفاده کنید."
                )
                
                # Log successful payment
                admin_log(f"ZarinPal payment successful: User {user_id}, Amount {amount}, RefID {ref_id}", "INFO")
            
            # Remove pending payment
            remove_pending_payment(authority)
            
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("📲 اضافه کردن اکانت", callback_data="goto_tapchi")],
                [InlineKeyboardButton("🏠 بازگشت به منوی اصلی", callback_data="back_to_subscription")]
            ])
            
            await query.edit_message_text(success_text, reply_markup=keyboard, parse_mode="HTML")
            
        else:
            error_code = result.get("data", {}).get("code", -1) if result.get("data") else -1
            error_message = zarinpal.format_error_message(error_code)
            
            # Remove pending payment on failure
            remove_pending_payment(authority)
            
            await query.edit_message_text(
                f"❌ <b>پرداخت ناموفق</b>\n\n"
                f"📝 علت: {error_message}\n\n"
                "💡 اگر پول از حساب شما کسر شده، ظرف 72 ساعت به حساب شما بازگردانده می‌شود.\n\n"
                "لطفاً دوباره تلاش کنید یا با پشتیبانی تماس بگیرید.",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("🔄 تلاش مجدد", callback_data="pay_zarinpal"),
                    InlineKeyboardButton("↪️ بازگشت", callback_data="back_to_subscription")
                ]]),
                parse_mode="HTML"
            )
            
            # Log failed payment
            admin_log(f"ZarinPal payment failed: User {user_id}, Authority {authority}, Error {error_code}", "WARNING")
            
    except Exception as e:
        logging.error(f"Error in ZarinPal verification: {e}")
        await query.edit_message_text(
            "❌ <b>خطای سیستمی در تأیید پرداخت</b>\n\n"
            "لطفاً با پشتیبانی تماس بگیرید و شناسه زیر را ارائه دهید:\n"
            f"<code>{authority}</code>",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🆔 پشتیبانی", url="https://t.me/your_support_username"),
                InlineKeyboardButton("↪️ بازگشت", callback_data="back_to_subscription")
            ]]),
            parse_mode="HTML"
        )

async def handle_upgrade_zarinpal_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle ZarinPal payment for subscription upgrades"""
    query = update.callback_query
    user_id = query.from_user.id
    
    # Get pending upgrade subscription data
    upgrade = context.user_data.get("pending_upgrade_subscription")
    if not upgrade:
        await query.answer("❌ اطلاعات ارتقاء یافت نشد. لطفاً دوباره تلاش کنید.", show_alert=True)
        return
    
    allowed = upgrade["allowed"]
    final_price = upgrade["final_price"]
    duration = upgrade["duration"]
    
    try:
        # Prepare payment data
        amount = final_price  # Amount in Tomans
        description = f"ارتقاء اشتراک تپچی {duration} روزه برای {allowed} اکانت"
        
        # Use bot's webhook URL for callback (you should set this to your actual domain)
        callback_url = f"https://your-domain.com/zarinpal_callback"  # Replace with your actual callback URL
        
        # Get user info for metadata
        user = query.from_user
        mobile = user.username if user.username else None
        email = None
        order_id = f"upgrade_{user_id}_{int(datetime.now().timestamp())}"
        
        # Create payment request
        success, result = zarinpal.create_payment_request(
            amount=amount,
            description=description,
            callback_url=callback_url,
            mobile=mobile,
            order_id=order_id
        )
        
        if success:
            authority = result.get("authority")
            payment_url = zarinpal.get_payment_url(authority)
            
            # Store pending payment data for upgrade
            store_pending_payment(
                authority=authority,
                user_id=user_id,
                amount=amount,
                subscription_data={
                    "type": "upgrade",
                    "allowed": allowed,
                    "final_price": final_price,
                    "duration": duration,
                    "unused_value": upgrade["unused_value"],
                    "base_price": upgrade["base_price"],
                    "current_sub": upgrade["current_sub"]
                }
            )
            
            # Show payment instructions
            payment_text = (
                "💳 <b>پرداخت آنلاین زرین‌پال - ارتقاء اشتراک</b>\n\n"
                f"📊 مبلغ قابل پرداخت: <code>{amount:,}</code> تومان\n"
                f"🔗 شناسه پرداخت: <code>{authority}</code>\n\n"
                "🚀 برای ادامه روی دکمه زیر کلیک کنید و به درگاه پرداخت منتقل شوید.\n\n"
                "⚠️ <b>توجه:</b> پس از پرداخت موفق، به همین بخش بازگردید و روی دکمه تأیید پرداخت کلیک کنید."
            )
            
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("💳 ورود به درگاه پرداخت", url=payment_url)],
                [InlineKeyboardButton("✅ تأیید پرداخت", callback_data=f"verify_zarinpal:{authority}")],
                [InlineKeyboardButton("↪️ بازگشت", callback_data="back_to_subscription")]
            ])
            
            await query.edit_message_text(payment_text, reply_markup=keyboard, parse_mode="HTML")
            
        else:
            error_code = result.get("errors", [{}])[0].get("code", -1) if result.get("errors") else -1
            error_message = zarinpal.format_error_message(error_code)
            
            await query.edit_message_text(
                f"❌ <b>خطا در ایجاد درخواست پرداخت</b>\n\n"
                f"📝 پیام خطا: {error_message}\n\n"
                "لطفاً دوباره تلاش کنید یا با پشتیبانی تماس بگیرید.",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("🔄 تلاش مجدد", callback_data="pay_upgrade_zarinpal"),
                    InlineKeyboardButton("↪️ بازگشت", callback_data="back_to_subscription")
                ]]),
                parse_mode="HTML"
            )
            
    except Exception as e:
        logging.error(f"Error in ZarinPal upgrade payment request: {e}")
        await query.edit_message_text(
            "❌ <b>خطای سیستمی</b>\n\n"
            "متأسفانه خطایی در سیستم پرداخت رخ داده است.\n"
            "لطفاً چند دقیقه دیگر تلاش کنید.",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🔄 تلاش مجدد", callback_data="pay_upgrade_zarinpal"),
                InlineKeyboardButton("↪️ بازگشت", callback_data="back_to_subscription")
            ]]),
            parse_mode="HTML"
        )

# Main function where memory usage is also tracked
def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    log_memory_usage("Before loading data")  # Log memory before loading data
    # Load data
    load_data()
    load_subscriptions()
    log_memory_usage("After loading data")  # Log memory after loading data
    
    # Set up Telegram bot with saved data
    persistence = PicklePersistence(filepath="bot_data.pkl")
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .persistence(persistence)
        .post_init(on_startup)
        .build()
    )

    # Global error handler
    async def global_error_handler(update, context):
        print(f"[ERROR] {context.error}")

    app.add_error_handler(global_error_handler)

    # Handlers (same as before)
    add_account_conv = ConversationHandler(
        entry_points=[CommandHandler("add_account", add_account_entry)],
        states={WAIT_PHONE: [MessageHandler(((filters.TEXT & ~filters.COMMAND) | filters.CONTACT), wait_phone_handler)]},
        fallbacks=[]
    )
    app.add_handler(add_account_conv)
    app.add_handler(MessageHandler(filters.Regex(r"^Username\s+@\w+"), username_lookup_handler))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin_panel))
    app.add_handler(CommandHandler("balance", balance_handler))
    app.add_handler(CommandHandler("cut", cut_handler))
    app.add_handler(CommandHandler("charge", charge_handler))
    
    # Add reset command handler
    async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        clear_user_flags(context)
        await update.message.reply_text(
            "🔄 <b>ریست کامل انجام شد</b>\n\n"
            "✅ تمام حالت‌های ربات پاک شد\n"
            "✅ می‌توانید از ابتدا شروع کنید\n"
            "✅ برای بازگشت به منوی اصلی /start را بفرستید",
            parse_mode="HTML"
        )
    
    app.add_handler(CommandHandler("reset", reset_command))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo_upload))
    app.add_handler(MessageHandler((filters.TEXT | filters.Document.ALL) & ~filters.COMMAND, conditional_handler))
    app.add_handler(CallbackQueryHandler(inline_callback_handler))    
    app.add_handler(CommandHandler("cut_plan", cut_plan))
    app.add_handler(CommandHandler("add_plan", add_plan))
    app.add_handler(CommandHandler("see_plan", see_plan))
    app.add_handler(send_msg_conv)
    
    log_memory_usage("After adding handlers")  # Log memory after handlers are added

    # Jobs - Optimized intervals for better performance
    job_queue = app.job_queue
    job_queue.run_repeating(monshi_keepalive_job, interval=120, first=0)  # Every 2 minutes instead of 30 seconds
    job_queue.run_repeating(sending_job, interval=60, first=0)  # Keep 1 minute
    job_queue.run_repeating(restart_dead_clocks, interval=600, first=2)  # Every 10 minutes instead of 5

    log_memory_usage("Before starting bot")  # Log memory before starting the bot
    # Start the bot
    app.run_polling()

if __name__ == "__main__":
    main()