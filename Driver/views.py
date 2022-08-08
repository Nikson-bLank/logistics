from functools import partial
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import Driver_DetailSerializer

from .models import Driver_Detail
from .serializers import Driver_DetailSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt


# from Logistics.Driver import serializers
# Create your views here.

def driver_details(request,pk):
    dr = Driver_Detail.objects.get(id=pk)
    serializer = Driver_DetailSerializer(dr)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type= 'application/json')

def driver_list(request):
    dr = Driver_Detail.objects.all()
    serializers = Driver_DetailSerializer(dr, many = True)
    return JsonResponse(serializers.data, safe=False)

@csrf_exempt
def driver_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = Driver_DetailSerializer(data = pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            # return JsonResponse(json_data)
            return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')
        
@csrf_exempt
def driver_update(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id= pythondata.get('id')
        stu = Driver_Detail.objects.get(id=id)
        serializer = Driver_DetailSerializer(stu, data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
@csrf_exempt
def driver_delete(request):
    if request.method =="DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id =pythondata.get('id')
        stu = Driver_Detail.objects.get(id=id)
        stu.delete()
        res = {'msg':'Data Deleted!!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
         

