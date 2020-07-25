from django.urls import path

from products.views import index

urlpatterns = [
    path('product', index, name='products/product'),
]
