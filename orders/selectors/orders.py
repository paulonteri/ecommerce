from django.core.exceptions import MultipleObjectsReturned

from accounts.models import User
from orders.models import Order
from payments.models import Payment


def get_order_for_items_update(user: User):

    # check if there is an active order
    order_qs = Order.objects.filter(user=user, ordered=False)
    if order_qs.exists():

        # cannot have more than one active order
        if order_qs.count() != 1:
            raise MultipleObjectsReturned()

        # Cannot update order while paying for it
        if Payment.objects.filter(order__in=order_qs, waiting=True).exists():
            raise Exception('Please complete the payment of the previous order')
        else:
            return order_qs[0]
    else:
        return None

