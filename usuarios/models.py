# usuarios/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('jefe', 'Jefe'),
        ('empleado', 'Empleado'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con el modelo de usuario
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)  # Tipo de usuario (jefe o empleado)
    
    # Puedes agregar más campos según sea necesario
    # Ejemplo:
    # phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"  # Representación del objeto
