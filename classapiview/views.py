from django.shortcuts import render
from . serializers import BookSerializer
from . models import Book
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def Allbook(request):
    ai = Book.objects.all()

    serializer = BookSerializer(ai, many = True)

    return Response(serializer.data)

@api_view(['POST'])
def Create_Book(request):
    
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        res = {'msg': 'Successfully Insert Done'}

        return Response(res)
    
    return Response(serializer.errors)

@api_view(['PUT'])
def Update_Book(request, pk=None):
    print('Just Checking', request.data, pk)
    id = pk
    Book = Book.objects.get(pk=id)

    serializer = BookSerializer(Book, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Full Data Updated'})
    
    return Response(serializer.errors)

@api_view(['PATCH'])
def Patch_Book(request, pk=None):
    id = pk
    Book = Book.objects.get(pk=id)

    serializer = BookSerializer(Book, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'})
    
    return Response(serializer.errors)