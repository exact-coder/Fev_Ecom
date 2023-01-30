from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.views.generic import TemplateView
from order.models import Cart,Order
from payment.models import BillingAddress
from payment.forms import BillingAddressForm
from accounts.models import Profile
from accounts.forms import ProfileForm,RegistrationForm
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.


def registration(request):
    if request.user.is_authenticated:
        return redirect('HomePage')
    else:
        if request.method == 'post' or request.method == 'POST':
            fullname = request.POST.get('fullname')
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                register = User.objects.create_user(user_name=username,email =email,password =password1)
                register.save()
                return redirect('login')

    return render(request, 'registration.html')        

@login_required
def LogoutPage(request):
    logout(request)
    return redirect('login')



def CustomerLogin(request):
    if request.user.is_authenticated:
        return redirect('HomePage')
    else:
        if request.method == 'POST' or request.method == 'post':
            username = request.POST.get('username')
            password = request.POST.get('password')
            customer = authenticate(request, username=username,password=password)
            if customer is not None:
                login(request, customer)
                return redirect('HomePage')
            else:
                return redirect('login')
    return render(request, 'login.html')

# Customers Profile

class ProfileView(TemplateView):
    def get(self,request,*args, **kwargs):
        orders = Order.objects.filter(user=request.user, ordered=True)

        billingaddress = BillingAddress.objects.get(user=request.user)
        billingaddress_form = BillingAddressForm(instance=billingaddress)

        profile_obj = Profile.objects.get(user = request.user)
        profileForm = ProfileForm(instance=profile_obj)

        context = {
            'orders' : orders,
            'billingaddress' :billingaddress_form,
            'profileForm' : profileForm,
        }
        return render(request, 'store/profile.html',context)

    def post(self,request,*args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            billingaddress = BillingAddress.objects.get(user=request.user)
            billingaddress_form = BillingAddressForm(request.POST,instance=billingaddress)
            profile_obj = Profile.objects.get(user = request.user)
        profileForm = ProfileForm(request.POST,instance=profile_obj)
        if billingaddress_form.is_valid() :
            billingaddress_form.save()
            return redirect('profile')
        if profileForm.is_valid():
            profileForm.save()
            return redirect('profile')

