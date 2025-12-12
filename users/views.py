from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from users.filters import PaymentFilter
from users.models import Payment
from users.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filters_backends = [DjangoFilterBackend]
    filterset_class =  PaymentFilter # класс фильтра
    ordering_fields = ['payment_date'] # сортировка по дате
    ordering = ['-payment_date'] # по умолчанию сортировка по убыванию


