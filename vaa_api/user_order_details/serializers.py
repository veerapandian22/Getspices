from rest_framework import serializers
from .models import Oderdetails


class OderdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oderdetails
        fields = ('id', 'user', 'product', 'product_list', 'product_name', 'product_path', 'price', 'quantity', 'total')
