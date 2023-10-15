from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProductItem
from .serializers import ProductItemSerializer


@api_view(['GET','POST'])
def productItem(request):
    if request.method == 'GET': 
        snippets = ProductItem.objects.all()
        serializer = ProductItemSerializer(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST': 
        serializer = ProductItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def productFilter(request, product_id):
    if request.method == 'GET':
        snippets = ProductItem.objects.filter(product_id = product_id)
        serializer = ProductItemSerializer(snippets, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def singleItem(request, single_item_id):
    if request.method == 'GET':
        snippets = ProductItem.objects.filter(id = single_item_id)
        serializer = ProductItemSerializer(snippets, many=True)
        return Response(serializer.data)
