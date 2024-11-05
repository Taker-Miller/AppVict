from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm  # Asegúrate de tener un formulario para Producto
from usuarios.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def inventario_view(request):
    productos = Producto.objects.all()  # Obtiene todos los productos del inventario

    # Obtén el tipo de usuario
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        user_type = user_profile.user_type  # Esto debería ser 'jefe' o 'empleado'
    except UserProfile.DoesNotExist:
        user_type = None  # Manejar el caso si el perfil no existe

    return render(request, 'inventario/inventario.html', {
        'productos': productos,
        'user_type': user_type  # Pasar el tipo de usuario a la plantilla
    })

@login_required
def editar_producto(request, id):
    # Verifica que el usuario sea jefe antes de permitir la edición
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.user_type != 'jefe':
            messages.error(request, 'No tienes permisos para editar productos.')
            return redirect('inventario')
    except UserProfile.DoesNotExist:
        messages.error(request, 'Perfil de usuario no encontrado.')
        return redirect('inventario')

    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto editado correctamente.')
            return redirect('inventario')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventario/editar_producto.html', {'form': form, 'producto': producto})

@login_required
def eliminar_producto(request, id):
    # Verifica que el usuario sea jefe antes de permitir la eliminación
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.user_type != 'jefe':
            messages.error(request, 'No tienes permisos para eliminar productos.')
            return redirect('inventario')
    except UserProfile.DoesNotExist:
        messages.error(request, 'Perfil de usuario no encontrado.')
        return redirect('inventario')

    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('inventario')
    return render(request, 'inventario/eliminar_producto.html', {'producto': producto})
