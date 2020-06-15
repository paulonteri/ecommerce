from django.contrib import admin
from .models import Payment, Coupon, Refund, Transaction, TransactionPhone, TransactionResponse

admin.site.register(Coupon)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'order', 'amount',
                       'paid', 'waiting', 'failed', 'cancelled']


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'order']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'payment', 'paid', 'waiting', 'failed', 'error_message',
                       'description', 'status', 'transaction_id', 'provider_channel']


@admin.register(TransactionPhone)
class TransactionPhoneAdmin(admin.ModelAdmin):
    readonly_fields = ['transaction', 'phone_number']


@admin.register(TransactionResponse)
class TransactionResponseAdmin(admin.ModelAdmin):
    readonly_fields = [
        'transaction',
        'success',
        'provider_fee',
        'africastalking_transaction_id',
        'category',
        'provider',
        'provider_ref_id',
        'provider_channel',
        'client_account',
        'product_name',
        'source_type',
        'source',
        'destination_type',
        'destination',
        'value',
        'transaction_fee',
        'description',
        'provider_metadata',
        'transaction_date',
    ]
