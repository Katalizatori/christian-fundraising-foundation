#!/bin/bash
# Render-compatible build script with improved static files handling

# Exit on errors and show commands
set -ex

echo "=== Starting Build Process ==="

# 1. Install Python dependencies
echo "----- Installing Python packages -----"
pip install -r requirements/prod.txt

# 2. Ensure PostgreSQL support (should be in requirements.txt, but keeping as backup)
echo "----- Installing psycopg2 -----"
pip install psycopg2-binary

# 3. Static files collection with enhanced logging
if [ "$DISABLE_COLLECTSTATIC" != "1" ]; then
    echo "----- Collecting static files -----"
    # Clear previous builds completely
    rm -rf /opt/render/project/src/staticfiles/
    
    # Run collectstatic with maximum verbosity
    python manage.py collectstatic --noinput -v 3
    
    # Verify collection with detailed output
    echo "----- Verifying collected files -----"
    ls -la /opt/render/project/src/staticfiles/
    du -sh /opt/render/project/src/staticfiles/
else
    echo "----- Skipping collectstatic (DISABLE_COLLECTSTATIC=1) -----"
fi

# 4. Apply database migrations
echo "----- Applying migrations -----"
python manage.py migrate --noinput

echo "----- Final Directory Structure -----"
find /opt/render/project/src -maxdepth 3 -type d | sort

echo "=== Build Successful ==="