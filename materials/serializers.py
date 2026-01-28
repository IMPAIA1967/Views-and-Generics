from rest_framework import serializers
from materials.models import Lesson, Course, Subscription
from materials.validators import validate_video_url


class LessonSerializer(serializers.ModelSerializer):

    video_url = serializers.URLField(validators=[validate_video_url])

    class Meta:
        model = Lesson
        fields = '__all__'


def gef_lesson_count(obj):
    return obj.lesson_set.count()


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True) # вложенные уроки
    lessons_count = serializers.SerializerMethodField() # Поле для количества уроков
    is_subscribed = serializers.SerializerMethodField() # призрак подписки

    class Meta:
        model = Course
        fields = '__all__'

def get_is_subscribed(self, obj):
    """Проверяем, подписан ли пользователь на курс"""
    request = self.context.get('request')
    if request and request.user.is_authenticated: # проверка залогинен ли пользователь
        return Subscription.objects.filter(user=request.user, course=obj).exists()
    return False

