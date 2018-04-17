from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('2', home2, name='home2'),
    path('add/', add_record, name='add_record'),
]
