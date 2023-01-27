from django.urls import path

from .views import (cadastrar, complementodados, deletar, editarCadastro,
                    index, pesquisar, visualizarDados)

urlpatterns = [
    path('', index, name='index'),
    path('cadastrar', cadastrar, name='cadastrar'),
    path('deletar', deletar, name='deletar'),
    path('pesquisar', pesquisar, name='pesquisar'),
    path('visualizarDados', visualizarDados, name='visualizarDados'),
    path('complementodados/<int:pk>', complementodados, name='complementodados'),
    path('editarCadastro/<int:pk>', editarCadastro, name='editarCadastro')
]
