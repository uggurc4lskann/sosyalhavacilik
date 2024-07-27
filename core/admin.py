from django.contrib import admin
from .models import (
    UserInfo,
    About,
    OurPurpose,
    Title
)

@admin.register(UserInfo)
class UserInfoModelAdmin(admin.ModelAdmin):
    list_display = ('id','title')

@admin.register(About)
class UserInfoModelAdmin(admin.ModelAdmin):
    list_display = ('id','content')


@admin.register(OurPurpose)
class UserInfoModelAdmin(admin.ModelAdmin):
    list_display = ('id','content')


@admin.register(Title)
class UserInfoModelAdmin(admin.ModelAdmin):
    list_display = ('id','title')
