from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings'),
    path('new_post/', views.new_post, name='new_post'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('follow/', views.follow, name='follow'),
    path('like_post/', views.like_post, name='like_post'),
    path('signup/', views.signup, name='signup_form'),
    path('login/', views.login, name='login_form'),
    path('logout/', views.logout, name='logout'),
]
