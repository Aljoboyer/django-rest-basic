from django.shortcuts import render
from . serializers import UserSerializer
from . models import User
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

# Create your views here.
class UserList(GenericAPIView, ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class CreateUser(GenericAPIView, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)