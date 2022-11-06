from django.contrib import admin
from .models import *
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display =["id","user","phone","country","city"]
    list_filter = ["country","city",'phone']
    list_display_links = ["id","user"]

admin.site.register(Profile,ProfileAdmin)