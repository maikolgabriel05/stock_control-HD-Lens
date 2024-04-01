#Projetodjango/serializers.py
from rest_framework import serializers
from customers.models import Customers
from shopping.models import Shop, Product, Cart


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['pk', 'name']

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['pk', 'customer', 'created']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'price']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['pk', 'shop', 'product', 'stock', 'price']
