from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.sign_up, name='signUp'),
    path('login/',views.handle_login, name='handleLogin'),
    path('logout/',views.handle_logout, name='handleLogout'),
    path('update-profile/',views.update_profile,name='updateProfile')
]