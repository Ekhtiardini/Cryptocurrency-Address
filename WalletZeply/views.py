from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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