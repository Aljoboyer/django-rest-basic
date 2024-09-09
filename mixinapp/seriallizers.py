from rest_framework import serializers
from . models import Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'phone', 'email', 'password']