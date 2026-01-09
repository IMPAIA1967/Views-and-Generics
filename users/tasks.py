from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


@shared_task
def block_inactive_users():
    """Блокирует пользователей, которые не заходили больше 30 дней"""
    try:
        print("=" * 50)
        print("Задача block_inactive_users запущена!")
        print("=" * 50)

        # Дата, раньше которой пользователь считается неактивным
        cutoff_date = timezone.now() - timedelta(days=30)

        # Находим пользователей, которые не заходили больше 30 дней
        inactive_users = User.objects.filter(
            last_login__lt=cutoff_date,
            is_active=True
        )

        # Считаем сколько таких пользователей
        count = inactive_users.count()

        if count > 0:
            # Блокируем их
            inactive_users.update(is_active=False)
            result = f"✅ Заблокировано {count} неактивных пользователей"
        else:
            result = f"✅ Неактивных пользователей не найдено"

        print(result)
        print("=" * 50)
        return result

    except Exception as e:
        error_msg = f"❌ Ошибка в задаче: {str(e)}"
        print(error_msg)
        return error_msg