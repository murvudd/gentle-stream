import os
from gettingstarted.settings import BASE_DIR
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Greeting
import httplib2
import json
import spotipy
import spotipy.oauth2 as oauth2

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    oauth = oauth2.SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope='user-library-read',
        cache_path=os.path.join(BASE_DIR, 'cache/testcache')
    )
    auth_url = oauth.get_authorize_url()

    return render(request, 'index.html', {"auth_url": auth_url})


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})


def base(request):
    return render(request, 'base.html')


# def sperr(request):
#     return render(request, 'temp.html', {'http_context': "str(content)"})


def splogin(request):
    code = request.GET.get('code', '')
    CHACHE_PATH = os.path.join(BASE_DIR, 'testcache')
    SCOPE=""
    h = oauth2.SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=SCOPE, cache_path=CHACHE_PATH)
    try:
        token_info = h.get_cached_token()
    except IOError:
        pass

    if code != '':
        token_info = h.get_access_token(code=code)
    # tokenJson = json.load(token_info)
    access_token = token_info['access_token']
    refresh_token = token_info['refresh_token']

    return render(request, 'splogin.html', {'val1':  access_token,
                                            'val2': refresh_token})
