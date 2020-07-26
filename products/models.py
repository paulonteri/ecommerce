from django.db import models


class CommonModelInfo(models.Model):
    time_added = models.DateTimeField(
        auto_now_add=True)
    time_last_edited = models.DateTimeField(
        auto_now=True)
    #
    last_edited_by = models.ForeignKey(
        'accounts.User', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class Category(CommonModelInfo):
    title = models.CharField(max_length=30, unique=True)
    image = models.ImageField(
        upload_to='images/dynamic/products/categories', null=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['title']

    def save(self, *args, **kwargs):
        if self.title:
            self.title = self.title.lower()
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class SubCategory(CommonModelInfo):
    title = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images/dynamic/products/subcategories', null=True)

    class Meta:
        verbose_name_plural = "Sub Categories"
        ordering = ['title']

    def save(self, *args, **kwargs):
        if self.title:
            self.title = self.title.lower()
        return super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} of {self.category.title}'


class Brand(CommonModelInfo):
    title = models.CharField(max_length=30, unique=True)
    image = models.ImageField(
        upload_to='images/dynamic/products/brands', null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


# TODO: Add separate model to store the display images
class Item(CommonModelInfo):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/dynamic/products/items/')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Variation(CommonModelInfo):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # size, color

    class Meta:
        unique_together = ['item', 'name']

    def __str__(self):
        return self.name


class ItemVariation(CommonModelInfo):
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)  # S, M, L
    attachment = models.ImageField(blank=True, null=True)

    class Meta:
        unique_together = (
            ('variation', 'value')
        )

    def __str__(self):
        return self.value
