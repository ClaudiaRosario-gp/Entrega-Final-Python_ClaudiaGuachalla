from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from Miaplicacion.views import AboutView  # Importa AboutView si es necesario
from Miaplicacion.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # URLs para usuarios
    path('blogs/', include('Miaplicacion.urls')),  # URLs para blogs
    
]

# Solo incluye esto una vez
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
