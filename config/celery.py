import os
from celery import Celery
from celery.schedules import crontab

# Указываем, где настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создаём приложение Celery
app = Celery('config')

# Загружаем настройки из settings.py (только те, что начинаются с CELERY)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Ищем задачи в файлах tasks.py всех приложений
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'block-inactive-users': {
        'task': 'users.tasks.block_inactive_users',
        'schedule': crontab(hour=3, minute=0, day_of_week=0),
    },
}

# часовой пояс для задачи
app.conf.timezone = 'UTC'