from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Checkout
from .serializers import CheckoutSerializer
from cart.models import Cart
from cart.serializers import CartSerializer
from user_order_details.models import Oderdetails
from user_order_details.serializers import OderdetailsSerializer

@api_view(['GET','POST'])
def checkout(request):
    if request.method == 'GET': 
        snippets = Checkout.objects.all()
        serializer = CheckoutSerializer(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST': 
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # copy data from cart to user_order_details table & remove product from cart.
            # FIXME: user_id
            cart_snippets = Cart.objects.filter(user_id = 1)
            for row in cart_snippets.values():
                Oderdetails.objects.create(**row)
            if cart_snippets:
                Cart.objects.get(user_id = 1).delete()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    