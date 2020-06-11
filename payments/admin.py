from django.contrib import admin
from .models import Payment, Coupon, Refund, Transaction

admin.site.register(Coupon)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'order', 'amount']


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'order']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'payment', 'paid', 'waiting', 'failed',
                       'description', 'status', 'transaction_id', 'provider_channel']
