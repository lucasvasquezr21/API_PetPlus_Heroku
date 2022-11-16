from django.urls import path
from .views import AnimalView

urlpatterns=[
    path('animal/', AnimalView.as_view(), name='animales'),
    path('animal/<int:id_animal>', AnimalView.as_view(), name='animal by id')
]