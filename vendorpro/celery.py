# celery.py
import os
from celery import Celery
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vendorpro.settings')
# Create a Celery instance
celery_app = Celery('vendorpro')
# Load task modules from all registered Django app configs.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
# Autodiscover tasks in all installed apps
celery_app.autodiscover_tasks()