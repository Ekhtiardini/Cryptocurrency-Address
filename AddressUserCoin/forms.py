from django import forms
from AddressUserCoin.models import  AddressUC

class AddressUCForm(forms.ModelForm):
    class Meta:
        model = AddressUC
        fields = ['addressUC_walletid','addressUC_Coinid','addressUC_address','addressUC_des']