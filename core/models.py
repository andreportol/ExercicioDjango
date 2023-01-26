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
    insc_imob = models.CharField('Inscricao', max_length=11)
    utm_x = models.DecimalField(
        'UTM_X', max_digits=6, decimal_places=3, null=True)
    utm_y = models.DecimalField(
        'UTM_Y', max_digits=6, decimal_places=3, null=True)
    reg_urbana = models.CharField('Região Urbana', max_length=50, null=True)
    tipo_logradouro = models.CharField(
        'Tipo Logradouro', max_length=50, null=True)
    bairro_imovel = models.CharField('Bairro', max_length=100, null=True)
    parcelamento_imovel = models.CharField(
        'Parcelamento', max_length=5, null=True)
    quadra_imovel = models.CharField('Quadra', max_length=5, null=True)
    lote_imovel = models.CharField('Lote', max_length=3, null=True)
    logradouro_imovel = models.CharField(
        'Logradouro', max_length=120, null=True)
    numero_imovel = models.CharField(
        'Número do local', max_length=7, null=True)
    obs_imovel = models.TextField('Observacao', null=True)
    nome_ocupante = models.CharField(
        'Nome Ocupante', max_length=100, null=True)
    rg_ocupante = models.CharField('RG Ocupante', max_length=20, null=True)
    cpf_ocupante = models.CharField('CPF Ocupante', max_length=11, null=True)
    num_notif = models.CharField('Número Notificação', max_length=6, null=True)
    num_auto = models.CharField('Número Auto', max_length=6, null=True)
    data_notif = models.DateField('Data Notificação', null=True, blank=True)
    data_auto = models.DateField('Data Auto', null=True, blank=True)
    num_processo = models.CharField(
        'Número Processo', max_length=30, null=True)
    num_cnpj = models.CharField('CNPJ', max_length=40, null=True)
    obs_documentacao = models.TextField('Observação', null=True)
    # variavel para trabalhar com radiobutton
    radio_reincidente = (('SIM', 'SIM'), ('NAO', 'NÃO'))
    RadioReincidente = models.CharField(
        'Reincidente', choices=radio_reincidente, max_length=10, null=True)

    def __str__(self):
        return f'{self.insc_imob} {self.reg_urbana}{self.bairro_imovel}{self.logradouro_imovel}{self.RadioReincidente}'


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.insc_imob)


signals.pre_save.connect(produto_pre_save, sender=Cadastro)
