from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings'),
    path('signup/', views.signup, name='signup_form'),
    path('login/', views.login, name='login_form'),
    path('logout/', views.logout, name='logout'),
]
