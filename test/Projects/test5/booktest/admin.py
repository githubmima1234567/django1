from django.contrib import admin
from .models import *
#注册方法一：

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle', 'bpub_date']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
admin.site.register(UserInfo)

#注册方法二：
# @admin.register(BookInfo)
# class BookInfoAdmin(admin.ModelAdmin):
#     list_display = ['btitle', 'bpub_date']


