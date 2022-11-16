from django.urls import path
from .views import RazaView

urlpatterns=[
    path('raza/', RazaView.as_view(), name='raza'),
    path('raza/<int:id_raza>', RazaView.as_view(), name='raza by id')
]