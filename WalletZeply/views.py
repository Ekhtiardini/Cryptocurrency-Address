from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse 
from django.http import HttpResponseRedirect
from WalletZeply.forms import WalletZeplyForm

@login_required(redirect_field_name="my_redirect_field")
def create_wallet(request):
    if request.method == "POST":
        form = WalletZeplyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"You're Created Wallet Successfully")
        else :
            messages.add_message(request,messages.ERROR,"Your Wallet didn't submited")
        

    form = WalletZeplyForm()
    return render(request, 'WalletZeply/genrateaddress.html',{'form':form})