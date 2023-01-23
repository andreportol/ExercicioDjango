from django.db import models
# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    
    class Meta:
        abstract = True

class Cadastro(Base):
    insc_imob = models.CharField(max_length=11, name='Inscricao_Imobiliaria')
    utm_x = models.DecimalField(max_digits=11, decimal_places=2, name='UTM_X')
    utm_y = models.DecimalField(max_digits=11, decimal_places=2, name='UTM_Y')
    reg_urbana = models.CharField(name='Regiao Urbana',max_length=30)
    bairro_imovel = models.CharField(name='Bairro', max_length=120)
    parcelamento_imovel = models.CharField(name='Parcelamento',max_length=5)
    quadra_imovel = models.CharField(name='Quadra',max_length=5)
    lote_imovel = models.CharField(name='Lote',max_length=5)
    logradouro_imovel = models.CharField('Logradouro_imovel',max_length=120)
    obs_imovel = models.TextField(name= 'Observacao') 
    
    def __str__(self):
        return f'{self.Inscricao_Imobiliaria}'

def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.Inscricao_Imobiliaria)

signals.pre_save.connect(produto_pre_save, sender=Cadastro)
