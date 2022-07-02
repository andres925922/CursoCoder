from django.contrib import admin
from django.urls import path, include
from .views import render_test_view, render_view_familiares

urlpatterns = [
    path('test/', render_test_view ),
    path('familiares/', render_view_familiares)
]