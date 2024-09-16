from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogEditView, BlogDeleteView, AboutView

urlpatterns = [
    
    path('', BlogListView.as_view(), name='blog_list'),  # Listar blogs en /blogs/
    path('pages/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),  # Detalles del blog
    path('pages/new/', BlogCreateView.as_view(), name='blog_create'),  # Crear blog
    path('pages/<int:pk>/edit/', BlogEditView.as_view(), name='blog_edit'),  # Editar blog
    path('pages/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),  # Eliminar blog
    path('about/', AboutView.as_view(), name='about')
    
  ]
