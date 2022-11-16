from django.urls import path
from .views import ComunaView

urlpatterns=[
    path('comuna/', ComunaView.as_view(), name='comunas'),
    path('comuna/<int:id_comuna>', ComunaView.as_view(), name='comunas by id')
]