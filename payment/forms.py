from django.db.models import fields
from payment.models import BillingAddress
from django import forms
from order.models import Order

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ["first_name","last_name","country","city","address1","address2","zipcode","phone_number"]
        labels ={'first_name':'First Name *','last_name':'Last Name','country':'Country *','city':'City*','address1': 'Address No.1  ','address2':'Address No. 2 ','zipcode':'Zip Code ','phone_number':'Phone Number'}
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Jhon'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Doe'}),
            'country': forms.Select(attrs={'class':'custom-select'}),
            'city': forms.TextInput(attrs={'class':'form-control','placeholder':'Chattogram'}),
            'address1': forms.Textarea(attrs={'class':'form-control','placeholder':'Halishahor,Boropul,Rode-1,Lane-1'}),
            'address2': forms.Textarea(attrs={'class':'form-control','placeholder':'Danmondi,Rode-1,Lane-1'}),
            'zipcode': forms.TextInput(attrs={'class':'form-control','placeholder':'246'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control','placeholder':'0173758778'}),
        }


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method',]
        labels = {'payment_method':'Select Payment Method',}
        widgets={
            'payment_method': forms.Select(attrs={'class':'custom-select'})
        }