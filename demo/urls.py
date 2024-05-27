"""mymy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import users.urls
from users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls', namespace='abc')),
    # url(r'^users/index', include(users.urls)),
    # url(r'^users/index', views.index)

    url(r'^cook/', include('cookdemo.urls')),
    url(r'^session/', include('sessiondemo.urls')),
    url(r'^classdemo/', include('classdemo.urls')),
    url(r'^booktest/', include('booktest.urls')),
    url(r'^temp/', include('tempdemo.urls')),
]

# url = reverse('abc:cbd')

# url:  /users/say


# 127.0.0.1:8000/blog/index/

# 路由:




















