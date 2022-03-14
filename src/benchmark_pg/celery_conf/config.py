import os
# File config for celery

broker_url = 'redis://redis:6379/0'
result_backend = 'redis://redis:6379/1'


CELERY_IMPORTS=("api.views",)

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True
