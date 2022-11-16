from django.urls import path
from .views import RegionView

urlpatterns=[
    path('region/', RegionView.as_view(), name='region'),
    path('region/<int:id_region>', RegionView.as_view(), name='region by id')
]