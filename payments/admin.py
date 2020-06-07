from django.contrib import admin
from .models import Payment, Coupon, Refund

admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
