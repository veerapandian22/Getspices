from .models import Cart
from .serializers import CartSerializer
from global_config.http_response import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def cart(request):
    if request.method == 'GET': 
        snippets = Cart.objects.all()
        serializer = CartSerializer(snippets, many=True)
        return HTTP_OK(serializer.data)
    
    elif request.method == 'POST': 
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return HTTP_CREATED(serializer.data)
        return HTTP_BAD_REQUEST(serializer.errors)
    
    elif request.method == 'DELETE':
        snippets = Cart.objects.get(id=request.data['id']).delete()
        return HTTP_NO_CONTENT()


# =========================================================================================================
@api_view(['GET'])
@permission_classes([AllowAny])
def user_cart(request, user_id):
    if request.method == 'GET':
        snippets = Cart.objects.filter(user_id=user_id)
        serializer = CartSerializer(snippets, many=True)
        return HTTP_OK(serializer.data)
