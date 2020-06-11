from django.db.models.signals import m2m_changed

from orders.models import Order


def add_order_items(instance, **kwargs):
    print('yow')


m2m_changed.connect(add_order_items, sender=Order.items.through)
