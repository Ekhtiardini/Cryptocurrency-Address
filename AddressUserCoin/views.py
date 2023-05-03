from django.contrib import messages
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from WalletZeply.models import Wallet
from AddressUserCoin.models import AddressUC
from AddressUserCoin.forms import AddressUCForm

@login_required(redirect_field_name="my_redirect_field")
def WalletItems(request,wid):
    wallet=get_object_or_404(Wallet,pk=wid)
    context={'wallet':wallet}
    return render(request, 'AddressUserCoin/walletitems.html',context) 

@login_required(redirect_field_name="my_redirect_field")
def WalletGenrateCoin(request,wid):
    wallet=get_object_or_404(Wallet,pk=wid)
    if request.method == "POST":
        form = AddressUCForm(request.POST)
        if form.is_valid():
            form.save()
            context={'wallet':wallet}
            messages.add_message(request,messages.SUCCESS,"You're Created  Successfully")
            return render(request, 'AddressUserCoin/walletitems.html',context) 
        else :
            messages.add_message(request,messages.ERROR,"Your  didn't Submited")
    
    form = AddressUCForm()
    context = {'wallet':wallet,'form':form}
    return render(request, 'AddressUserCoin/genrate_coin_address.html',context) 

@login_required(redirect_field_name="my_redirect_field")
def WalletGenrateLTC(request,wid):
    wallet=get_object_or_404(Wallet,pk=wid)
    if request.method == "POST":
        form = AddressUCForm(request.POST)
        if form.is_valid():
            form.save()
            context={'wallet':wallet}
            messages.add_message(request,messages.SUCCESS,"You're Created  Successfully")
            return render(request, 'AddressUserCoin/walletitems.html',context) 
        else :
            messages.add_message(request,messages.ERROR,"Your  didn't Submited")
    
    form = AddressUCForm()
    context = {'wallet':wallet,'form':form}
    return render(request, 'AddressUserCoin/generate_LTC_adddress.html',context) 

@login_required(redirect_field_name="my_redirect_field")
def WalletGenrateETH(request,wid):
    wallet=get_object_or_404(Wallet,pk=wid)
    if request.method == "POST":
        form = AddressUCForm(request.POST)
        if form.is_valid():
            form.save()
            context={'wallet':wallet}
            messages.add_message(request,messages.SUCCESS,"You're Created  Successfully")
            return render(request, 'AddressUserCoin/walletitems.html',context) 
        else :
            messages.add_message(request,messages.ERROR,"Your  didn't Submited")
    
    form = AddressUCForm()
    context = {'wallet':wallet,'form':form}
    return render(request, 'AddressUserCoin/genrate_ETH_address.html',context) 
