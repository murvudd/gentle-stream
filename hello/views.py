import os
from django.shortcuts import render
# import django.http.request as http_request
from django.utils import translation
from django.http import HttpResponse
import spotipy
from .models import Greeting
import json
import spotipy
import spotipy.oauth2 as oauth2
import httplib2


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


def spauth(request):

    oauth = oauth2.SpotifyOAuth(
        client_id=os.environ['CLIENT_ID'],
        client_secret=os.environ['CLIENT_SECRET'],
        redirect_uri=os.environ['SPOTIPY_REDIRECT_URI'],
        scope='user-library-read')
    auth_url = oauth.get_authorize_url()
    (resp_headers, content) = httplib2.Http().request(auth_url, "GET")
    # HttpResponse()
    return render(request, 'temp.html', {'http_context': str(content)})


def splogin(request):
    # text = os.environ
    text = os.environ["SPOTIPY_REDIRECT_URI"]
    # text = "text zy pythona"
    return render(request, 'splogin.html', {'val': text})
