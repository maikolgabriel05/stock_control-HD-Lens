from rest_framework import serializers
from customers.models import Customers
from shopping.models import Shop, Product, Cart, Itens


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['pk', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itens
        fields = 'all'


class CartSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Cart
        fields = ['product', 'stock', 'price']


class ShopSerializer(serializers.Serializer):
    customer = serializers.IntegerField()
    itens = CartSerializer(many=True)

    def create(self, validated_data):
        customer_id = validated_data.pop('customer')
        itens_data = validated_data.pop('itens')

        shop = Shop.objects.create(customer_id=customer_id)

        for item_data in itens_data:
            product_id = item_data.pop('product')
            product = Product.objects.get(pk=product_id)
            Cart.objects.create(shop=shop, product=product, **item_data)

        return shop
