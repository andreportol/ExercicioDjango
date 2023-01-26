from django.urls import path

from .views import (atualizar, cadastrar, complementodados, deletar, index,
                    pesquisar, visualizarDados)

urlpatterns = [
    path('', index, name='index'),
    path('cadastrar', cadastrar, name='cadastrar'),
    path('deletar', deletar, name='deletar'),
    path('atualizar', atualizar, name='atualizar'),
    path('pesquisar', pesquisar, name='pesquisar'),
    path('visualizarDados', visualizarDados, name='visualizarDados'),
    path('complementodados', complementodados, name='complementodados'),
    
]
