from django.contrib import admin
from CoinZeply.models import Coin

class CoinAdmin(admin.ModelAdmin):
    search_fields = ['coin_name']
    empty_value_display = '-empty-'
    list_display = ('coin_sign', 'coin_name' ,'coin_author','concoin_des','coin_image')
    list_filter = ('coin_sign','coin_author')

admin.site.register(Coin,CoinAdmin)
# Register your models here.
