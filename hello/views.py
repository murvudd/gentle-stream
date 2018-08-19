import os
from django.shortcuts import render
from django.utils import translation
from django.http import HttpResponse
import spotipy
from .models import Greeting
import json


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')

    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


def base(request):
    return render(request, 'base.html')


def splogin(request):
    text = os.environ["SPOTIPY_REDIRECT_URI"]
    return render(request, 'splogin.html', {'val': text})
