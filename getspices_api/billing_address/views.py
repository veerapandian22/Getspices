from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BillingAddress
from .serializers import BillingAddressSerializer
from cart.models import Cart
from orders.models import Oderdetails

@api_view(['GET','POST'])
def billing_address(request):
    if request.method == 'GET': 
        snippets = BillingAddress.objects.all()
        serializer = BillingAddressSerializer(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST': 
        serializer = BillingAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # copy data from cart to order_details table & remove products from cart.
            # FIXME: user_id
            cart_snippets = Cart.objects.filter(user_id = 1)
            for row in cart_snippets.values():
                Oderdetails.objects.create(**row)
            if cart_snippets:
                Cart.objects.get(user_id = 1).delete()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    