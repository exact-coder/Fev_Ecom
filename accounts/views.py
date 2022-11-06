from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

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