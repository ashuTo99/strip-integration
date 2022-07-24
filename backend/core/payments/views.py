from django.conf import settings
from rest_framework.views import APIView
import stripe
from rest_framework.response import Response
from rest_framework import status

from rest_framework import authentication, permissions
from django.shortcuts import redirect

stripe.api_key = settings.STRIP_SECRET_KEY


class StripCheckOutView(APIView):
    def post(self, request):
        try:
        #     pay_data = {
        #     "price_data": {
        #         "currency": "usd",
        #         "unit_amount": 1000,
        #         "product_data": {
        #             "name": "hari mirch",
        #             "images": 
        #             '',
        #         }
        #     },
        #     "quantity": 1,
        # }
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': 'price_1LOwvdSGaK3NGrLZufXlToU4',
                        'quantity': 1,
                    },
                    # pay_data
                ],
                mode='payment',
                success_url=settings.SITE_URL + '?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=settings.SITE_URL + '?canceled=true',
            )
            return redirect(checkout_session.url, code=303)
        except:
            return Response(
                {'error':"somthing went wrong",
                'status':status.HTTP_500_INTERNAL_SERVER_ERROR}
            )


class StripeRefundView(APIView):
    """
    StripeRefundView is the API of refund resource, and
    responsible to handle the requests of /refund/ endpoint.
    """
    YOUR_PAYMENT_INTENT_ID = ''
    def post(self, request, format=None):
        refund = stripe.Refund.create(
            payment_intent={YOUR_PAYMENT_INTENT_ID}
        )
        return Response(refund)

