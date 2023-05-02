from django.db import models
from CoinZeply.models import Coin
from WalletZeply.models import Wallet

class AddressUC(models.Model):
    addressUC_walletid = models.ForeignKey(Wallet, on_delete=models.SET_NULL,null=True)
    addressUC_Coinid = models.ForeignKey(Coin, on_delete=models.SET_NULL,null=True)
    addressUC_address=models.CharField(max_length=255)
    addressUC_des=models.TextField(null=True)
    addressUC_created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.addressUC_address,self.id