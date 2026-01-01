import os

import stripe

STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')


def create_stripe_product(name):
    """Создаём продукт в Stripe"""
    product = stripe.Product.create(name=name)
    return product


def create_stripe_price(product_id, amount):
    """Создаём цену в Stripe"""
    price = stripe.Price.create(product_id=product_id, unit_amount=int(amount), currency="rub")


def create_stripe_price(product_id: str, amount_rub: float) -> stripe.Price:
    """Создаём цену в Stripe"""
    amount_in_kopecks = int(amount_rub * 100)  # рубли → копейки
    price = stripe.Price.create(
        product=product_id,
        unit_amount=amount_in_kopecks,  # копейки
        currency="rub"
    )
    return price


def create_stripe_checkout_session(price_id, success_url, cancel_url):
    """ Создаём сессию оплаты в Stripe"""
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],  # Разрешаем только карты
        line_items=[{
            'price': price_id, # Какую цену оплачиваем
            'quantity': 1, # количество курсов
        }],
        mode='payment', # одноразовый платёж
        success_url=success_url,     # URL успеха
        cancel_url=cancel_url        # URL отмены
    )
    return session


def retrieve_stripe_session(session_id):
    """Получаем данные существующей сессии в Stripe"""
    session = stripe.checkout.Session.retrieve(session_id)
    return session
