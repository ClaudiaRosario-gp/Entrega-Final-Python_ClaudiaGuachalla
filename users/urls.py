from django.urls import path
from . import views
from .views import edit_profile

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    path('edit/', views.edit_profile, name='edit_profile'),
        
    
]
