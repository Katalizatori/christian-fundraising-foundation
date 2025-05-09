from .base import *  # Import all base settings first

DEBUG = False  # Always False in staging/production
ALLOWED_HOSTS = ['staging.yourdomain.com']  # Your staging domaiin

# Database configuration (if not in base)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cf_staging_db',
        'USER': 'cf_staging_user',
        'PASSWORD': 'your_secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Email settings (use a testing configuration)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your.smtp.server'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Security settings
SECURE_SSL_REDIRECT = True  # If using SSL
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True