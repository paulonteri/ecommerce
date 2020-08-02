import uuid

from django.core.exceptions import ValidationError
from django.db import models

from payments.models import Payment


class CommonOrdersModelInfo(models.Model):
    time_added = models.DateTimeField(
        auto_now_add=True)
    time_last_edited = models.DateTimeField(
        auto_now=True)
    #
    user = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class OrderItem(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey('products.Item', on_delete=models.PROTECT)
    # TODO: Implement variations better
    # item_variations = models.ManyToManyField('products.ItemVariation')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'accounts.Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'accounts.Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'payments.Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    # TODO:
    # ref_code = models.CharField(max_length=20, blank=True, null=True)
    ordered_date = models.DateTimeField()

    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        orders = Order.objects.filter(user=self.user)

        # Save new Order
        if self._state.adding:

            if orders.exists():

                # prevent addition of new orders while waiting for payments
                if Payment.objects.filter(order__in=orders, waiting=True).exists():
                    raise ValidationError('Complete previous order payments transactions.')

                # prevent two active orders
                if not self.ordered:
                    obj = orders.filter(ordered=False)
                    if obj and obj[0].id != self.id:
                        raise ValidationError('A user cannot have two active carts/orders.')

        # Update Order
        else:

            # prevent editing ordered order
            ordered_obj_qs = orders.filter(id=self.id, ordered=True)
            if ordered_obj_qs.exists():
                ordered_object = ordered_obj_qs[0]
                if ordered_object.user != self.user or ordered_object.coupon != self.coupon:
                    raise ValidationError('Order already processed.')

            # prevent addition of new orders while waiting for payments
            if self.ordered:
                if Payment.objects.filter(order__in=orders, waiting=True).exists():
                    raise ValidationError('Complete previous order payments transactions.')

            else:
                obj = orders.filter(ordered=False)
                if obj and obj[0].id != self.id:
                    raise ValidationError('A user cannot have two active carts/orders.')

