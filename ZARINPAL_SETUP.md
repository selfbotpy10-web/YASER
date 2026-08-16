# راهنمای راه‌اندازی درگاه پرداخت زرین‌پال

## نصب و راه‌اندازی

### مرحله 1: تنظیمات اولیه

1. **دریافت Merchant ID از زرین‌پال:**
   - به پنل پذیرندگان زرین‌پال مراجعه کنید
   - Merchant ID خود را کپی کنید

2. **تنظیم فایل پیکربندی:**
   ```bash
   cp config_template.json config.json
   ```
   
   سپس فایل `config.json` را ویرایش کرده و مقادیر زیر را تنظیم کنید:
   ```json
   {
     "zarinpal": {
       "merchant_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
       "sandbox_mode": false,
       "callback_url": "https://your-domain.com/zarinpal_callback"
     }
   }
   ```

3. **نصب پکیج‌های مورد نیاز:**
   ```bash
   pip install -r requirements.txt
   ```

### مرحله 2: ویرایش کد اصلی

1. **تنظیم Merchant ID در `zarinpal_payment.py`:**
   ```python
   ZARINPAL_MERCHANT_ID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
   ```

2. **تنظیم URL callback در توابع پرداخت:**
   در فایل `Tapchi.py` در توابع `handle_zarinpal_payment` و `handle_upgrade_zarinpal_payment`، خط زیر را ویرایش کنید:
   ```python
   callback_url = f"https://your-domain.com/zarinpal_callback"
   ```
   `your-domain.com` را با دامنه واقعی خود جایگزین کنید.

### مرحله 3: راه‌اندازی وب‌هوک (اختیاری)

برای تأیید خودکار پرداخت‌ها، می‌توانید وب‌هوک را راه‌اندازی کنید:

1. **اجرای سرور وب‌هوک:**
   ```bash
   python zarinpal_webhook.py
   ```

2. **استفاده از Nginx (پروداکشن):**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location /zarinpal_callback {
           proxy_pass http://127.0.0.1:5000/zarinpal_callback;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

### مرحله 4: تست در حالت Sandbox

برای تست، از تنظیمات Sandbox استفاده کنید:

1. **در `zarinpal_payment.py`:**
   ```python
   # Uncomment sandbox URLs for testing
   ZARINPAL_REQUEST_URL = "https://sandbox.zarinpal.com/pg/v4/payment/request.json"
   ZARINPAL_VERIFY_URL = "https://sandbox.zarinpal.com/pg/v4/payment/verify.json"
   ZARINPAL_GATEWAY_URL = "https://sandbox.zarinpal.com/pg/StartPay/"
   ```

2. **Merchant ID برای Sandbox:**
   ```python
   ZARINPAL_MERCHANT_ID = "00000000-0000-0000-0000-000000000000"
   ```

## نحوه استفاده

### برای کاربران:

1. کاربر روی "🛒 خرید اشتراک" کلیک می‌کند
2. پلن مورد نظر را انتخاب می‌کند
3. روش پرداخت را انتخاب می‌کند:
   - 💰 پرداخت از موجودی کیف پول (اگر موجودی کافی باشد)
   - 💳 پرداخت آنلاین (زرین‌پال)
4. در صورت انتخاب زرین‌پال:
   - به درگاه پرداخت منتقل می‌شود
   - پس از پرداخت، باید روی "✅ تأیید پرداخت" کلیک کند
   - یا به صورت خودکار تأیید می‌شود (اگر وب‌هوک فعال باشد)

### فیچرهای اضافه شده:

- ✅ پرداخت آنلاین با زرین‌پال
- ✅ پشتیبانی از ارتقاء اشتراک با زرین‌پال
- ✅ تأیید دستی و خودکار پرداخت
- ✅ ذخیره اطلاعات تراکنش
- ✅ مدیریت خطاهای پرداخت
- ✅ لاگ‌گیری کامل از تراکنش‌ها

## عیب‌یابی

### مشکلات متداول:

1. **خطای "Merchant ID نامعتبر":**
   - Merchant ID را از پنل زرین‌پال کپی کنید
   - مطمئن شوید که اسپیس اضافی وجود ندارد

2. **خطای "Callback URL نامعتبر":**
   - URL باید با `https://` شروع شود
   - دامنه باید معتبر و در دسترس باشد

3. **تأیید پرداخت کار نمی‌کند:**
   - مطمئن شوید که فایل `data/pending_payments.json` قابل نوشتن است
   - لاگ‌های ربات را بررسی کنید

### لاگ‌های مفید:

```bash
# مشاهده لاگ‌های پرداخت
tail -f data/admin_logs/admin_$(date +%Y-%m-%d).log | grep -i zarinpal

# مشاهده پرداخت‌های در انتظار
cat data/pending_payments.json
```

## امنیت

⚠️ **نکات امنیتی مهم:**

1. Merchant ID را محرمانه نگه دارید
2. از HTTPS استفاده کنید
3. فایل‌های داده را بک‌آپ بگیرید
4. دسترسی‌های فایل‌ها را محدود کنید

## پشتیبانی

در صورت بروز مشکل:
1. ابتدا بخش عیب‌یابی را مطالعه کنید
2. لاگ‌های خطا را بررسی کنید
3. با پشتیبانی زرین‌پال تماس بگیرید

## نسخه‌ها

- v1.0: پیاده‌سازی اولیه زرین‌پال
- v1.1: افزودن پشتیبانی از ارتقاء اشتراک
- v1.2: اضافه کردن وب‌هوک خودکار
