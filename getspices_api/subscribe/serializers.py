from rest_framework import serializers
from .models import Subscribe


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe # this is the model that is being serialized
        fields = ('email',)
