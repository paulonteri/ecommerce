from django.urls import path

from orders.api.cart import OrderItemDeleteAPI, ReduceOrderItemQuantityAPI, OrderDetailAPI, AddToCartAPI

urlpatterns = [
    path('add-to-cart/', AddToCartAPI.as_view(), name='add-to-cart'),
    path('order-summary/', OrderDetailAPI.as_view(), name='order-summary'),
    path('order-items/<pk>/delete/',
         OrderItemDeleteAPI.as_view(), name='order-item-delete'),
    path('order-item/reduce-quantity/',
         ReduceOrderItemQuantityAPI.as_view(), name='order-item-update-quantity'),
]
