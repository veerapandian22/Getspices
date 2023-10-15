from django.urls import path
from .views import billing_address


urlpatterns = [
    path('billing_address', billing_address, name="billing_address")
]
