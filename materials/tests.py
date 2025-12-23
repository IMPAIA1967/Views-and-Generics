from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Course, Lesson


User = get_user_model()

class MyTests(APITestCase):
    def test_user_can_create_lesson(self):

        #  Создаём пользователя
        user = User.objects.create_user(username='test@test.com', password='123')

        #  Создаём курс
        course = Course.objects.create(title='Мой курс', owner=user)

        # Делаем вид, что пользователь зашёл на сайт
        self.client.force_authenticate(user=user)

        # Пытаемся создать урок
        response = self.client.post('/api/lessons/create/', {
            'title': 'Новый урок',
            'video_url': 'https://www.youtube.com/watch?v=123',
            'course': course.id
        })
        print("Response data:", response.data)
        self.assertEqual(response.status_code, 201)  # успешно создано
        self.assertEqual(Lesson.objects.count(), 1)  # должен быть 1 урок