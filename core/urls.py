from django.urls import path
from .views import home,user_login,user_logout,user_signUp

urlpatterns = [
    path('home',home,name='home'),
    path('login',user_login, name='login'),
    path('logout',user_logout, name='logout'),
    path('signup',user_signUp, name='signup'),
]