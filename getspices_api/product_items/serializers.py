from rest_framework import serializers
from .models import ProductItem


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ('id','product_id', 'item_code', 'item_name', 'item_grade', 'item_img_path',
                  'item_desc', 'item_price', 'stack_qty', 'available_qty', 'manufacturer_from')
