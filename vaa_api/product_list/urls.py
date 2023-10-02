from django.urls import path
from .views import productList
from .views import productFilter
from .views import singleProduct


urlpatterns = [
    path('product_list/', productList, name="product_list"),
    path('product_list/<int:product_id>/', productFilter, name="product_filter"),
    path('single_product_details/<int:single_product_id>/<int:product_id>/', singleProduct, name="single_product")
]
