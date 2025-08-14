# christianfoundation/settings/development.py
import os
import dj_database_url
from .base import *

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "https://christian-fundraising-foundation-8x79.onrender.com"]

# Database configuration using DATABASE_URL
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600  # Optional: improves performance
    )
}

# Fallback sqlite

if not all(DATABASES['default'].values()):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Dev-only npm path (Windows-specific)
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"