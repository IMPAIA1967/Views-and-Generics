from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from materials.models import Subscription


@shared_task
def send_course_update_email(course_id, course_title, emails=None):
    """Отправляет email всем подписчикам курса"""
    # Получаем подписчиков
    subscriptions = Subscription.objects.filter(course_id=course_id)
    email = [sub.user.email for sub in subscriptions if sub.user.email]

    if email:
        send_mail(
            subject=f"Курс «{course_title}» обновлён!",
            message=f"Привет! Материалы курса «{course_title}» были обновлены.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=emails,
            fail_silently=False,
        )
    return f'Писем отправлено: {len(email)} шт'

