from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderTrackingSerializer
from .models import OrderTracking


@api_view(['GET', 'POST', 'PATCH'])
def order_tracking(request):
    if request.method == 'GET':
        snippets = OrderTracking.objects.all()
        serializer = OrderTrackingSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderTrackingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        user = OrderTracking.objects.get(user_id=request.data['user_id'])
        serializer = OrderTrackingSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
