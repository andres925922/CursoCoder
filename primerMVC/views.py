from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import Familiar
from .service_familiar import get_all_familiares

# Create your views here.

def render_test_view(request):
    return render(request, 'primerMVC/test.html')

def render_view_familiares(request):
    return render(request, 'primerMVC/familiares.html', context={"familiar":get_all_familiares()})
