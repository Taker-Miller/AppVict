from django.db import models
from inventario.models import Producto  # Asegúrate de que esta importación sea correcta

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Disminuir el stock del producto al registrar la venta
        if self.pk is None:  # Solo disminuir el stock si es una nueva venta
            self.producto.stock -= self.cantidad
            self.producto.save()  # Guarda los cambios en el stock del producto
        super().save(*args, **kwargs)
