import os
from gettingstarted.settings import BASE_DIR
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# from .models import Greeting
import hello.models as models
import httplib2
import json
import spotipy
import spotipy.oauth2 as oauth2

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']
# CACHE_PATH = os.path.join(BASE_DIR, 'cache/testcache')
CACHE_PATH = ""
SCOPES = "" \
         "playlist-read-collaborative " \
         "playlist-read-private " \
         "user-follow-read " \
         "user-library-read " \
         "user-top-read " \
         "user-read-recently-played"


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    oauth = oauth2.SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPES
        # cache_path=CACHE_PATH
    )
    auth_url = oauth.get_authorize_url()

    return render(request, 'index.html', {"auth_url": auth_url})


# def db(request):
#     greeting = models.Greeting()
#     greeting.save()
#
#     greetings = models.Greeting.objects.all()
#     return render(request, 'db.html', {'greetings': greetings})


# def base(request):
#     return render(request, 'base.html')


def datapolicy(request):

    return render(request, 'datapolicy.html')


def splogin(request):
    code = request.GET.get('code', '')
    # CHACHE_PATH = os.path.join(BASE_DIR, 'testcache')
    h = oauth2.SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=SCOPES,
                            # cache_path=CHACHE_PATH
                            )
    try:
        token_info = h.get_cached_token()
    except IOError:
    #     raise
       pass

    # if code != '':
    #     token_info = h.get_access_token(code=code)
    try:
        token_info = h.get_access_token(code=code)
    except:
        raise
        # pass
    # tokenJson = json.load(token_info)
    # user_auth.Id =
    user_auth = models.ApiData()
    user_auth.access_token = token_info['access_token']
    user_auth.refresh_token = token_info['refresh_token']
    user_auth.save()
    return render(request, 'splogin.html', {'val1': "",
                                            'val2': ""})
