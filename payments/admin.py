from django.contrib import admin
from .models import Payment, Coupon, Refund

admin.site.register(Coupon)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'order', 'amount']


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'order']
