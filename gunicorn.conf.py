# gunicorn.conf.py
import multiprocessing

# Server socket
bind = "0.0.0.0:10000"

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gthread"
threads = 3

# Timeouts
timeout = 120  # Seconds
graceful_timeout = 30
keepalive = 5

# Logging
accesslog = "-"  # Log to stdout
errorlog = "-"   # Log to stderr
loglevel = "info"

# Security
limit_request_fields = 32000
limit_request_field_size = 0  # Unlimited

# Server mechanics
max_requests = 1000
max_requests_jitter = 50