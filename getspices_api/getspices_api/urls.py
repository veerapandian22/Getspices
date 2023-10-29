"""
URL configuration for getspices_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import urls as user_urls
from subscribe import urls as subscribe_urls
from contact import urls as contact_urls
from products import urls as product_urls
from product_items import urls as product_item_urls
from cart import urls as cart_urls
from billing_address import urls as billing_address_urls
from orders import urls as orders_urls
from payment import urls as payment_urls
from order_pivot_ids import urls as order_pivot_urls
from order_tracking import urls as order_tracking_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('', include(user_urls)),
        path('', include(subscribe_urls)),
        path('', include(contact_urls)),
        path('', include(product_urls)),
        path('', include(product_item_urls)),
        path('', include(cart_urls)),
        path('', include(billing_address_urls)),
        path('', include(orders_urls)),
        path('', include(payment_urls)),
        path('', include(order_pivot_urls)),
        path('', include(order_tracking_urls)),
    ])),
]
