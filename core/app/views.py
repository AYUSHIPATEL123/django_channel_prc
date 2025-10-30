from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app(request):
    return HttpResponse("Hello, this is the app view Channels Practice.\n version 1.0.0")