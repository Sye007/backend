from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import food
from rest_framework import serializers

class foodserializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = '__all__'
    

# Create your views here.

#def signup(request):
    #return HttpResponse("Hello world")

@api_view (['Get'])
def hello(request):
    allfood = food.objects.all()
    serializer = foodserializer(allfood, many=True)
    return Response(serializer.data)


@api_view (['Post'])
def createfood(request):
    return Response(request.data)




