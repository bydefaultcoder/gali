# Generated by Django 4.2.6 on 2023-10-11 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_clienttransaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clienttransaction',
            old_name='amount',
            new_name='price',
        ),
    ]
