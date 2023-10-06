from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Oderdetails
from .serializers import OderdetailsSerializer


@api_view(['GET', 'DELETE'])
def user_order_details(request, login_user_id):
    if request.method == 'GET': 
        snippets = Oderdetails.objects.filter(user_id = login_user_id)
        serializer = OderdetailsSerializer(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        snippets = Oderdetails.objects.get(id=request.data['id']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    