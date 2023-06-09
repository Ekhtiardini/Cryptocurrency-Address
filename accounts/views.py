from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse 
from django.http import HttpResponseRedirect
from WalletZeply.models import Wallet

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.add_message(request,messages.SUCCESS,"You are Login Success")
                    return redirect("/")
                    
                else :
                    messages.add_message(request,messages.ERROR,"You are Login Failed")
            
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'accounts/login.html',context)
    else:
        return redirect('/')

@login_required(redirect_field_name="my_redirect_field")
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid:
                form.save()
                messages.add_message(request,messages.SUCCESS,"Your SignUp Success")
                return redirect("/") 
            else :
                messages.add_message(request,messages.ERROR,"Your SignUp Failed")
        form = UserCreationForm()
        context = {'form':form}
        return render(request, 'accounts/signup.html',context)
    else:
        return redirect('/')

@login_required(redirect_field_name="my_redirect_field")
def dashboard_view(request):
    return render(request, 'accounts/indexdashboard.html')
