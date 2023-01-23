from django import forms

from .models import Cadastro


class CadastroModelForm(forms.ModelForm):
   class Meta:
      model = Cadastro
      fields = ['insc_imob','utm_x', 'utm_y','reg_urbana', 'bairro_imovel', 'parcelamento_imovel',
      'quadra_imovel', 'lote_imovel', 'logradouro_imovel', 'numero_imovel', 'obs_imovel']   
      

