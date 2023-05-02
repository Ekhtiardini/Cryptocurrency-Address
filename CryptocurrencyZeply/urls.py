from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # add app url to my site
    path('',include('WebsiteZeply.urls')),
    path('accounts/',include('accounts.urls')),
    path('WalletZeply/',include('WalletZeply.urls')),
    path('AddressUserCoin/',include('AddressUserCoin.urls')),
]

urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
