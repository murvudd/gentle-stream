from django.conf.urls import include, url
from django.urls import path
import hello.views

from django.contrib import admin
admin.autodiscover()


# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^base', hello.views.base, name='db'),
    path('admin/', admin.site.urls),
    url(r'sp/(?P<code>[\w.@+-]+)$', hello.views.splogin),

    # url(r'(code=(?P<code>.*))', hello.views.splogin,  name='logged in')

    # url(r'^sp\?error', hello.views.sperr),
    # url(r'^sp/(?!\?code=).+$', hello.views.sperr)
    #
    #
    # url(r'^sp/(?P<code>.+)', hello.views.splogin)
    # url(r'^sp(?P<code>(.*))', hello.views.splogin)
    #
    #
    # path('^code=', hello.views.splogin),
    # url(r'^sp', hello.views.splogin)
    # url(r'^sp/', hello.views.splogin)
    # path('sp/', include('hello.urls'))
    # path('polls/', include('polls.urls'))
    # https://gentle-stream.herokuapp.com/sp?error=access_denied
]
