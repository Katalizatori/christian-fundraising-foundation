# christianfoundation/settings/development.py
import os
from .base import *

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "https://christian-fundraising-foundation-8x79.onrender.com"]

# SQLite for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

# Fallback sqlite

# If any PostgreSQL env var is missing, fall back to SQLite
if not all(DATABASES['default'].values()):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Dev-only npm path (Windows-specific)
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"