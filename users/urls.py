from django.conf.urls import url
from . import views

urlpatterns = [
    url('^index/$', views.index),
    url('^sayhello', views.sayhello),
    url('^say', views.say, name='cbd'),
    url('^form/$', views.formdata),
    url('^json/$', views.jsonfunc),
    url('^redirect/$', views.redirectfunc),
    url('^router/(?P<city>[a-zA-Z0-9]+)/(?P<year>\d{4})', views.routerparams),
]






