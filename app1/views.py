from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_first(response):
    return HttpResponse('<marquee><h1>app1 first response<h1/><marquee/>')

def app1_second(response):
    return HttpResponse('app1 second response')