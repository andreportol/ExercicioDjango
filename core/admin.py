from django.contrib import admin

# Register your models here.
from .models import Cadastro


@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('Inscricao_Imobiliaria', 'Bairro','Regiao Urbana')

