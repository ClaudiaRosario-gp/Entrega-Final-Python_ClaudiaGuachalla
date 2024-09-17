from django.urls import path
from . import views
from .views import edit_profile, LogoutView, register, login_request
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    #path('logout/', views.custom_logout, name='logout'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
    path('logout', views.LogoutView.as_view(), name='logout'),
              
]
