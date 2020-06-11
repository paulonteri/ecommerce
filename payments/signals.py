from django.db.models.signals import post_save

from payments.models import Payment
from django.dispatch import receiver


@receiver(post_save, sender=Payment)
def post_payment_save(sender, instance, **kwargs):
    if instance.paid:
        order = instance.order
        order.ordered = True
        order.save()

