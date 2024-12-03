from django.contrib import admin
from django.urls import path, include
from pagina import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('home/admin/', views.home_admin, name='home_admin'),
    path('home/alumno/', views.home_alumno, name='home_alumno'),
    path('home/profesor/', views.home_profesor, name='home_profesor'),
    path('home/subdirector/', views.home_subdirector, name='home_subdirector'),
    path('administrar_alumnos/', views.administrar_alumnos, name='administrar_alumnos'),
    path('administrar_profesores/', views.administrar_profesores, name='administrar_profesores'),
    path('delete/<str:role>/<int:id>/', views.delete_user, name='delete_user'),
    path('__reload__/', include('django_browser_reload.urls')),
    path('administrar_subdirectores/', views.administrar_roles, {'role': 'subdirector'}, name='administrar_subdirectors'),
]

