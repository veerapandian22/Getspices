from .models import Payment
from global_config.http_response import *
from .serializers import PaymentSerializer
from rest_framework.decorators import api_view
from global_config.order_maintenance import ORDER_PIVOT_IDS_PAYMENT


@api_view(['GET', 'POST', 'PATCH'])
def payment(request):
    if request.method == 'GET': 
        snippets = Payment.objects.all()
        serializer = PaymentSerializer(snippets, many=True)
        return HTTP_OK(serializer.data)
    
    elif request.method == 'POST':
        user_id = 1  # FIXME: user_id
        req_data = request.data
        bill_id = req_data.pop('bill_id')
        serializer = PaymentSerializer(data=req_data)
        if serializer.is_valid():
            payment_obj = serializer.save()
            payment_id = payment_obj.id

            ORDER_PIVOT_IDS_PAYMENT(user_id, bill_id, payment_id)

            return HTTP_CREATED(serializer.data)
        return HTTP_BAD_REQUEST(serializer.errors)

    elif request.method == 'PATCH':
        user = Payment.objects.get(user_id=request.data['user_id'])
        serializer = PaymentSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return HTTP_OK(serializer.data)
        return HTTP_BAD_REQUEST(serializer.errors)
