import os
from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting
import json
import spotipy
import spotipy.oauth2 as oauth2


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    oauth = oauth2.SpotifyOAuth(
        client_id=os.environ['CLIENT_ID'],
        client_secret=os.environ['CLIENT_SECRET'],
        redirect_uri=os.environ['SPOTIPY_REDIRECT_URI'],
        scope='user-library-read')
    auth_url = oauth.get_authorize_url()
    return render(request, 'index.html', {"auth_url": auth_url})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


def base(request):
    return render(request, 'base.html')


def sperr(request):

    return render(request, 'temp.html', {'http_context': "str(content)"})


def splogin(request):
    if request.GET.get('error', "test default"):
    # # if request.GET.get('code', "defautl test"):
        val = request.GET['error']

    # val = request.GET['code']
    # request.GET['error']
    # request.GET['status']
    return render(request, 'splogin.html', {'value':  val, 'request': request})
