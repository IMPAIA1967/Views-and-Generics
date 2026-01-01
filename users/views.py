from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from materials.models import Course
from materials.stripe_service import create_stripe_product, create_stripe_price, create_stripe_checkout_session, \
    retrieve_stripe_session
from users.filters import PaymentFilter
from users.models import Payment, User
from users.serializers import PaymentSerializer, RegisterSerializer, UserSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filters_backends = [DjangoFilterBackend]
    filterset_class =  PaymentFilter # класс фильтра
    ordering_fields = ['payment_date'] # сортировка по дате
    ordering = ['-payment_date'] # по умолчанию сортировка по убыванию


@api_view(['POST'])
@permission_classes([AllowAny])  # открывает эндпоинт для всех, даже без токена
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Пользователь успешно зарегистрирован!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Пользователь видит только свой профиль
        return User.objects.filter(id=self.request.user.id)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_stripe_payment(request):
    """
    Создаём платёж через Stripe.
    """
    course_id = request.data.get('course_id')
    course = get_object_or_404(Course, id=course_id)

    # 1. Создаём продукт в Stripe
    product = create_stripe_product(course.title)

    # 2. Создаём цену
    price = create_stripe_price(product.id, float(course.price))

    # 3. Создаём сессию
    session = create_stripe_checkout_session(
        price.id,
        success_url="http://localhost:8000/success/",
        cancel_url="http://localhost:8000/cancel/"
    )

    # 4. Сохраняем в модель Payment
    payment = Payment.objects.create(
        user=request.user,
        course=course,
        amount=course.price,
        payment_method='transfer',
        stripe_product_id=product.id,
        stripe_price_id=price.id,
        stripe_session_id=session.id,
        stripe_session_url=session.url,
        payment_status=session.payment_status
    )

    return Response({
        "message": "Платёж создан",
        "pay_url": session.url,
        "payment_id": payment.id
    })



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_stripe_payment_status(request, payment_id):
    """Проверяем статус платежа в Stripe."""
    payment = get_object_or_404(Payment, id=payment_id, user=request.user)

    # Получаем свежие данные из Stripe
    session_data = retrieve_stripe_session(payment.stripe_session_id)

    # Обновляем статус у себя
    payment.payment_status = session_data.payment_status
    payment.save()

    return Response({
        "status": session_data.payment_status,
        "amount_total": session_data.amount_total,  # в копейках
        "url": session_data.url
    })