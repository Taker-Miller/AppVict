from django.urls import path
from .views import registrar_venta, listar_ventas

urlpatterns = [
    path('registrar/', registrar_venta, name='registrar_ventas'),  # URL para registrar ventas (accesible para todos)
    path('listar/', listar_ventas, name='listar_ventas'),          # URL para listar ventas (accesible solo para jefes)
]
