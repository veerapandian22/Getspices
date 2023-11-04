from cart.models import Cart
from .models import BillingAddress
from orders.models import Oderdetails
from global_config.http_response import *
from rest_framework.decorators import api_view
from .serializers import BillingAddressSerializer
from global_config.order_maintenance import ORDER_PIVOT_IDS_BILLING


@api_view(['GET', 'POST'])
def billing_address(request):
    if request.method == 'GET': 
        snippets = BillingAddress.objects.all()
        serializer = BillingAddressSerializer(snippets, many=True)
        return HTTP_OK(serializer.data)
    
    elif request.method == 'POST':
        user_id = 1  # FIXME: user_id
        order_id = []
        serializer = BillingAddressSerializer(data=request.data)
        if serializer.is_valid():
            billing_obj = serializer.save()
            billing_id = billing_obj.id

            # copy data from cart to order_details table & remove products from cart.
            cart_snippets = Cart.objects.filter(user_id=user_id)
            for row in cart_snippets.values():
                order_obj = Oderdetails.objects.create(**row)
                order_id.append(order_obj.id)
            if cart_snippets:
                Cart.objects.filter(user_id=user_id).delete()

            ORDER_PIVOT_IDS_BILLING(user_id, billing_id, order_id)

            return HTTP_CREATED(serializer.data)
        return HTTP_BAD_REQUEST(serializer.errors)
