from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/novo/', views.cliente_form, name='cliente_create'),
    path('clientes/<int:id>/', views.cliente_form, name='cliente_update'),
    # Similar paths for `produtos` and `vendas`
    path('funcionarios/', views.cliente_list, name='funcionario_list'),
    path('funcionarios/novo/', views.cliente_form, name='funcionario_create'),
    path('funcionarios/<int:id>/', views.cliente_form, name='funcionario_update'),
]