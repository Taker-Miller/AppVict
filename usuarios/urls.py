from django.urls import path
from .views import add_user, login_view, employee_panel, boss_panel, reportes_view, usuarios_view, edit_user

urlpatterns = [
    path('add/', add_user, name='add_user'),  # Ruta para agregar usuarios
    path('login/', login_view, name='login'),  # Ruta para iniciar sesión
    path('employee_panel/', employee_panel, name='employee_panel'),  # Panel para empleados
    path('boss_panel/', boss_panel, name='boss_panel'),  # Panel para jefes
    path('reportes/', reportes_view, name='reportes'),  # Ruta para la sección de reportes
    path('usuarios/', usuarios_view, name='usuarios'),  # Ruta para la gestión de usuarios
    path('edit/<int:user_id>/', edit_user, name='edit_user'),  # Ruta para editar un usuario
]
