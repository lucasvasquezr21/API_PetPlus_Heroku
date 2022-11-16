from django.urls import path
from .views import SexoView

urlpatterns=[
    path('sexo/', SexoView.as_view(), name='sexo'),
    path('sexo/<int:id_sexo>', SexoView.as_view(), name='sexo by id')
]