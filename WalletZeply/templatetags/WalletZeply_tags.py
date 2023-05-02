from django import template
from WalletZeply.models import Wallet
from CoinZeply.models import Coin
from AddressUserCoin.BTC_Genrate import BTC_Gen
from AddressUserCoin.LTC_Genrate import LTC_Gen
from AddressUserCoin.models import AddressUC



register = template.Library()

@register.simple_tag(name='ShowWallet')
def function(userid):
    wallet = Wallet.objects.filter(wallet_user=userid)
    return wallet


@register.simple_tag(name='CountWalletUser')
def function(userid):
    wallet = Wallet.objects.filter(wallet_user=userid).count()
    if wallet < 2:
        return True
    else:
        return False
    
@register.simple_tag(name='ShowWalletItems')
def function(walletid):
    wallet = AddressUC.objects.filter(addressUC_walletid=walletid)
    return wallet

@register.simple_tag(name='ShowCoin')
def function(Coinid):
    coin = Coin.objects.filter(id=Coinid)
    return coin



@register.simple_tag(name='RegBTC')
def function(NameW):
    BTC_add=BTC_Gen(NameW)
    return BTC_add

@register.simple_tag(name='RegLTC')
def function(NameW):
    BTC_add=LTC_Gen(NameW)
    return BTC_add

@register.simple_tag(name='RegBTCWall')
def function(Wallid,Coinid):
    RegAdd = AddressUC.objects.filter(addressUC_walletid=Wallid,addressUC_Coinid=Coinid).count()
    if RegAdd == 0:
        return True
    else:
        return False
    
@register.simple_tag(name='RegLTCWall')
def function(Wallid,Coinid):
    RegAdd = AddressUC.objects.filter(addressUC_walletid=Wallid,addressUC_Coinid=Coinid).count()
    if RegAdd == 0:
        return True
    else:
        print (RegAdd)
        return False