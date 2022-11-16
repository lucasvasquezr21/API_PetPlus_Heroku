"""API_PetPlus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('index.urls')),
    path('admin/', admin.site.urls),
    path('app_animal/',include('app_animal.urls')),
    path('app_comuna/',include('app_comuna.urls')),
    path('app_dueno/',include('app_dueno.urls')),
    path('app_emp/',include('app_emp.urls')),
    path('app_estado_hora/',include('app_estado_hora.urls')),
    path('app_procedimiento/',include('app_procedimiento.urls')),
    path('app_region/',include('app_region.urls')),
    path('app_reserva/',include('app_reserva.urls')),
    path('app_consulta_procedimiento/',include('app_consulta_procedimiento.urls')),
    path('app_veterinaria/',include('app_veterinaria.urls')),
    path('app_consulta_reserva/',include('app_consulta_reserva.urls')),
    path('app_color/',include('app_color.urls')),
    path('app_especie/',include('app_especie.urls')),
    path('app_raza/',include('app_raza.urls')),
    path('app_sexo/',include('app_sexo.urls')),
    path('app_tipo_empleado/',include('app_tipo_empleado.urls')),
    path('app_estado/',include('app_estado.urls')),
]
