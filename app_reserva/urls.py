from django.urls import path
from .views import ReservaHorasView

urlpatterns=[
    path('reserva_horas/', ReservaHorasView.as_view(), name='reserva_horas'),
    path('reserva_horas/<int:id_reserva_horas>', ReservaHorasView.as_view(), name='reserva_horas by id')
]