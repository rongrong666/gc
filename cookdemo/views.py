from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def setfunc(request):
    '''设置cookie'''

    response = HttpResponse('setfunc cook')

    response.set_cookie('name', 'zs', max_age=600)

    return response


def getcookfun(request):
    '''读取cookie'''

    value = request.COOKIES.get('name')

    print(value)

    return HttpResponse('getcookfun cook')