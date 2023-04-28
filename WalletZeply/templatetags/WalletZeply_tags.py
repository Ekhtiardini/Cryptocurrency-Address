from django import template
from WalletZeply.models import Wallet


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