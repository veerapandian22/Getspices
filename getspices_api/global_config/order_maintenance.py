from order_pivot_ids.serializers import OrderPivotIdsSerializer
from order_pivot_ids.models import OrderPivotIds


def ORDER_PIVOT_IDS_BILLING(user_id: int, billing_id: int, order_ids: list):
    for order_id in order_ids:
        query = {'user_id': user_id, 'billing_id': billing_id, 'order_id': order_id}
        serializer = OrderPivotIdsSerializer(data=query)
        if serializer.is_valid():
            serializer.save()


def ORDER_PIVOT_IDS_PAYMENT(user_id: int, bill_id: int, payment_id: int):

    queryset = OrderPivotIds.objects.filter(user_id=user_id, billing_id=bill_id).values_list('id', flat=True)
    for i in range(queryset.count()):
        query = {'payment_id': payment_id}
        obj = OrderPivotIds.objects.get(id=queryset[i])
        serializer = OrderPivotIdsSerializer(instance=obj, data=query, partial=True)
        if serializer.is_valid():
            serializer.save()
