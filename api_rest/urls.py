from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

   path('', views.get_users, name='get_all_users'), #trazendo a def todos os usuarios

   #crinado rota para consultar por paramentro PK = ("Nick")
   path('user/<str:nick>',views.get_by_nick), #importando da view, senao criar
   path('data/', views.user_manager)
    
]