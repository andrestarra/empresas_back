from django.contrib import admin
from django.urls import path, include
from .views import (
    EmpresaDetalleView,
    EmpresasListaView,
    EmpresaCrearView,
    EmpresaEditarView,
    EmpresaEliminarView
)

urlpatterns = [
    path("empresa/crear", EmpresaCrearView.as_view(), name=None),
    # path("empresa/<int:pk>", EmpresaDetalleView.as_view(), name=None),
    path("empresa/editar/<int:pk>", EmpresaEditarView.as_view(), name=None),
    path("empresa/eliminar/<int:pk>", EmpresaEliminarView.as_view(), name=None),
    path("empresas", EmpresasListaView.as_view(), name=None),
]
