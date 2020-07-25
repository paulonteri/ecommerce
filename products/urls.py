from django.urls import path

from products.views import index, catalog, categories

urlpatterns = [
    path('product', index, name='products/product'),
    path('catalog', catalog, name='products/catalog'),
    path('categories', categories, name='products/categories'),
]
