from django.urls import path
from . import views  # Importa las vistas de la aplicación inventario

urlpatterns = [
    path('', views.inventario_view, name='inventario'),  # Ruta para ver el inventario principal
]
