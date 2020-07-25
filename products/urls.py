from django.urls import path

from products.views import index, catalog, categories, subcategory

urlpatterns = [
    path('product', index, name='products/product'),
    path('catalog', catalog, name='products/catalog'),
    path('catalog/categories', categories, name='products/catalog/categories'),
    path('catalog/categories/subcategory', subcategory, name='products/catalog/categories/subcategories'),
]
