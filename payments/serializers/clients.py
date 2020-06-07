from rest_framework import serializers

from payments.models import Coupon


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            'id',
            'code',
            'amount'
        ]
