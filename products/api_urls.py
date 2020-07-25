from django.urls import path
from products.api.clients import (
    ItemListView,
    ItemDetailView,
)

urlpatterns = [
    path('', ItemListView.as_view(), name='product-list'),
    path('<pk>/', ItemDetailView.as_view(), name='product-detail'),
]
