from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status  # Import status module
from user_app.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from user_app import models

@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({'msg':'Logout Successful!'}, status=status.HTTP_200_OK)

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)  # Pass data as the argument
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = 'Registration Successfull'
            data['username'] = account.username
            data['email'] =  account.email
            #manually creating simple token, we have used signal here in model.py file
            token = Token.objects.get(user=account).key
            data['token'] = token
            
        else:
            data = serializer.errors
            
        return Response(data, status=status.HTTP_201_CREATED)