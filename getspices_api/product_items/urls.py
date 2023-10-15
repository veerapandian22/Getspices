from django.urls import path
from .views import productItem
from .views import productFilter
from .views import singleItem


urlpatterns = [
    path('product_item', productItem, name="product_item"),
    path('product_item/<int:product_id>', productFilter, name="product_filter"),
    path('single_item_details/<int:single_item_id>', singleItem, name="single_item")
]
