from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import APIException, NotAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from accounts.models import Address
from orders.models import Order
from payments.models import Coupon, Payment, PAYMENT_METHODS
from payments.serializers.clients import PaymentSerializer
from payments.services.checkout import checkout


class AddCouponAPI(APIView):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise NotAuthenticated()

        code = request.data.get('code', None)
        if code is None:
            return Response({"message": "Coupon code required"}, status=HTTP_400_BAD_REQUEST)
        order = Order.objects.get(
            user=self.request.user, ordered=False)
        coupon = get_object_or_404(Coupon, code=code)
        order.coupon = coupon
        order.save()
        return Response(status=HTTP_200_OK)


class PaymentListAPI(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)


class PaymentAPI(APIView):
    """
    Handles the checkout & payment process
    """
    class InputSerializer(serializers.Serializer):
        order = serializers.IntegerField()
        billing_address_id = serializers.IntegerField()
        shipping_address_id = serializers.IntegerField()
        payment_method = serializers.ChoiceField(choices=PAYMENT_METHODS)

    def post(self, request, *args, **kwargs):
        """
        :param request: request.data =
        {
        'payment_method': PAYMENT_METHODS,
        'billing_address_id': Address.id,
        'shipping_address_id': Address.id
        }
        """

        if not request.user.is_authenticated:
            print(request.user)
            raise NotAuthenticated()

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        payment_method = request.data.get('payment_method')
        billing_address = get_object_or_404(Address, id=request.data.get('billing_address_id'))
        shipping_address = get_object_or_404(Address, id=request.data.get('shipping_address_id'))

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            order.billing_address = billing_address
            order.shipping_address = shipping_address
            order.save()
            checkout(order=order, payment_method=payment_method)
        except ObjectDoesNotExist:
            raise Http404("You do not have an active order")
        except Exception as e:
            print(e)
            raise APIException('Something went wrong. Please try again. '
                               'Ensure the billing information you provided is correct')
        else:
            return Response(status=HTTP_200_OK)
