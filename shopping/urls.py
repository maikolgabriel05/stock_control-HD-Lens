# shopping/urls.py
from django.urls import path
from shopping import views as v
from . import views
from django.urls import path
from shopping import views as v
from .views import ShopListCreate, CartListCreate, ProductListCreate

app_name = 'shopping'

urlpatterns = [
    path('shopping/', v.shopping, name='shopping'),
    path('cart-items/<int:pk>/', v.cart_items, name='cart_items'),
    path('shops/', ShopListCreate.as_view(), name='shop-list-create'),
    path('carts/', CartListCreate.as_view(), name='cart-list-create'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
]
