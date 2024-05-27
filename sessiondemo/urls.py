from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^setsession/$', views.set_session),
    url(r'^getsession/$', views.get_session),
]






