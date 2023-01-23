from django import forms

from .models import Cadastro


class CadastroModelForm(forms.ModelForm):
   class Meta:
      model = Cadastro
      fields = ['insc_imob']

