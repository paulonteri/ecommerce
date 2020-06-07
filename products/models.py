from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)
    #
    time_added = models.DateTimeField(
        auto_now_add=True)
    time_last_edited = models.DateTimeField(
        auto_now=True)
    #
    last_edited_by = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #
    time_added = models.DateTimeField(
        auto_now_add=True)
    time_last_edited = models.DateTimeField(
        auto_now=True)
    #
    last_edited_by = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title} of {self.category.title}'


class Brand(models.Model):
    title = models.CharField(max_length=30, unique=True)
    #
    time_added = models.DateTimeField(
        auto_now_add=True)
    time_last_edited = models.DateTimeField(
        auto_now=True)
    #
    last_edited_by = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    description = models.TextField()
    image = models.ImageField()
    #
    time_added = models.DateTimeField(
        auto_now_add=True)
    time_last_edited = models.DateTimeField(
        auto_now=True)
    #
    last_edited_by = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
