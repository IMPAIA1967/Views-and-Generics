import os
from celery import Celery

# Указываем, где настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создаём приложение Celery
app = Celery('config')

# Загружаем настройки из settings.py (только те, что начинаются с CELERY)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Ищем задачи в файлах tasks.py всех приложений
app.autodiscover_tasks()