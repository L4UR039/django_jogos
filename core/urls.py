from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'), 

    path('desenvolvedores/', views.listar_desenvolvedores, name='listar_desenvolvedores'),
    path('desenvolvedores/criar/', views.criar_desenvolvedor, name='criar_desenvolvedor'),
    path('desenvolvedores/editar/<int:id>/', views.editar_desenvolvedor, name='editar_desenvolvedor'),
    path('desenvolvedores/deletar/<int:id>/', views.deletar_desenvolvedor, name='deletar_desenvolvedor'),

    path('jogos/', views.listar_jogos, name='listar_jogos'),
    path('jogos/criar/', views.criar_jogo, name='criar_jogo'),
    path('jogos/editar/<int:id>/', views.editar_jogo, name='editar_jogo'),
    path('jogos/deletar/<int:id>/', views.deletar_jogo, name='deletar_jogo'),
]
