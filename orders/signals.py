from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.models import Order, OrderItem


@receiver(post_save, sender=Order)
def after_save_order(instance, **kwargs):
    # mark OrderItems as ordered if Order is ordered
    if instance.ordered:
        order_items = instance.items.all()
        for item in order_items:
            item.ordered = True
        OrderItem.objects.bulk_update(order_items, ['ordered'])
