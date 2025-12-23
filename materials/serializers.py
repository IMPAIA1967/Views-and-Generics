import self
from rest_framework import serializers

from materials.models import Lesson, Course
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


    class Meta:
        model = Course
        fields = '__all__'

