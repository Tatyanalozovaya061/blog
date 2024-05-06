import stripe
from django.urls import reverse
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_stripe_product_and_price(payment):
    stripe_product = stripe.Product.create(name=payment.pay_course.name)
    stripe_price = stripe.Price.create(
        currency='rub',
        unit_amount=payment.price * 100,
        product_data={'name': stripe_product['name']},
    )
    return stripe_price['id']


def create_payment_session(request, stripe_price_id):
    """Создание сессии для оплаты подписки"""

    stripe_session = stripe.checkout.Session.create(
        success_url='http://127.0.0.1:8000/',
        line_items=[{'price': stripe_price_id, 'quantity': 1}],
        mode='payment',
    )
    return stripe_session['url'], stripe_session['id']


    # session = stripe.checkout.Session.create(
    #     payment_method_types=['card'],
    #     line_items=[{
    #         'price_data': {
    #             'currency': 'rub',
    #             'product_data': {
    #                 'name': "Подписка на Blog Journal",
    #             },
    #             'unit_amount': 100 * 100,
    #         },
    #         'quantity': 1,
    #     }],
    #     mode='payment',
    #     success_url=request.build_absolute_uri(reverse('users:success_subscription')),
    #     cancel_url=request.build_absolute_uri(reverse('users:cancel_subscription')),
    # )
    #
    # return session