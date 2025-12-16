from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

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