from django.contrib import admin
from WalletZeply.models import Wallet

class WalletAdmin(admin.ModelAdmin):
    date_hierarchy = 'wallet_created_date'
    search_fields = ['wallet_name']
    empty_value_display = '-empty-'
    list_display = ('wallet_name', 'wallet_user' ,'wallet_des','wallet_created_date')
    list_filter = ('wallet_user',)

admin.site.register(Wallet,WalletAdmin)
# Register your models here.