from django.db import models


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
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey('products.Item', on_delete=models.PROTECT)
    item_variations = models.ManyToManyField('products.ItemVariation')
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
