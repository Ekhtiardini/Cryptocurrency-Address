from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    #Login
    path('login/',views.login_view,name='login'),
    #Logout
    path('logout/',views.logout_view,name='logout'),
    #SignUp
    path('signup/',views.signup_view,name='signup'),
]