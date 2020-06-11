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
    paid = models.BooleanField(default=False, editable=False)
    waiting = models.BooleanField(default=False, editable=False)
    cancelled = models.BooleanField(default=False, editable=False)
    failed = models.BooleanField(default=False, editable=False)
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
        if not self.id:
            waiting = payments.filter(waiting=True, order=self.order)
            if waiting.exists():
                raise ValidationError(
                    'Please complete your previous payment before making a new payment.')
        if self.paid:
            if self.failed:
                raise ValidationError('Payment cannot be paid and failed at the same time')
            if self.waiting:
                raise ValidationError('Payment cannot be paid and waiting at the same time')
            if self.cancelled:
                raise ValidationError('Payment cannot be paid and cancelled at the same time')
        if self.waiting:
            if self.failed:
                raise ValidationError('Payment cannot be waiting and failed at the same time')
            if self.paid:
                raise ValidationError('Payment cannot be waiting and paid at the same time')
            if self.cancelled:
                raise ValidationError('Payment cannot be waiting and cancelled at the same time')
        if self.failed:
            if self.paid:
                raise ValidationError('Payment cannot be failed and paid at the same time')
            if self.waiting:
                raise ValidationError('Payment cannot be failed and waiting at the same time')
            if self.cancelled:
                raise ValidationError('Payment cannot be failed and cancelled at the same time')
        if self.cancelled:
            if self.paid:
                raise ValidationError('Payment cannot be cancelled and paid at the same time')
            if self.waiting:
                raise ValidationError('Payment cannot be cancelled and waiting at the same time')
            if self.failed:
                raise ValidationError('Payment cannot be cancelled and failed at the same time')


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
        if not self.order.ordered:
            raise ValidationError('Order not complete.')
        if not self.order.payment_set.filter(paid=True).exists():
            raise ValidationError('Order has not been paid for.')
        if Refund.objects.filter(accepted=True, order=self.order):
            raise ValidationError('Order has already been refunded.')
        if self.accepted:
            if self.rejected:
                raise ValidationError('Refund cannot be accepted and rejected at the same time')
            if self.waiting:
                raise ValidationError('Refund cannot be accepted and waiting at the same time')
        if self.waiting:
            if self.rejected:
                raise ValidationError('Refund cannot be waiting and rejected at the same time')
            if self.accepted:
                raise ValidationError('Refund cannot be waiting and accepted at the same time')
        if self.rejected:
            if self.accepted:
                raise ValidationError('Refund cannot be rejected and accepted at the same time')
            if self.waiting:
                raise ValidationError('Refund cannot be failed and waiting at the same time')


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, editable=False)
    #
    description = models.CharField(max_length=255, null=True, blank=True, editable=False)
    status = models.CharField(max_length=255, null=True, blank=True, editable=False)
    transaction_id = models.CharField(max_length=255, null=True, blank=True, editable=False)
    provider_channel = models.CharField(max_length=255, null=True, blank=True, editable=False)
    #
    paid = models.BooleanField(default=False, editable=False)
    waiting = models.BooleanField(default=False, editable=False)
    failed = models.BooleanField(default=False, editable=False)
    #
    error_message = models.TextField(null=True, blank=True, editable=False)
    #
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        if self.paid:
            if self.failed:
                raise ValidationError('Transaction cannot be paid and failed at the same time')
            if self.waiting:
                raise ValidationError('Transaction cannot be paid and waiting at the same time')
        if self.waiting:
            if self.failed:
                raise ValidationError('Transaction cannot be waiting and failed at the same time')
            if self.paid:
                raise ValidationError('Transaction cannot be waiting and paid at the same time')
        if self.failed:
            if self.paid:
                raise ValidationError('Transaction cannot be failed and paid at the same time')
            if self.waiting:
                raise ValidationError('Transaction cannot be failed and waiting at the same time')
