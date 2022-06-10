import email
from logging import exception
from django.shortcuts import render
from pkg_resources import require
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from .serializers import userSerializer
from django.contrib.auth import get_user_model
User= get_user_model()


def responseFormat(error,message,additional,data):
    return Response({"error":error,"message":str(message),"additionalMessage":additional,"data":data});

@api_view(['POST'])
@permission_classes([AllowAny])
def createUser(request):
    if request.method == "POST":
        try:
            data = request.data 
            user = User.objects.create(email=data['email'],first_name = data['first_name'],last_name=data['last_name'])
            user.set_password(data['password'])
            user.save()
            if User.objects.filter(email = data['email']):
                return responseFormat(False,"Account Created Successfully !!","","")
            else:
                return Response({"error":True,"msg":"Something went wrong try again","additional":"","data":""})
        except Exception as e:
            return responseFormat(True,e,"Error occured in creating user !!","")


@api_view(['GET','PATCH','DELETE'])
def userDetails(request):
    if request.method == "GET":
        try:
            user = User.objects.get(email= request.user)
            serializer = userSerializer(user)
            return responseFormat(False,"","",serializer.data)
        except Exception as e:
            return responseFormat(True,e,"Error occured in getting user details !!","")
    elif request.method =="PATCH":
        try:
            user = User.objects.get(email = request.user)
            data = request.data
            serializer = userSerializer(data = data,instance = user)
            if serializer.is_valid():
                serializer.save()
                return responseFormat(False,"","","")
            else:
                return responseFormat(True,str(serializer.errors),"error ocurred in updating user data","")
        except Exception as e:
            return responseFormat(True,str(e),"erorr occured in updating user ","")
    elif request.method =="DELETE":
        try:
            user = User.objects.get(email = request.user)
            user.delete()
            return responseFormat(False,"Account deleted Successfully!!","","")
        except Exception as e:
            return responseFormat(True,str(e),"erorr occured in deleting user ","")

