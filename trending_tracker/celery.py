import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trending_tracker.settings')

app = Celery('trending_tracker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


from celery.schedules import crontab

app.conf.beat_schedule = {
    'scrape-github-trending-daily': {
        'task': 'trending.tasks.scrape_trending',
        'schedule': crontab(hour=0, minute=0),
    },
}
