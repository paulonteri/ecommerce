from django.db import models
from products.models import CommonModelInfo


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Coupon(CommonModelInfo):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code



