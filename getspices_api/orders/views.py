from .models import Oderdetails
from global_config.http_response import *
from .serializers import OderdetailsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def orders(request, login_user_id):
    if request.method == 'GET': 
        snippets = Oderdetails.objects.filter(user_id=login_user_id)
        serializer = OderdetailsSerializer(snippets, many=True)
        return HTTP_OK(serializer.data)
    
    elif request.method == 'DELETE':
        snippets = Oderdetails.objects.get(id=request.data['id']).delete()
        return HTTP_NO_CONTENT()
    