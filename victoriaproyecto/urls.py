from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from login.views import home_view  # Importa la vista de inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', include('login.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('inventario/', include('inventario.urls')),  # Incluye las URLs de la aplicación inventario
    path('ventas/', include('ventas.urls')),  # Incluye las URLs de la aplicación ventas
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Manejo de archivos estáticos
