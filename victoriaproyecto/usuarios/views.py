from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm, VerificationCodeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import UserProfile
from django.contrib.auth.decorators import login_required  # Importa el decorador aquí

def add_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        verification_code_form = VerificationCodeForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Validar el código de verificación si el usuario es jefe
            if profile.user_type == 'jefe':
                verification_code = verification_code_form.cleaned_data.get('verification_code')
                if verification_code != '123':
                    messages.error(request, 'El código de verificación es incorrecto.')
                    return render(request, 'usuarios/add_user.html', {
                        'user_form': user_form,
                        'profile_form': profile_form,
                        'verification_code_form': verification_code_form,
                    })
            
            messages.success(request, 'Usuario agregado exitosamente.')
            return redirect('user_list')  # Cambia esto a la vista de lista de usuarios o donde desees redirigir.

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        verification_code_form = VerificationCodeForm()
    
    return render(request, 'usuarios/add_user.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'verification_code_form': verification_code_form,
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            user_profile = UserProfile.objects.get(user=user)  # Obtener el perfil de usuario

            # Redirigir a la vista del panel correspondiente
            if user_profile.user_type == 'jefe':
                messages.success(request, 'Bienvenido, Jefe.')
                return redirect('boss_panel')  # Cambia esto por el nombre de la URL del panel de jefe
            else:
                messages.success(request, 'Bienvenido, Empleado.')
                return redirect('employee_panel')  # Cambia esto por el nombre de la URL del panel de empleado
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    return render(request, 'login/login.html')

@login_required  # Añade el decorador aquí
def employee_panel(request):
    # Verifica si el usuario tiene el rol adecuado
    if request.user.is_authenticated and request.user.userprofile.user_type == 'empleado':
        return render(request, 'usuarios/employee_panel.html')  # Asegúrate de tener esta plantilla
    else:
        return redirect('home')  # Redirigir a otra página si no tiene permiso

@login_required  # Añade el decorador aquí
def boss_panel(request):
    return render(request, 'usuarios/boss_panel.html')  # Asegúrate de tener esta plantilla
