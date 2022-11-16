from django.urls import path
from .views import ConsultaProcedimientoView

urlpatterns=[
    path('consulta_procedimiento/', ConsultaProcedimientoView.as_view(), name='consulta_procedimiento'),
    path('consulta_procedimiento/<int:id_consulta_procedimiento>', ConsultaProcedimientoView.as_view(), name='consulta_procedimiento by id')
]