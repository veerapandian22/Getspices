from django.urls import path
from .views import order_pivot_ids


urlpatterns = [
    path('order_pivot_ids', order_pivot_ids, name="order_pivot_ids")
]
