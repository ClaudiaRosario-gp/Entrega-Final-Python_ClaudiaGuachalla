from django.http import HttpResponse
from datetime import date, datetime
from django.template import Template, Context
from django.template import loader

from django.shortcuts import render

def index(request):
    return render(request, 'miaplicacion/index.html')


