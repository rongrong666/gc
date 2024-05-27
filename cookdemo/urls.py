from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^setcook/$', views.setfunc),
    url(r'^getcook/$', views.getcookfun),
]






