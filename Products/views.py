from django.shortcuts import render
from django.http import HttpResponse

def index1(request):
    return HttpResponse('<h1 style="text-align:center;"> Errooorrrrrr </h1>')

def index2(request):
    return HttpResponse('<h1 style="text-align:center;"> You have an exception </h1>')

def index3(request, data):
    return HttpResponse(f'''<h1 style="text-align:center;"> Hello, {data}</h1>
                        <p style="text-align:center;">You are our special client.</p>''')