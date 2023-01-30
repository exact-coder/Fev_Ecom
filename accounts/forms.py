from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile
from django import forms


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name','username','country','city','zipcode','phone','address']
        labels ={'full_name':'Full Name *','username':'User Name','country':'Country *','city':'City *','address': 'Address No ','zipcode':'Zip Code ','phone':'Contact Number'}
        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}),
            'address': forms.Textarea(attrs={'class':'form-control','placeholder':'Your Address.....'}),
            'country': forms.Select(attrs={'class':'custom-select'}),
            'city': forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),
            'zipcode': forms.TextInput(attrs={'class':'form-control','placeholder':'246'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}),
        }

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email','username','password1','password2')
        