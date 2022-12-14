from django.contrib import admin
from .models import Cart,Order

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ["id","user","item","quantity"]
    list_display_links = ["id",]

admin.site.register(Cart,CartAdmin)

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ["id","user","orderitems"]
#     list_display_links = ["id",]

admin.site.register(Order)