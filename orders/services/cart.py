from django.db.models import Q
from django.utils import timezone

from accounts.models import User
from orders.models import OrderItem, Order
from orders.selectors.orders import get_order_for_items_update
from payments.models import Payment, Coupon
from products.models import Item, Variation


def add_to_cart(user: User, item: Item, variations=None):
    """
    Add OrderItems to Order(cart)
    One Item at a Time
    """
    
    # TODO: Transaction Atomic
    # https://github.com/ljodal/djangocon-eu-2019/blob/master/orders/managers.py

    # check if OrderItem
    # order item queryset, check for items already in the cart
    order_item_qs = OrderItem.objects.filter(
        item=item,
        user=user,
        ordered=False
    )

    # if item is in OrderItem, add quantity
    if order_item_qs.exists():
        order_item = order_item_qs.first()
        order_item.quantity += 1
        order_item.save()
    # else create item in OrderItem
    else:
        order_item = OrderItem.objects.create(
            item=item,
            user=user,
            ordered=False
        )

        order_item.save()

    # check if there is an active order
    order_qs = get_order_for_items_update(user=user)

    # add item to Order if there is an active order
    if order_qs is not None:
        order = order_qs
        if not order.items.filter(item__id=order_item.id).exists():
            order.items.add(order_item)
            return True
    # create order & add item to Order otherwise
    else:
        order = Order.objects.create(
            user=user, ordered_date=timezone.now())
        order.items.add(order_item)
        return True


def reduce_order_item_quantity(user: User, item: Item, ):
    """
    Reduce order item quantity
    """

    # get Order
    order_qs = Order.objects.filter(
        user=user,
        ordered=False
    )

    # check if thre is an order with an incomplete payment
    if Payment.objects.filter(order__in=order_qs, waiting=True).exists():
        raise Exception('Please complete the payment of your previous order')

    if order_qs.exists():
        order = order_qs[0]
        # get OrderItem
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=user,
                ordered=False
            )[0]
            # if there are more than one, reduce quantity by one
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            # else delete it
            else:
                order.items.remove(order_item)
            return True
        else:
            raise Exception("This item was not in your cart")
    else:
        raise Exception("You do not have an active order")


# def add_coupon(coupon:Coupon):
