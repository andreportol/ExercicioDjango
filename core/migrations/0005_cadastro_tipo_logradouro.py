# Generated by Django 4.1.5 on 2023-01-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cadastro_bairro_imovel_cadastro_logradouro_imovel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='tipo_logradouro',
            field=models.CharField(max_length=50, null=True, verbose_name='Tipo Logradouro'),
        ),
    ]