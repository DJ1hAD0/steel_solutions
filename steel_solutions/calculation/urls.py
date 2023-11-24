from django.urls import path, re_path
from . import views


urlpatterns = [
    path('pogonage_unit', views.pogonage_sortament, name='pogonage'),
    path('sheet_unit', views.sheet_sortament, name='sheet'),
    path('spec/<product_id>/', views.spec, name='spec'),
    path('delete_spec_entry', views.delete_spec_entry, name='delete_spec_entry'),
    path('create_spec_entry', views.create_spec_entry, name='create_spec_entry'),
    path('update_spec_entry', views.update_spec_entry, name='update_spec_entry'),
    path('index', views.index, name='index')
]
