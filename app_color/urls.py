from django.urls import path
from .views import ColorView

urlpatterns=[
    path('color/', ColorView.as_view(), name='color'),
    path('color/<int:id_color>', ColorView.as_view(), name='color by id')
]