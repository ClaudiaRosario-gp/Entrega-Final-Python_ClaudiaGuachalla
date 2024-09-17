from django import views
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogEditView, BlogDeleteView, AboutView
from . import views
from django.urls import path
from . import views  

urlpatterns = [
     
    path('', BlogListView.as_view(), name='blog_list'),  # Listar blogs 
    path('pages/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),  # Detalles del blog
    path('pages/new/', BlogCreateView.as_view(), name='blog_create'),  # Crear blog
    path('pages/<int:pk>/edit/', BlogEditView.as_view(), name='blog_edit'),  # Editar blog
    path('pages/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),  # Eliminar blog
    path('about/', AboutView.as_view(), name='about'),
    path('pages/<int:pk>/guardar_comentario/', views.guardar_comentario, name='guardar_comentario'),
    path('search/', views.blog_search, name='blog_search'),    
  ]
