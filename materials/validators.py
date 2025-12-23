from urllib.parse import urlparse

from django.core.exceptions import ValidationError


def validate_video_url(value):
    """Проверяем что сылка ведет только на ютюб"""

    # Разбираем ссылку на части
    parsed_url = urlparse(value)

    # Извлекаем домен
    domain = parsed_url.netloc.lower()

    # Разрешаем только домены, которые заканчиваются на 'youtube.com'
    if not domain.endswith('youtube.com'):
        raise ValidationError('Ссылка на видео должна вести только на youtube.com')



