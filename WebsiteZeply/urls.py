from django.urls import path
from .views import *

app_name = 'WebsiteZeply'

urlpatterns = [
    # path ('url address', view)
    path('',index,name='index'),
]