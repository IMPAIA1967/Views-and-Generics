from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, register_user, ProfileViewSet, check_stripe_payment_status, create_stripe_payment

router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('register/', register_user, name='register'),
    path('create-stripe-payment/', create_stripe_payment, name='create_stripe_payment'),
    path('check-stripe-payment/<int:payment_id>/', check_stripe_payment_status, name='check_stripe_payment'),
    path('', include(router.urls)),

]