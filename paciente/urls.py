from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.pacientes_crud, name='pacientes_crud'),
    path('paciente/<int:id>', views.pacientes_by_id, name='pacientes_by_id')
]
