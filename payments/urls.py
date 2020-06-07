from django.urls import path

from payments.api.clients import AddCouponView, PaymentListView

urlpatterns = [
    path('', PaymentListView.as_view(), name='payment-list'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
]
