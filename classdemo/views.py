from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponse






# Create your views here.
class LoginView(View):

    def get(self, request):
        print('LoginView get')

        obj = LoginView()


        return HttpResponse('LoginView get')


    def post(self, request):
        print('LoginView post')
        return HttpResponse('LoginView post')










# def index(request):
#     pass
#
#
#
# xiaoming = LoginView()
# xiaoming.get()
#
#
# LoginView.post()








def my_decorator(func):
    def wrapper(request, *args, **kwargs):
        print('装饰器调用了')
        print('调用的路径:%s' % request.path)
        return func(request, *args, **kwargs)
    return wrapper

def my_decorator2(func):
    def wrapper(request, *args, **kwargs):
        print('装饰器调用了2')
        print('调用的路径2:%s' % request.path)
        return func(request, *args, **kwargs)
    return wrapper


class FirstView(object):

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        return my_decorator(view)

class SecondView(object):

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        return my_decorator2(view)


# @method_decorator(my_decorator, name='dispatch')
class RegisterView(FirstView, SecondView, View):

    def get(self, request):
        print('RegisterView get')
        return HttpResponse('RegisterView get')

    def post(self, request):
        print('RegisterView post')
        return HttpResponse('RegisterView post')
























