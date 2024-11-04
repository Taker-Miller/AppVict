from django.urls import path
from .views import registrar_venta, listar_ventas

urlpatterns = [
    path('registrar/', registrar_venta, name='registrar_ventas'),
    path('', listar_ventas, name='listar_ventas'),  # URL para listar ventas
]
