from django.urls import path
from .views import TipoEmpView

urlpatterns=[
    path('tipo_emp/', TipoEmpView.as_view(), name='tipo emp'),
    path('tipo_emp/<int:id_tipo_emp>', TipoEmpView.as_view(), name='tipo emp by id')
]