from django.urls import path
from . import views

app_name = 'WalletZeply'

urlpatterns = [
    path('create_wallet/',views.create_wallet,name='create_wallet'),
]