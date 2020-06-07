from django.contrib import admin
from .models import Item, Category, SubCategory, Brand, Variation, ItemVariation

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(Variation)
admin.site.register(ItemVariation)
