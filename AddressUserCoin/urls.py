from django.urls import path
from AddressUserCoin.views import *

app_name = 'AddressUserCoin'

urlpatterns = [
    
    path('<int:wid>',WalletItems,name='Wallet-Items'),
    path('Wallet-Genrate-Coin/<int:wid>',WalletGenrateCoin,name='Wallet-Genrate-Coin'),
    path('Wallet-Genrate-LTC/<int:wid>',WalletGenrateLTC,name='Wallet-Genrate-LTC'),

]