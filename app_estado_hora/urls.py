from django.urls import path
from .views import EstadoHoraView


urlpatterns=[
    path('estado_hora/', EstadoHoraView.as_view(), name='estado'),
    path('estado_hora/<int:id_estado_hora>', EstadoHoraView.as_view(), name='estado by id')
]