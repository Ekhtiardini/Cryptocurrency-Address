from django import forms
from WalletZeply.models import Wallet

class WalletZeplyForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['wallet_name','wallet_des','wallet_user']
