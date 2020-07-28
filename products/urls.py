from django.urls import path

from products.views import product_detail, index, catalog, categories, subcategory

urlpatterns = [
    path('product', index, name='products/product'),
    path('product/<slug:item_slug>/', product_detail, name='products/product_detail'),
    path('catalog', catalog, name='products/catalog'),
    path('catalog/categories', categories, name='products/catalog/categories'),
    path('catalog/categories/subcategory', subcategory, name='products/catalog/categories/subcategories'),
]
