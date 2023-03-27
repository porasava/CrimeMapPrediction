# Generated by Django 4.0.6 on 2022-07-23 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoCrimeapp', '0008_delete_crime_prediction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crime_prediction1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month', models.IntegerField()),
                ('Year', models.DecimalField(decimal_places=0, max_digits=5)),
                ('LATITUDE', models.DecimalField(decimal_places=10, max_digits=10)),
                ('LONGITUDE', models.DecimalField(decimal_places=10, max_digits=10)),
                ('Area_unitID', models.DecimalField(decimal_places=0, max_digits=5)),
                ('Day_Of_Week_ID', models.IntegerField()),
                ('HRGroup', models.IntegerField()),
                ('TA_ID', models.DecimalField(decimal_places=0, max_digits=5)),
                ('Locn_Type_DivisionID', models.IntegerField()),
                ('Types_of_Crime_ID', models.DecimalField(decimal_places=0, max_digits=5)),
                ('Crime_Case', models.CharField(max_length=30)),
                ('Accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
