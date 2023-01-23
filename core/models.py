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
       
    def __str__(self):
        return f'{self.insc_imob}'

def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.insc_imob)

signals.pre_save.connect(produto_pre_save, sender=Cadastro)
