from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogEditView, BlogDeleteView, AboutView

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),  # Listar blogs (ruta principal)
    path('pages/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),  # Detalles del blog
    path('pages/new/', views.BlogCreateView.as_view(), name='blog_create'),  # Crear blog
    path('pages/<int:pk>/edit/', views.BlogEditView.as_view(), name='blog_edit'),  # Editar blog
    path('pages/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),  # Eliminar blog
    path('about/', AboutView.as_view(), name='about'),  # Vista "Acerca de mí"
]
