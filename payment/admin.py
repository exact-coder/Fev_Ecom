from django.contrib import admin
from payment.models import BillingAddress

# Register your models here.

class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','phone_number','country','city','address']
    list_display_links = ['id','first_name','phone_number']
    list_filter =['phone_number','country']

admin.site.register(BillingAddress,BillingAddressAdmin)
