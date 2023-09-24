from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users
from .serializers import UsersSerializer


@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET': # user requesting data 
        snippets = Users.objects.all()
        serializer = UsersSerializer(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST': # user posting data
        print(request.data)
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
