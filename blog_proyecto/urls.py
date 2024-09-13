from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para 'index'
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),  # Para usuarios
    path('blogs/', include('Miaplicacion.urls')),  # Incluye las URLs de la app de blogs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

