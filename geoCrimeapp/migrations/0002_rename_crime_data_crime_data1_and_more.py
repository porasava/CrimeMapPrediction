# Generated by Django 4.0.6 on 2022-07-22 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoCrimeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Crime_data',
            new_name='Crime_data1',
        ),
        migrations.AlterModelOptions(
            name='crime_data1',
            options={'verbose_name_plural': 'Crime_data1'},
        ),
    ]
