from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users # this is the model that is being serialized
        fields = ('name', 'email', 'ph_no', 'added_on')
