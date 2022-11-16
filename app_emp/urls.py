from django.urls import path
from .views import EmpView

urlpatterns=[
    path('emp/', EmpView.as_view(), name='emps'),
    path('emp/<int:id_emp>', EmpView.as_view(), name='emp by id')
]