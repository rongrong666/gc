from django.contrib import admin
from .models import BookInfo, HeroInfo

# Register your models here.



# 定义 admin 管理类
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']
    list_per_page = 2




admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)