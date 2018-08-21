from django.conf.urls import include, url
from django.urls import path
import hello.views

urlpatterns = [
    url(r'^?code=$(?P<code>.*)', hello.views.splogin,  name='logged in')
    # url(r'^(?!\?code=).+$', hello.views.sperr),
    # # path('splogin/', hello.views.splogin)
    # # url(r'^$', hello.views.index, name='index'),
    # # url(r'^db', hello.views.db, name='db'),
    # url(r'^base', hello.views.base, name='db'),
]
