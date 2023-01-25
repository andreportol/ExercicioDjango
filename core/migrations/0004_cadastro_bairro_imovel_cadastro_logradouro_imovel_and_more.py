# Generated by Django 4.1.5 on 2023-01-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cadastro_reg_urbana'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='bairro_imovel',
            field=models.CharField(max_length=100, null=True, verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='logradouro_imovel',
            field=models.CharField(max_length=120, null=True, verbose_name='Logradouro'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='lote_imovel',
            field=models.CharField(max_length=3, null=True, verbose_name='Lote'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='numero_imovel',
            field=models.CharField(max_length=7, null=True, verbose_name='Número do local'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='obs_imovel',
            field=models.TextField(null=True, verbose_name='Observacao'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='parcelamento_imovel',
            field=models.CharField(max_length=5, null=True, verbose_name='Parcelamento'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='quadra_imovel',
            field=models.CharField(max_length=5, null=True, verbose_name='Quadra'),
        ),
    ]
