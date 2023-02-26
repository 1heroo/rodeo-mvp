from django.contrib import admin
from .models import MyUser

from django.contrib import admin
from django.contrib.auth.models import Group


class MyUserAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
admin.site.register(MyUser, MyUserAdmin)
admin.site.site_header = 'Rodeo KG'