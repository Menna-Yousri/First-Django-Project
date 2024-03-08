from django.shortcuts import render
from django.http import HttpResponse

def customer1(request):
    return HttpResponse('<h1 style="text-align:center;"> This is the first customer profile </h1>')

def customern(request, data):
    return HttpResponse(f'<h1 style="text-align:center;"> This is the {data} customer profile')