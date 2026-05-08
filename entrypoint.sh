#!/bin/sh
set -e

echo "--- Keleres Terminal - Starting ---"
echo "Current directory: $(pwd)"
echo "Files in /app:"
ls -la /app/
echo "Config dir:"
ls -la /app/config/ 2>/dev/null || echo "NO CONFIG DIR"

# Wait for database to be ready
if [ -n "$DB_HOST" ]; then
    echo "Waiting for database at $DB_HOST:5432..."
    for i in $(seq 1 30); do
        if python -c "import socket; s=socket.socket(); s.settimeout(2); s.connect(('$DB_HOST', 5432)); s.close()" 2>/dev/null; then
            echo "Database ready!"
            break
        fi
        echo "Waiting... ($i/30)"
        sleep 2
    done
fi

echo "Running collectstatic..."
python manage.py collectstatic --noinput 2>&1

echo "Running migrations..."
python manage.py migrate --noinput 2>&1

echo "Starting gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4
