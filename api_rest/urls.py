from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    # trazendo a def todos os usuarios
    path('', views.get_users, name='get_all_users'),

    # crinado rota para consultar por paramentro PK = ("Nick")
    # importando da view, senao criar
    path('user/<str:nick>', views.get_by_nick),
    # CRUD completo para usuários
    path('data/', views.user_manager),

]
