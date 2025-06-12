import os
import sys

# Set Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings")

# Initialize Django
import django
django.setup()

# Import settings
from django.conf import settings

print("=== DJANGO SETTINGS ===")
print(f"BROKER_URL: {getattr(settings, 'BROKER_URL', 'NOT SET')}")
print(f"CELERY_BROKER_URL: {getattr(settings, 'CELERY_BROKER_URL', 'NOT SET')}")
print(f"CELERY_RESULT_BACKEND: {getattr(settings, 'CELERY_RESULT_BACKEND', 'NOT SET')}")
print(f"REDIS_LOCATION: {getattr(settings, 'REDIS_LOCATION', 'NOT SET')}")

# Import and inspect Celery app
from cms.celery import app

print("\n=== CELERY APP CONFIG ===")
print(f"broker_url: {app.conf.broker_url}")
print(f"result_backend: {app.conf.result_backend}")
print(f"task_serializer: {app.conf.task_serializer}")

# Check namespace loading
print("\n=== CELERY NAMESPACE CHECK ===")
all_settings = [attr for attr in dir(settings) if attr.startswith('CELERY_')]
for setting in all_settings[:10]:  # Show first 10
    print(f"{setting}: {getattr(settings, setting)}")

print("\n=== ENVIRONMENT VARIABLES ===")
print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
print(f"BROKER_URL (env): {os.environ.get('BROKER_URL')}")
print(f"CELERY_BROKER_URL (env): {os.environ.get('CELERY_BROKER_URL')}")

print("\n=== CHECKING CELERY DEFAULT BROKER ===")
# Check if Celery has any default configuration
print(f"Celery default broker_url: {app.conf.get('broker_url', 'NOT SET')}")

# Let's also check what happens when we manually set it
print("\n=== MANUAL BROKER SETTING TEST ===")
app.conf.broker_url = 'redis://127.0.0.1:6379/1'
print(f"After manual setting: {app.conf.broker_url}")