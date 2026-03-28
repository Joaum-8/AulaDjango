from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_listas, name='home'),
    path('concluir/<int:id>/', views.concluir_tarefa, name='concluir'),
    path('deletar/<int:id>/', views.deletar_tarefa, name='deletar'),
    path('lixeira/', views.lixeira, name='lixeira'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar'),
]