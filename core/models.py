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
    insc_imob = models.CharField('Inscricao',max_length=11)
    utm_x = models.DecimalField('UTM_X', max_digits=6, decimal_places=3)
    utm_y = models.DecimalField('UTM_Y', max_digits=6, decimal_places=3) 
    reg_urbana = models.CharField('Região Urbana', max_length=50)  
    bairro_imovel = models.CharField('Bairro', max_length=100)
    parcelamento_imovel = models.CharField('Parcelamento', max_length=5)
    quadra_imovel = models.CharField('Quadra', max_length=5)
    lote_imovel = models.CharField('Lote', max_length=3)
    logradouro_imovel = models.CharField('Logradouro',max_length=120)
    numero_imovel = models.CharField('Número do local',max_length=7)
    obs_imovel = models.TextField('Observacao')
    
    def __str__(self):
        return f'{self.insc_imob}'

def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.insc_imob)

signals.pre_save.connect(produto_pre_save, sender=Cadastro)
