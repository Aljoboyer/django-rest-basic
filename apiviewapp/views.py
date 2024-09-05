from django.shortcuts import render
from . serializers import MovieSerializer
from . models import Movie
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def Allmovies(request):
    ai = Movie.objects.all()

    serializer = MovieSerializer(ai, many = True)

    return Response(serializer.data)

@api_view(['POST'])
def Create_Movie(request):
    
    serializer = MovieSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        res = {'msg': 'Successfully Insert Done'}

        return Response(res)
    
    return Response(serializer.errors)

@api_view(['PUT'])
def Update_Movie(request, pk=None):
    print('Just Checking', request.data, pk)
    id = pk
    movie = Movie.objects.get(pk=id)

    serializer = MovieSerializer(movie, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Full Data Updated'})
    
    return Response(serializer.errors)

@api_view(['PATCH'])
def Patch_Movie(request, pk=None):
    id = pk
    movie = Movie.objects.get(pk=id)

    serializer = MovieSerializer(movie, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'})
    
    return Response(serializer.errors)