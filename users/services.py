import stripe
from django.urls import reverse

from config.settings import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY


def create_payment_session(request):
    """Создание сессии для оплаты подписки"""

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': "Подписка",
                },
                'unit_amount': 100 * 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('users:success_subscription')),
        cancel_url=request.build_absolute_uri(reverse('users:cancel_subscription')),
    )

    return session
