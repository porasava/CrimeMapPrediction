# Generated by Django 4.0.6 on 2022-07-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoCrimeapp', '0011_crime_prediction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime_prediction',
            name='LATITUDE',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='crime_prediction',
            name='LONGITUDE',
            field=models.FloatField(),
        ),
    ]
