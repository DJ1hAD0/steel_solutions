from django.urls import path
from . import views

urlpatterns = [
    path('', views.pogonage_sortament, name='pogonage')
]