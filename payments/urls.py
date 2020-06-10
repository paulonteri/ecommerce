from django.urls import path

from payments.api.clients import AddCouponAPI, PaymentListAPI, PaymentAPI

urlpatterns = [
    path('', PaymentListAPI.as_view(), name='payment-list'),
    path('add-coupon/', AddCouponAPI.as_view(), name='add-coupon'),
    path('checkout/', PaymentAPI.as_view(), name='checkout'),
]
