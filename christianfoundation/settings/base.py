# christianfoundation/settings/base.py
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ========================
# Core Path Configuration
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_DIR = BASE_DIR / "christianfoundation"

# ========================
# Security & Environment
# ========================
SECRET_KEY = os.getenv("SECRET_KEY")  # Loaded from .env
MAILCHIMP_API_KEY = os.getenv('MAILCHIMP_API_KEY')
MAILCHIMP_LIST_ID = os.getenv('MAILCHIMP_LIST_ID')
MAILCHIMP_SERVER_PREFIX = os.getenv('MAILCHIMP_SERVER_PREFIX')

# ========================
# Application Definition
# ========================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ckeditor",
    "ckeditor_uploader",
    "tailwind",
    "django_bleach",
    "blog",
    "training",
    "subscriptions",
    "calls",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware', # !! Must be second
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ========================
# Templates
# ========================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",  # Now looks in project_root/templates/
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "subscriptions.context_processor.subscribe_form",
            ],
        },
    },
]

# ========================
# Database
# (Configured in environment-specific files)
# ========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # Will be overridden in production.py
    }
}

# ========================
# Static & Media Files (UPDATE THESE)
# ========================
STATIC_URL = "/static/"  # Add leading slash
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "blog/static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ========================
# Third-Party Configurations
# ========================
# CKEditor
CKEDITOR_UPLOAD_PATH = "ckeditor_uploads/"
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "Custom",
        "height": 400,
        "width": "100%",
        "extraPlugins": ",".join(["uploadimage"]),
        "uploadUrl": "/ckeditor/upload/",
    },
}

# Bleach
BLEACH_ALLOWED_TAGS = ['p', 'br', 'ul', 'ol', 'li', 'strong', 'em', 'a']
BLEACH_ALLOWED_ATTRIBUTES = {'a': ['href', 'title']}
BLEACH_STRIP_TAGS = True
BLEACH_STRIP_COMMENTS = True
BLEACH_CLEAN_STYLE = True


# ========================
# Other Core Settings
# ========================
ROOT_URLCONF = "christianfoundation.urls"
WSGI_APPLICATION = "christianfoundation.wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ========================
# Development-Specific (will be overridden in production)
# ========================
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"  # Dev-only

if 'RENDER' in os.environ:
    # Tell Django to trust the X-Forwarded-Proto header
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    
    # WhiteNoise configuration
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'