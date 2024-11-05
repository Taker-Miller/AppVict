from django.shortcuts import render, redirect
from .models import Venta
from .forms import VentaForm
from inventario.models import Producto  # Asegúrate de que esto sea correcto

def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            producto = venta.producto
            venta.precio_total = producto.precio * venta.cantidad
            venta.save()
            return redirect('inventario')  # Redirige a la página de inventario después de guardar
    else:
        form = VentaForm()
    
    # Asegúrate de incluir la lista de productos si es necesario
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'ventas/registrar_ventas.html', {'form': form, 'productos': productos})

def listar_ventas(request):
    ventas = Venta.objects.all()  # Obtiene todas las ventas registradas
    return render(request, 'ventas/listar_ventas.html', {'ventas': ventas})
