from rest_framework import serializers
from .models import ProductList


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductList
        fields = ('id', 'product', 'name', 'image_path', 'price', 'stack_quantity', 'grade', 'content', 'manufacturer_from')
