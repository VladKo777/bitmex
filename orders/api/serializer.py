from rest_framework import serializers
from orders.models import Order


class Subscribe(serializers.Serializer):
    account = serializers.CharField(max_length=200)
    action = serializers.CharField(max_length=20)


class GetAccount(serializers.Serializer):
    account = serializers.CharField(max_length=200)


class GetOrders(serializers.Serializer):
    account = serializers.CharField(max_length=200)
    symbol = serializers.CharField(max_length=200)
    ord_status = serializers.CharField(max_length=200, required=False)


class CreateOrderSerializer(serializers.ModelSerializer):
    account = serializers.CharField(max_length=200)
    symbol = serializers.CharField(max_length=200)
    ordType = serializers.CharField(max_length=200)
    orderQty = serializers.CharField(max_length=200)
    side = serializers.CharField(max_length=200)

    class Meta:
        model = Order
        fields = ('account', 'symbol', 'ordType', 'orderQty', 'side',)
