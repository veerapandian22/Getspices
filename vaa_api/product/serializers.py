from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'image_path', 'price', 'stack_quantity', 'grade', 'manufacturer_from', 'filter')
