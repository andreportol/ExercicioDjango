from django.contrib import admin

# Register your models here.
from .models import Cadastro


@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('insc_imob','nome_ocupante','insc_imob','reg_urbana',
        'bairro_imovel','logradouro_imovel','RadioReincidente')
