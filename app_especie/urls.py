from django.urls import path
from .views import EspecieView

urlpatterns=[
    path('especie/', EspecieView.as_view(), name='especie'),
    path('especie/<int:id_especie>', EspecieView.as_view(), name='especie by id')
]