from django.urls import path
from .views import user_order_details


urlpatterns = [
    path('user_order_details/<int:login_user_id>/', user_order_details, name="user_order_details")
]
