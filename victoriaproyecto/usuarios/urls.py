from django.urls import path
from .views import add_user, login_view, employee_panel, boss_panel

urlpatterns = [
    path('add/', add_user, name='add_user'),  # Ruta para agregar usuarios
    path('login/', login_view, name='login'),  # Ruta para iniciar sesión
    path('employee_panel/', employee_panel, name='employee_panel'),  # Panel para empleados
    path('boss_panel/', boss_panel, name='boss_panel'),  # Panel para jefes
    # Agrega otras rutas según sea necesario
]
