import django_filters

from .models import Cadastro


class CadastroFilter(django_filters.FilterSet):
    insc_imob = django_filters.CharFilter(lookup_expr='icontains')
    nome_ocupante = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Cadastro
        fields = ('insc_imob', 'nome_ocupante') 