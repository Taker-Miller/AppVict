from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirigir a la vista de inicio
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')  # Mensaje de éxito
    return redirect('login')  # Redirigir a la vista de login

def home_view(request):
    """ Vista para redirigir a la página de inicio o a otra sección según tus requerimientos. """
    if request.user.is_authenticated:
        return render(request, 'home.html')  # Renderiza una plantilla para usuarios autenticados
    else:
        return redirect('login')  # Redirigir a la página de login si no está autenticado
