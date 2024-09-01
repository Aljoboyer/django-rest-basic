from django.shortcuts import render
from . serializers import ShopSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from . models import Shop
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

# Create your views here.

@csrf_exempt
def shop_create(request):
    if request.method == 'POST':
        json_data = request.body
        #Json to Stream Converting
        stream = io.BytesIO(json_data)
        #stream to python
        pythonData = JSONParser().parse(stream)
        #python to complex conversion
        serializer = ShopSerializer(data=pythonData)

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

        aiq = Shop.objects.get(id=id)

        serializer = ShopSerializer(aiq, data=pythonData, partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Successfully UPDATE Done'}

            json_data = JSONRenderer().render(res)

            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/sjon')
    
    if request.method == 'DELETE':
        json_data = request.body

        stream = io.BytesIO(json_data)

        pythonData = JSONParser().parse(stream)

        id = pythonData.get('id')

        aiqDlt = Shop.objects.get(id = id)

        aiqDlt.delete()

        res = {'msg': 'Successfully Deleted Data'}

        jsonMsg = JSONRenderer().render(res)

        return HttpResponse(jsonMsg, content_type='application/json')
