# Generated by Django 4.2.6 on 2023-10-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_saler_name_wholesaler_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='convertTo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=models.SET(None), to='main.unit'),
        ),
    ]