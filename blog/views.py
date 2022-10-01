from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h3>Blog Home</h3>')

def about(request):
    return HttpResponse('<h3>Blog About</h3>')