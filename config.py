import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # تنظیمات توکن و دیتابیس
    TOKEN = os.getenv("BOT_TOKEN")
    DB_PATH = "data/phrases.db"
    
    # تنظیمات زمان‌بندی
    NOTIFICATION_HOUR = 8  # ساعت ارسال پیام‌های صبحگاهی
    
    # محدودیت‌ها
    MAX_EVENTS_PER_DAY = 3
