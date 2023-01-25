# Generated by Django 4.1.5 on 2023-01-25 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_cadastro_tipo_logradouro'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='cpf_ocupante',
            field=models.CharField(max_length=11, null=True, verbose_name='Nome Ocupante'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='nome_ocupante',
            field=models.CharField(max_length=100, null=True, verbose_name='Nome Ocupante'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='rg_ocupante',
            field=models.CharField(max_length=20, null=True, verbose_name='Nome Ocupante'),
        ),
    ]
