# Render-compatible build script (works on Windows/WSL and Linux)

# Exit on errors
set -e

echo "=== Starting Build Process ==="

# 1. Install Python dependencies
echo "Installing Python packages..."
pip install -r requirements.txt

# 2. Ensure PostgreSQL support
echo "Installing psycopg2..."
pip install psycopg2-binary

# 3. Handle static files
if [ "$DISABLE_COLLECTSTATIC" != "1" ]; then
    echo "Collecting static files..."
    python manage.py collectstatic --noinput
else
    echo "Skipping collectstatic (DISABLE_COLLECTSTATIC=1)"
fi

# 4. Apply database migrations
echo "Applying migrations..."
python manage.py migrate --noinput

echo "=== Build Successful ==="