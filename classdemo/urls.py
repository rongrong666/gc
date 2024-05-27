from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view()),
    # url(r'^register/$', views.my_decorator(views.RegisterView.as_view())),
    url(r'^register/$', views.RegisterView.as_view()),
]

















