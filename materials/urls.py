from django.urls import path
from rest_framework import views



urlpatterns = [
    path('lessons/', views.LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/create/', views.LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lessons/<int:pk>/', views.LessonRetrieveAPIView.as_view(), name='lesson-detail'),
    path('lessons/<int:pk>/update/', views.LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lessons/<int:pk>/delete/', views.LessonDestroyAPIView.as_view(), name='lesson-delete'),
]