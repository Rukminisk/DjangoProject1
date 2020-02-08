from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def Test1(request):
    return HttpResponse('<h1> It is a Bright morning</h1>')
