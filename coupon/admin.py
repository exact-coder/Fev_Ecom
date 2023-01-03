from django.contrib import admin
from coupon.models import Coupon

# Register your models here.

class CouponAdmin(admin.ModelAdmin):
    list_display = ["id","code","valid_from","valid_to","discount","active"]
    list_display_links = ["id","code","discount"]

admin.site.register(Coupon,CouponAdmin)
