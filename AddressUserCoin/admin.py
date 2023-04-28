from django.contrib import admin
from AddressUserCoin.models import AddressUC

class AddressUCAdmin(admin.ModelAdmin):
    search_fields = ['addressUC_des']
    date_hierarchy = 'addressUC_created_date'
    empty_value_display = '-empty-'
    list_display = ('addressUC_address', 'addressUC_des' ,'addressUC_created_date')

admin.site.register(AddressUC,AddressUCAdmin)
# Register your models here.