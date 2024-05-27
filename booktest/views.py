from django.db.models import F
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
from booktest.models import HeroInfo, BookInfo


class CreateView(View):

    def post(self, request):
        '''给数据库增加数据'''

        # 1.给数据库中增加数据: create
        HeroInfo.objects.create(
            hname = '猪八戒',
            hgender= 0,
            hcomment='三十六变',
            hbook_id=5
        )


        return HttpResponse('ok')


    def get(self, request):

        # get的使用:
        # try:
        #     hero = HeroInfo.objects.get(pk=1)
        # except Exception as e:
        #     return HttpResponse('查询出错')
        #
        # print(hero)


        # all的使用:
        # heros = HeroInfo.objects.all()
        # print(heros)


        # count = HeroInfo.objects.count()
        # print(count)


        # 过滤查询:
        # filter
        # hero = HeroInfo.objects.filter(id__exact=1)
        # print(hero)


        # heros = HeroInfo.objects.filter(hname__contains='黄')
        # print(heros)

        # heros = HeroInfo.objects.exclude(id__gt=3)
        #         # print(heros)


        # F对象:
        # books = BookInfo.objects.filter(bread__gte=F('bcomment'))
        # print(books)

        # q对象的使用: 表示逻辑关系: 逻辑与  逻辑或  逻辑非
        books = BookInfo.objects.filter(bread__gt=2).filter(bcomment__lt=100)
        print(books)




        return HttpResponse('ok')