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

# Create your views here.

def registration(request):
    if request.user.is_authenticated:
        return HttpResponse("<h1>You are Authenticated!!!</h1>")
    else:
        form = RegistrationForm()
        if request.method == 'post' or request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('Your Account has been created successfully!!!')

    context = {
        'form': form,
    }
    return render(request, 'registration.html',context)


def CustomerLogin(request):
    if request.user.is_authenticated:
        return HttpResponse('<h1>You are Already LogedIn!!</h1>')
    else:
        if request.method == 'POST' or request.method == 'post':
            username = request.POST.get('username')
            password = request.POST.get('password')
            customer = authenticate(request, username=username,password=password)
            if customer is not None:
                login(request, customer)
                return HttpResponse("You are logged in Successfully!!")
            else:
                return HttpResponse('Something happening Wrong for login!!')
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

