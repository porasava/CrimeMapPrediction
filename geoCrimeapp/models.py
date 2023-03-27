from turtle import pd
from django.db import models


# # Create your models here.
class Crime_data(models.Model):
    Month=models.IntegerField()
    Year=models.IntegerField()
    SHAPE_X=models.FloatField()
    SHAPE_Y=models.FloatField()
    LATITUDE=models.FloatField()
    LONGITUDE=models.FloatField()
    Area_unitID=models.FloatField()
    Day_Of_Week_ID=models.IntegerField()
    HRGroup=models.IntegerField()
    TA_ID=models.FloatField()
    Locn_Type_DivisionID=models.IntegerField()
    Types_of_Crime_ID=models.FloatField()
    Number_of_records=models.FloatField()
    new_column=models.FloatField()
    
    def __str__(self):
        return self.Area_unitID
    class Meta:
            verbose_name_plural='Crime_data'


class Crime_prediction(models.Model):
    Month=models.IntegerField()
    Year=models.DecimalField( max_digits=5, decimal_places=0)
    LATITUDE=models.FloatField()
    LONGITUDE=models.FloatField()
    Area_unitID=models.DecimalField( max_digits=5, decimal_places=0)
    Day_Of_Week_ID=models.IntegerField()
    HRGroup=models.IntegerField()
    TA_ID=models.DecimalField( max_digits=5, decimal_places=0)
    Locn_Type_DivisionID=models.IntegerField()
    Types_of_Crime_ID=models.DecimalField( max_digits=5, decimal_places=0)
    Crime_Case=models.CharField(max_length=30)
    Accuracy=models.DecimalField( max_digits=5, decimal_places=2)

class Meta:
    verbose_name_plural='Crime_prediction'
    