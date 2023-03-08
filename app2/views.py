from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2_first(response):
    return HttpResponse('app2 first response')

def app2_second(response):
    return HttpResponse('app2 second response')