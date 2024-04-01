# shopping/admin.py
from django.contrib import admin
from .models import Shop, Product, Cart


class CartInline(admin.TabularInline):
    model = Cart
    extra = 0


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    inlines = (CartInline,)
    list_display = ('__str__', 'created')
    search_fields = ('customer',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'price')
    search_fields = ('name',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_sale_customer', 'stock', 'price')  # Adicionando 'get_sale_customer' ao list_display
    search_fields = ('shop__customer__name', 'product__name')  # Alterando 'sale__customer' para 'shop__customer__name'

    def get_sale_customer(self, obj):
        return obj.shop.customer.name  # Substituindo 'sale__customer' por 'shop__customer__name'

    get_sale_customer.short_description = 'Sale Customer'  # Definindo o nome da coluna no admin

