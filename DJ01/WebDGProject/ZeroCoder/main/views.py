from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')
#
# def data(request):
#     return HttpResponse("<h1>Это страница Data на Django!!</h1>")
#
# def test(request):
#     return HttpResponse("<h1>Это страница Test на Django!</h1>")