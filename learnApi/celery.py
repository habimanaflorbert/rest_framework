# learnApi/celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learnApi.settings")
app = Celery("learnApi")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()