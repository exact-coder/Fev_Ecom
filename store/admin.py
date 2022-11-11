from django.contrib import admin
from .models import Category,Product,ProductImages

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name","parent"]
    list_display_links = ["id","parent"]

admin.site.register(Category,CategoryAdmin)

class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    list_display= ['id','name','category','price','is_stock','preview_des']
    list_display_links = ["id","name"]
    inlines = [ProductImagesAdmin]

admin.site.register(Product,ProductAdmin)