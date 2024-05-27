from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def set_session(request):
    '''设置session'''

    request.session['itcast001'] = 'python001'


    return HttpResponse('set_session')


def get_session(request):
    '''设置session'''

    value = request.session['itcast001']

    print(value)


    return HttpResponse('get_session')