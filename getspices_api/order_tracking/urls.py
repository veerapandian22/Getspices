from django.urls import path
from .views import order_tracking


urlpatterns = [
    path('order_tracking', order_tracking, name="order_tracking")
]
