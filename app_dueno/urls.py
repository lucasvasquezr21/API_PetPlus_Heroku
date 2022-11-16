from django.urls import path
from .views import DuenoView

urlpatterns=[
    path('dueno/', DuenoView.as_view(), name='duenos'),
    path('dueno/<int:id_dueno>', DuenoView.as_view(), name='dueno by id')
]