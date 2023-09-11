from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    return HttpResponse('hi this is the home page')

