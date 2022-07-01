from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import Familiar

# Create your views here.

def render_test_view(request):
    return render(request, 'primerMVC/test.html')
