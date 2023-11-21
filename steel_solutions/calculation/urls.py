from django.urls import path, re_path
from . import views


urlpatterns = [
    path('pogonage_unit', views.pogonage_sortament, name='pogonage'),
    path('sheet_unit', views.sheet_sortament, name='sheet'),
    path('spec/<product_id>/', views.spec, name='spec'),
    path('index', views.index, name='index')
]
