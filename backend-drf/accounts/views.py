from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    def get(self,request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,req):
        response = {
            "status" : "Request was Permitted"
        }
        return Response(response)