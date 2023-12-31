from django.urls import path, re_path
from . import views


urlpatterns = [
    path('pogonage_unit', views.pogonage_sortament, name='pogonage'),
    path('sheet_unit', views.sheet_sortament, name='sheet'),
    path('product/<product_id>/', views.get_product_by_id, name='product'),
    path('list_products', views.list_products, name='list_products'),
    path('create_product', views.create_product, name='create_product'),
    path('delete_product/<product_id>/', views.delete_product, name='delete_product'),
    path('create_spec_entry', views.create_spec_entry, name='create_spec_entry'),
    path('update_spec_entry', views.update_spec_entry, name='update_spec_entry'),
    path('delete_spec_entry', views.delete_spec_entry, name='delete_spec_entry'),
    path('create_unit_entry', views.create_unit_entry, name='create_unit_entry'),
    path('update_unit_entry', views.update_unit_entry, name='update_unit_entry'),
    path('delete_unit_entry', views.delete_unit_entry, name='delete_unit_entry'),
    path('', views.index, name='index')
]

