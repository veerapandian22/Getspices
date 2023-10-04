from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProductList
from .serializers import ProductListSerializer


@api_view(['GET','POST'])
def productList(request):
    if request.method == 'GET': 
        snippets = ProductList.objects.all()
        serializer = ProductListSerializer(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST': 
        serializer = ProductListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def productFilter(request, product_id):
    if request.method == 'GET':
        snippets = ProductList.objects.filter(product_id = product_id)
        serializer = ProductListSerializer(snippets, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def singleProduct(request, single_product_id):
    if request.method == 'GET':
        snippets = ProductList.objects.filter(id = single_product_id)
        serializer = ProductListSerializer(snippets, many=True)
        return Response(serializer.data)
