from django.urls import path
from .views import orders


urlpatterns = [
    path('orders/<int:login_user_id>', orders, name="orders")
]
