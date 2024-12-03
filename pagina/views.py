from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.contrib.auth.hashers import check_password, make_password

# Hardcoded admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Generic CRUD View
def administrar_roles(request, role):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password', '')  # Default to empty if not provided
        action = request.POST.get('action')

        if action == 'add' and username and password:
            user, created = User.objects.get_or_create(username=username, role=role)
            user.password = make_password(password)  # Hash the password
            user.save()
        elif action == 'delete' and username:
            user = get_object_or_404(User, username=username, role=role)
            user.delete()

    # Get all users with the specified role
    users = User.objects.filter(role=role)
    template = f"administrar_{role}s.html"
    return render(request, template, {f"{role}s": users})

def administrar_roles(request, role):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password', '')  # Default to empty if not provided
        action = request.POST.get('action')

        if action == 'add' and username and password:
            user, created = User.objects.get_or_create(username=username, role=role)
            user.password = make_password(password)  # Hash the password
            user.save()
        elif action == 'delete':
            user_id = request.POST.get('id')
            user = get_object_or_404(User, id=user_id, role=role)
            user.delete()

    # Get all users with the specified role
    users = User.objects.filter(role=role)
    template = f"administrar_{role}s.html"
    return render(request, template, {f"{role}s": users})

# Role-Specific Views
def administrar_alumnos(request):
    return administrar_roles(request, role='alumno')

def administrar_profesores(request):
    return administrar_roles(request, role='profesore')

def administrar_subdirector(request):
    return administrar_roles(request, role='subdirector')

def administrar_subdirectors(request):
    return render(request, 'administrar_subdirectors.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check hardcoded admin credentials
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return redirect('home_admin')

        # Check database for other users
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                # Redirect based on user role
                role_redirects = {
                    'alumno': 'home_alumno',
                    'profesore': 'home_profesor',
                    'subdirector': 'home_subdirector',
                }
                return redirect(role_redirects.get(user.role, 'login'))
            else:
                return render(request, 'login.html', {'error': 'Credenciales inválidas'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})

    return render(request, 'login.html')


# Delete User View
def delete_user(request, id, role):
    user = get_object_or_404(User, id=id)
    if user.role != role:
        return redirect('home_admin')  # Redirect to admin if role mismatch
    user.delete()
    # Redirect based on role
    role_redirects = {
        'alumno': 'administrar_alumnos',
        'profesore': 'administrar_profesores',
        'subdirector': 'administrar_subdirector',
    }
    return redirect(role_redirects.get(role, 'home_admin'))


# Home Views
def inicio(request):
    return render(request, 'inicio.html')

def home_admin(request):
    return render(request, 'home_admin.html')

def home_alumno(request):
    return render(request, 'home_alumno.html')

def home_profesor(request):
    return render(request, 'home_profesor.html')

def home_subdirector(request):
    return render(request, 'home_subdirector.html')

def inicio(request):
    return render(request, 'inicio.html')