# Generated by Django 4.2.6 on 2023-10-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.AddField(
            model_name='client',
            name='age_group',
            field=models.CharField(blank=True, choices=[('0-10', '0-10 years'), ('10-20', '10-20 years'), ('20-40', '20-40 years'), ('40-100', '40-100 years')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
    ]
