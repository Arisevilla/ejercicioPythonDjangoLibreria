# Generated by Django 4.2.7 on 2023-12-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_formulario_formulario_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='formulario_id',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
    ]
