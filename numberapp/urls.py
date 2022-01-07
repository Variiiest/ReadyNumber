from django.urls import path
from .views import calculate, main, get_answer
urlpatterns = [
    path('',main),
    path('calculate/<int:number1>/<int:number2>/',calculate),
    path('get_answer/<int:id>/', get_answer),
]