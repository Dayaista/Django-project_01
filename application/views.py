from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
def hero(request):
    return HttpResponse('James Bond')