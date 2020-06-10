import uuid

from django.core.exceptions import ValidationError
from django.db import models

from products.models import CommonModelInfo

PAYMENT_METHODS = (
    ('M', 'Mpesa'),
    ('C', 'Card'),
)


class Payment(CommonModelInfo):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, editable=False)
    amount = models.FloatField(editable=False)
    payment_method = models.CharField(max_length=1, choices=PAYMENT_METHODS)
    #
    paid = models.BooleanField(default=False)
    waiting = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    failed = models.BooleanField(default=False)
    #
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order.user.username

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        payments = Payment.objects.all()
        if payments.filter(paid=True, order=self.order).exists():
            raise ValidationError('Order has already been paid for.')
        if payments.filter(waiting=True, order=self.order).exists():
            raise ValidationError('Please wait before making a new payment.')


class Coupon(CommonModelInfo):
    code = models.CharField(max_length=15, unique=True)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(CommonModelInfo):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, editable=False)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    waiting = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.order}"

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        if not self.order.payment_set.filter(paid=True).exists():
            raise ValidationError('Order has not been paid for.')
        if Refund.objects.filter(accepted=True, order=self.order):
            raise ValidationError('Order has already been refunded.')
