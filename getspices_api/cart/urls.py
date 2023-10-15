from django.urls import path
from .views import cart, user_cart


urlpatterns = [
    path('cart', cart, name="cart"),
    path('cart/<int:user_id>', user_cart, name="user_cart")
]
