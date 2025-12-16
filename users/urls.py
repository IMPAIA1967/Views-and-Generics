from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, register_user, ProfileViewSet

router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('register/', register_user, name='register'),
    path('', include(router.urls)),

]