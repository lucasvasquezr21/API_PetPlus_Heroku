from django.urls import path
from .views import UsuarioView

urlpatterns=[
    path('usuario/', UsuarioView.as_view(), name='usuarios'),
    path('usuario/<int:id_usuario>', UsuarioView.as_view(), name='usuario by id')
]