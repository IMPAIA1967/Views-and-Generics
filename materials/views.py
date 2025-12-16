from rest_framework import serializers, generics, viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.serializers import LessonSerializer, CourseSerializer



class IsNotModerator(permissions.BasePermission):
    """Разрешает доступ, если пользователь не состоит в группе модераторы """
    def has_permission(self, request, view):
        return not request.user.groups.filter(name='модераторы').exists()


# Для курса — ViewSet
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.groups.filter(name='модераторы').exists():
            return Course.objects.all()
        return Course.objects.filter(owner=self.request.user)

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            # Только авторизованные не модераторы
            self.permission_classes = [IsAuthenticated, IsNotModerator]
        # Для list, retrieve, update — любой авторизованный (включая модераторов)
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

# Для урока — Generic-классы
class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.groups.filter(name='модераторы').exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)

class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsNotModerator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.groups.filter(name='модераторы').exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)

class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.groups.filter(name='модераторы').exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsNotModerator]

    def get_queryset(self):
        if self.request.user.groups.filter(name='модераторы').exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.groups.filter(name='модераторы').exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)

