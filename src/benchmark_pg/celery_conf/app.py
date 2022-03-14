from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "benchmark_pg.settings")

app = Celery("benchmark_pg")
app.config_from_object("celery_conf.config", namespace="CELERY")
app.autodiscover_tasks()
