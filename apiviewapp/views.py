from django.shortcuts import render
from . serializers import MovieSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from . models import Movie
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def Allmovies(request):
    ai = Movie.objects.all()

    serializer = MovieSerializer(ai, many = True)

    return Response(serializer.data)
