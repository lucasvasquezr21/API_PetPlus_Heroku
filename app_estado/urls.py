from django.urls import path
from .views import EstadoView

urlpatterns=[
    path('estado/', EstadoView.as_view(), name='estado'),
    path('estado/<int:id_estado>', EstadoView.as_view(), name='estado by id')
]