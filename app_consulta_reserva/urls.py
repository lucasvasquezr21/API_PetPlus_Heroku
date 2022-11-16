from django.urls import path
from .views import ConsultaReservaView

urlpatterns=[
    path('consulta_reserva/', ConsultaReservaView.as_view(), name='ConsultaReserva'),
    path('consulta_reserva/<int:id_consulta_reserva>', ConsultaReservaView.as_view(), name='ConsultaReserva by id')
]