from django.contrib import admin
from django.urls import path, include
from .views import render_test_view

urlpatterns = [
    path('test/', render_test_view )
]