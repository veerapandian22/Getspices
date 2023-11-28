from global_config.http_response import *
from .serializers import SubscribeSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes


@api_view(['POST'])
@permission_classes([AllowAny])
def subscribe(request):
    if request.method == 'POST':
        serializer = SubscribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HTTP_CREATED(serializer.data)
        return HTTP_BAD_REQUEST(serializer.errors)
