from django.conf.urls import include, url
from django.urls import path
import hello.views

urlpatterns = [
    path('^code=', hello.views.splogin),
    # path('splogin/', hello.views.splogin)
    # url(r'^$', hello.views.index, name='index'),
    # url(r'^db', hello.views.db, name='db'),
    # url(r'^base', hello.views.base, name='db'),
]