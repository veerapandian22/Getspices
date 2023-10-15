from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'hsn_code', 'product_code', 'product_name', 'product_img_path', 'product_desc',
                  'product_price', 'stack_qty', 'available_qty', 'manufacturer_from')
