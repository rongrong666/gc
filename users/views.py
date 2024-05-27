from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
import json

def index(request):

    # result = 1 / 0

    print('index')

    response = HttpResponse('hello django')

    return response


def say(request):

    print('say')

    return HttpResponse('say func')


def sayhello(request):
    # /users/say
    # url = reverse('abc:cbd')
    #
    # print('sayhello')

    # return HttpResponse('sayhello func')

    # 接收查询字符串参数:
    queryDict = request.GET
    a = queryDict.get('a')
    b = queryDict.get('b')
    alist = queryDict.getlist('a')


    print(a)
    print(b)
    print(alist)


    return HttpResponse('sayhello func')






def routerparams(request, city, year):

    print(city)
    print(year)

    return HttpResponse('routerparams')




def formdata(request):


    qd = request.POST
    a = qd.get('a')
    b = qd.get('b')
    alist = qd.getlist('a')

    print(a)
    print(b)
    print(alist)

    return HttpResponse('routerparams')



def jsonfunc(request):


    # json参数:
    # json_bytes = request.body   # bytes
    # json_str = json_bytes.decode()  # str
    # dict = json.loads(json_str)   # dict

    # dict = json.loads(request.body.decode())
    #
    # print(dict)


    # 请求头信息:
    # length = request.META.get('CONTENT_LENGTH')
    #
    # print(length)


    # 获取其他信息:
    print(request.method)
    print(request.user)
    print(request.path)


    #
    # return HttpResponse('jsonfunc',
    #                     content_type='application/json',
    #                     status=404)

    # return HttpResponseNotFound('jsonhaha')


    dict = {
        'name':'zs',
        'age':12
    }

    list = [{
            'name': 'zs',
            'age': 12
        }]



    return JsonResponse(list, safe=False)







def redirectfunc(request):
    '''进行重定向'''

    print('redirectfunc')

    # reverse('')

    # return redirect('路径')
    # return redirect('/users/json/')


    # return redirect(reverse('abc:cbd'))


    response = HttpResponse()

    response.set_cookie('itcast', 'python', max_age=3600 * 24 * 14)

    return response


































