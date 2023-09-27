from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SubscribeSerializer


@api_view(['POST'])
def subscribe(request):
    if request.method == 'POST': # user posting data
        serializer = SubscribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    