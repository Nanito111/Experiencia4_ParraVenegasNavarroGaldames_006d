# Generated by Django 4.0.5 on 2022-07-14 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_boleta_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscripcion',
            name='fecha',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
