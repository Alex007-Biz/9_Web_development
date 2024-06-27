from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    data = {
        'caption':"Plitkanadom.ru - Django"
    }
    return render(request, 'main/index.html', data)

def new(request):
    return render(request, 'main/new.html')

def goods(request):
    return render(request, 'main/goods.html')

def service(request):
    return render(request, 'main/service.html')