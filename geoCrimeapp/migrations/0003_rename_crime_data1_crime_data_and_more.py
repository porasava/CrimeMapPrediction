# Generated by Django 4.0.6 on 2022-07-22 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoCrimeapp', '0002_rename_crime_data_crime_data1_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Crime_data1',
            new_name='Crime_data',
        ),
        migrations.AlterModelOptions(
            name='crime_data',
            options={'verbose_name_plural': 'Crime_data'},
        ),
    ]
