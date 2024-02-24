#!/bin/sh
set -e

# Apply database migrations
python manage.py migrate --noinput

# Start server
gunicorn server.wsgi:application --bind 0.0.0.0:80 --workers=3 --preload
