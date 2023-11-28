from .models import ProductItem
from global_config.http_response import *
from .serializers import ProductItemSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def productItem(request):
    if request.method == 'GET': 
        snippets = ProductItem.objects.all()
        serializer = ProductItemSerializer(snippets, many=True)
        return HTTP_OK(serializer.data)
    
    elif request.method == 'POST': 
        serializer = ProductItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return HTTP_CREATED(serializer.data)
        return HTTP_BAD_REQUEST(serializer.errors)


@api_view(['GET'])
@permission_classes([AllowAny])
def productFilter(request, product_id):
    if request.method == 'GET':
        snippets = ProductItem.objects.filter(product_id=product_id)
        serializer = ProductItemSerializer(snippets, many=True)
        return HTTP_OK(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def singleItem(request, single_item_id):
    if request.method == 'GET':
        snippets = ProductItem.objects.filter(id = single_item_id)
        serializer = ProductItemSerializer(snippets, many=True)
        return HTTP_OK(serializer.data)
