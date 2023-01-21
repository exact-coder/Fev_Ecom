from django.contrib import admin
from .models import Category,Product,ProductImages,VariationValue,Banner,Logo,Favicon,Offer

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name","parent"]
    list_display_links = ["id","parent"]

admin.site.register(Category,CategoryAdmin)

class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    list_display= ['id','name','category','price','is_stock','product_variatin']
    list_display_links = ["id","name"]
    inlines = [ProductImagesAdmin]

admin.site.register(Product,ProductAdmin)

class VariationValueAdmin(admin.ModelAdmin):
    list_display = ['id','name','product','price']
    list_display_links = ['id','name']
admin.site.register(VariationValue,VariationValueAdmin)


class BannerAdmin(admin.ModelAdmin):
    list_display = ['id','title','is_active','short_desc']
    list_display_links = ['id','title']
admin.site.register(Banner,BannerAdmin)

class OfferAdmin(admin.ModelAdmin):
    list_display = ['id','title','discount','is_active']
    list_display_links =['id','title']
admin.site.register(Offer,OfferAdmin)

admin.site.register(Logo)
admin.site.register(Favicon)