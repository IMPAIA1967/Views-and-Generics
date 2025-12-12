import django_filters
from .models import Payment


class PaymentFilter(django_filters.FilterSet):
    course = django_filters.ModelChoiceFilter(queryset=None, field_name='course', label='Курс')
    lesson = django_filters.ModelChoiceFilter(queryset=None, field_name='lesson', label='Урок')
    payment_method = django_filters.ChoiceFilter(choices=Payment.PAYMENT_CHOICES, label='Способ оплаты')

    class Meta:
        model = Payment
        fields = ['course', 'lesson', 'payment_method']