from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer


@api_view(['GET','POST', 'DELETE'])
def cart(request):
    if request.method == 'GET': 
        snippets = Cart.objects.all()
        serializer = CartSerializer(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST': 
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        snippets = Cart.objects.get(id=request.data['id']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_cart(request, user_id):
    if request.method == 'GET':
        snippets = Cart.objects.filter(user_id = user_id)
        serializer = CartSerializer(snippets, many=True)
        return Response(serializer.data)