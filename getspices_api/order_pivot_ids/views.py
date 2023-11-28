from .models import OrderPivotIds
from global_config.http_response import *
from rest_framework.decorators import api_view
from .serializers import OrderPivotIdsSerializer


@api_view(['GET', 'POST', 'PATCH'])
def order_pivot_ids(request):
    if request.method == 'GET': 
        snippets = OrderPivotIds.objects.all()
        serializer = OrderPivotIdsSerializer(snippets, many=True)
        return HTTP_OK(serializer.data)
    
    elif request.method == 'POST': 
        serializer = OrderPivotIdsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return HTTP_CREATED(serializer.data)
        return HTTP_BAD_REQUEST(serializer.errors)

    elif request.method == 'PATCH':
        user = OrderPivotIds.objects.get(user_id=request.data['user_id'])
        serializer = OrderPivotIdsSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return HTTP_ACCEPTED(serializer.data)
        return HTTP_BAD_REQUEST(serializer.errors)
