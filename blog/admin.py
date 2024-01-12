from django.contrib import admin
from .models import post,categories,UserProfile,Comment,ContactMessage
# Register your models here.


class post_class(admin.ModelAdmin):
    list_display=('id','author','title','content','date','category')

admin.site.register(post,post_class)


class postcate(admin.ModelAdmin):
    list_display=('cate',)
admin.site.register(categories,postcate)


class pos_profile(admin.ModelAdmin):
    list_display=('id','user','picture','bio','facebook','twitter','instagram')
admin.site.register(UserProfile,pos_profile)


class Comment_class(admin.ModelAdmin):
    list_display=('name','email','text','blog_post')
admin.site.register(Comment,Comment_class)

class conmi(admin.ModelAdmin):
    list_display=('name','email','message')
admin.site.register(ContactMessage,conmi)