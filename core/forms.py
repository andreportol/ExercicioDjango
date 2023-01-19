from django import forms


class CadastroForm(forms.Form):
   insc_imob =  forms.CharField(label = 'Inscrição Imobiliária', max_length=11, min_length=11)
   coordenadaUtm = forms.CharField(label= 'Coordenada')
   