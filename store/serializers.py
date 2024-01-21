from decimal import Decimal
from . import models
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Collection
        fields = ['id', 'name', 'products_count']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = ['id', 'street', 'city']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ['id', 'plased_at', 'delivery_at', 'payment_status', 'order_items']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = ['id', 'product']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = ['id', 'cart_items']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = ['id', 'product']


