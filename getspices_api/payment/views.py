from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PaymentSerializer
from .models import Payment


@api_view(['GET', 'POST', 'PATCH'])
def payment(request):
    if request.method == 'GET': 
        snippets = Payment.objects.all()
        serializer = PaymentSerializer(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST': 
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        user = Payment.objects.get(user_id=request.data['user_id'])
        serializer = PaymentSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
