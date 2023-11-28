from .models import User
from .serializers import UserSerializer
from global_config.http_response import *
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def user(request):
    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return HTTP_OK(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HTTP_CREATED(serializer.data)
        return HTTP_BAD_REQUEST(serializer.errors)
    