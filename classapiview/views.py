from django.shortcuts import render
from . serializers import BookSerializer
from . models import Book
from rest_framework.parsers import JSONParser
from rest_framework.decorators import APIView
from rest_framework.response import Response

class Allbook(APIView):
    def get(self, request):
        ai = Book.objects.all()

        serializer = BookSerializer(ai, many = True)

        return Response(serializer.data)

class Create_Book(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Successfully Insert Done'}

            return Response(res)
        
        return Response(serializer.errors)

class Update_Book(APIView):
    def put(self, request, pk= None):
        id = pk
        books = Book.objects.get(pk=id)

        serializer = BookSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Full Data Updated'})
        
        return Response(serializer.errors)
    
class Patch_Book(APIView):
    def patch(self, request, pk= None):
        id = pk
        Books = Book.objects.get(pk=id)

        serializer = BookSerializer(Books, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        
        return Response(serializer.errors)