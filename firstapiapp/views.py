from django.shortcuts import render
from . models import Aiquest
from . serializers import AiquestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from . models import Students
from . serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

# Create your views here.
def aiquest_info(request):
    ai = Aiquest.objects.all()
    serializer = AiquestSerializer(ai, many = True)
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type = 'application/json')

def aiquest_individual(request, pk):
    ai = Aiquest.objects.get(id=pk)

    serializer = AiquestSerializer(ai)

    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type = 'application/json')

def get_all_students(request):

    student = Students.objects.all()

    serializer = StudentSerializer(student, many = True)

    jsonData = JSONRenderer().render(serializer.data)

    return HttpResponse(jsonData, content_type='application/json')

@csrf_exempt
def aiquest_create(request):
    if request.method == 'POST':
        json_data = request.body
        #Json to Stream Converting
        stream = io.BytesIO(json_data)
        #stream to python
        pythonData = JSONParser().parse(stream)
        #python to complex conversion
        serializer = AiquestSerializer(data=pythonData)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Successfully Insert Done'}

            json_data = JSONRenderer().render(res)

            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/sjon')

    if request.method == 'PUT':
        json_data = request.body
        
        stream = io.BytesIO(json_data)

        pythonData = JSONParser().parse(stream)

        id = pythonData.get('id')

        aiq = Aiquest.objects.get(id=id)

        serializer = AiquestSerializer(aiq, data=pythonData, partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Successfully UPDATE Done'}

            json_data = JSONRenderer().render(res)

            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/sjon')


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body

        stream = io.BytesIO(json_data)

        pythondata = JSONParser().parse(stream)

        serializer = StudentSerializer(data=pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Successfully Insert Done'}

            json_data = JSONRenderer().render(res)

            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/sjon')
    
    if request.method == 'PUT':
        json_data = request.body

        stream = io.BytesIO(json_data)

        pythondata = JSONParser().parse(stream)

        id = pythondata.get('id')

        std = Students.objects.get(id=id)

        serializer = StudentSerializer(std, data=pythondata, partial=True)

        if serializer.is_valid():

            serializer.save()
            res = {'msg': 'Successfully UPDATE Done'}

            json_data = JSONRenderer().render(res)

            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/sjon')