from django.db import models
from products.models import Products
from customers.models import Customers


class Product(models.Model):
    name = models.CharField('nome', max_length=100, unique=True)
    price = models.DecimalField('preço', max_digits=6, decimal_places=2)

    class Meta:
        ordering = ('name',)
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'value': self.pk,
            'text': self.name,
            'price': self.price
        }


class Shop(models.Model):
    customer = models.ForeignKey(
        Customers,
        verbose_name='cliente',
        related_name='shops',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'compra'
        verbose_name_plural = 'compras'

    def __str__(self):
        return f'Compra de {self.customer.name} em {self.created}'

class Itens(models.Model):
    item = models.ForeignKey(
        Customers,
        related_name='itens',
        on_delete=models.CASCADE
    )


class Cart(models.Model):
    shop = models.ForeignKey(
        Shop,
        related_name='itens',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Products,
        verbose_name='Produtos',
        related_name='itens',
        on_delete=models.CASCADE
    )
    stock = models.PositiveIntegerField('quantidade')
    price = models.DecimalField('preço', max_digits=6, decimal_places=2)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'item de carrinho'
        verbose_name_plural = 'itens de carrinho'

    def __str__(self):
        if self.shop:
            return f'{self.shop.pk}-{self.pk}-{self.product}'
        return str(self.pk)

    def get_subtotal(self):
        return self.price * (self.stock or 0)
