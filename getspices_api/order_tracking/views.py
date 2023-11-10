from rest_framework import status
from .models import OrderTracking
from global_config.http_response import *
from rest_framework.decorators import api_view
from .serializers import OrderTrackingSerializer
from global_config.order_maintenance import ORDER_PIVOT_IDS_TRACKING


@api_view(['GET', 'POST', 'PATCH'])
def order_tracking(request):
    if request.method == 'GET':
        snippets = OrderTracking.objects.all()
        serializer = OrderTrackingSerializer(snippets, many=True)
        return HTTP_OK(serializer.data)

    elif request.method == 'POST':
        serializer = OrderTrackingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HTTP_CREATED(serializer.data)
        return HTTP_BAD_REQUEST(serializer.errors)

    elif request.method == 'PATCH':
        user = OrderTracking.objects.get(user_id=request.data['user_id'])
        serializer = OrderTrackingSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return HTTP_OK(serializer.data)
        return HTTP_BAD_REQUEST(serializer.errors)


def order_track(bill_id: int, payment_id: int, user_id: int = None):
    user_id = 1
    query = {"user_id": user_id, "order_placed": 1}
    serializer = OrderTrackingSerializer(data=query)
    if serializer.is_valid():
        order_tracking_obj = serializer.save()
        order_tracking_id = order_tracking_obj.id
        # update order tracking id in pivot table
        ORDER_PIVOT_IDS_TRACKING(user_id, bill_id, payment_id, order_tracking_id)
    