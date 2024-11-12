from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Venta
from .forms import VentaForm
from inventario.models import Producto

# Función para verificar si el usuario es jefe
def es_jefe(user):
    return user.is_superuser

@login_required
def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            producto = venta.producto
            venta.precio_total = producto.precio * venta.cantidad
            venta.save()
            # Redirige a listar ventas si es jefe; de lo contrario, permanece en la página de registro de ventas
            return redirect('listar_ventas' if request.user.is_superuser else 'registrar_ventas')
    else:
        form = VentaForm()
    
    # Asegúrate de incluir la lista de productos
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'ventas/registrar_ventas.html', {'form': form, 'productos': productos})

# Vista para listar ventas (solo accesible para jefes)
@login_required
@user_passes_test(es_jefe)
def listar_ventas(request):
    ventas = Venta.objects.all()  # Obtiene todas las ventas registradas
    return render(request, 'ventas/listar_ventas.html', {'ventas': ventas})

from django.contrib.auth.decorators import login_required

@login_required
def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/listar_ventas.html', {'ventas': ventas})

