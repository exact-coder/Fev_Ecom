from django import forms

class CouponCodeForm(forms.Form):
    code = forms.CharField(max_length=50, required=False,label="", widget=forms.TextInput(attrs={'class':"form-control border-0 p-4",'placeholder':'Coupon Code'}))