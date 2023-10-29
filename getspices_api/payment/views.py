from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PaymentSerializer
from .models import Payment


@api_view(['GET','POST'])
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
    
    