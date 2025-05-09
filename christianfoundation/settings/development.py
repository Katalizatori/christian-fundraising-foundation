# christianfoundation/settings/development.py
from .base import *

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# SQLite for local development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Dev-only npm path (Windows-specific)
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"