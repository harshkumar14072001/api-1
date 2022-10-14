from http.client import HTTPResponse
from django.shortcuts import render
import io
from .models import Student
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# from gs3.api import serializers

def student_api(request):
    if request.method == 'GET':
        json_data =request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data =  JSONRenderer().render(serializer.data)
            return HTTPResponse(json_data,content_type='application/json')
            
        stu= Student.object.all()
        serializer=StudentSerializer(stu,many=True)
        json_data =  JSONRenderer().render(serializer.data)
        return HTTPResponse(json_data,content_type='application/json')
            

    if request.method == 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        serializer = StudentSerializer(data= pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HTTPResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HTTPResponse(json_data,content_type='application/json')
        
