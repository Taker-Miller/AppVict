from django.shortcuts import render
from .models import Producto

def inventario_view(request):
    productos = Producto.objects.all()  # Obtiene todos los productos del inventario
    return render(request, 'inventario/inventario.html', {'productos': productos})
