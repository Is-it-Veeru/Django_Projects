from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login_page/',views.login_page,name='login_page'),
    path('login_action/',views.login_action,name='login_action'),
    path('signup_page/',views.signup_page,name='signup_page'),
    path('signup_action/',views.signup_action,name='signup_action'),
    path('logout/',views.logout,name="logout")
]
