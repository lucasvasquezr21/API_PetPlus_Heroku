from django.urls import path
from .views import ProcedimientoView

urlpatterns=[
    path('procedimiento/', ProcedimientoView.as_view(), name='procedimiento'),
    path('procedimiento/<int:id_procedimiento>', ProcedimientoView.as_view(), name='procedimiento by id')
]