from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotAuthenticated, APIException
from rest_framework.generics import DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from orders.models import Order, OrderItem
from orders.serializers.clients import OrderSerializer
from orders.services.cart import add_to_cart, reduce_order_item_quantity
from products.models import Item, Variation


class OrderDetailAPI(RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            return order
        except ObjectDoesNotExist:
            raise Http404("You do not have an active order")


class OrderItemDeleteAPI(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = OrderItem.objects.all()


class AddToCartAPI(APIView):
    """
    Add to Order(cart)
    """

    def post(self, request, *args, **kwargs):

        # Create OrderItems
        if not request.user.is_authenticated:
            print(request.user)
            raise NotAuthenticated()

        # get Item Using slug
        slug = request.data.get('slug', None)
        if slug is None:
            return Response({"message": "Invalid request"}, status=HTTP_400_BAD_REQUEST)
        item = get_object_or_404(Item, slug=slug)

        # verify number of variations
        variations = request.data.get('variations', [])
        minimum_variation_count = Variation.objects.filter(item=item).count()
        if len(variations) < minimum_variation_count:
            return Response({"message": "Please specify the required variation types"}, status=HTTP_400_BAD_REQUEST)

        try:
            add_to_cart(item=item, variations=variations, user=request.user)
        except Exception as e:
            raise APIException(e)
        else:
            return Response(status=HTTP_200_OK)


class ReduceOrderItemQuantityAPI(APIView):
    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            raise NotAuthenticated()

        # get Item
        slug = request.data.get('slug', None)
        if slug is None:
            return Response({"message": "Invalid data"}, status=HTTP_400_BAD_REQUEST)
        item = get_object_or_404(Item, slug=slug)

        try:
            reduce_order_item_quantity(user=request.user, item=item)
        except Exception as e:
            raise APIException(e)
        else:
            return Response(status=HTTP_200_OK)
