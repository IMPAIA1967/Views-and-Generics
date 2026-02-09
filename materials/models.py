from django.db import models


class Course(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name='Название курса'
    )
    preview = models.ImageField(
        blank=True,
        null=True,
        verbose_name='Превью (картинка)'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание'
    )
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name='Название урока'
    )
    preview = models.ImageField(
        blank=True,
        null=True,
        verbose_name='Превью (картинка)'
    )
    video_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Ссылка на видео'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс'
    )
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Владелец'
    )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.title


class Subscription(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f"{self.user.email} -> {self.course.title}"
