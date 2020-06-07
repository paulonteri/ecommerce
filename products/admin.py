from django.contrib import admin
from .models import Item, Category, SubCategory, Brand

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
