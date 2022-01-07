from rest_framework import status
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Numbers
import time

waiting_time= 0
def queueSleep(waiting_time=10):
    time.sleep(waiting_time)


@api_view(['GET'])
def calculate(request, number1, number2):
    data= {'number1':number1, 'number2':number2,'answer':number1+number2}
    datasave= Numbers.objects.create(number1= number1, number2= number2, answer= number1+number2)
    global waiting_time
    waiting_time+= 10
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_answer(request, id):
    global waiting_time
    queueSleep(waiting_time)
    waiting_time= 0
    if waiting_time==0:
        d= Numbers.objects.filter(id= id)
        data = {'answer':d[0].answer}
        return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def main(request):
    data= {'response':'Hi from test API'}
    return Response(data, status= status.HTTP_200_OK)

