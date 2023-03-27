# from turtle import pd
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse #API
from django.template import RequestContext
from datetime import datetime
from django.core.serializers import serialize
from geoCrimeapp.admin import Accuracy
from geoCrimeapp.models import Crime_data, Crime_prediction
from django.template.context import Context
import pandas as pd

# Create your views here.
def Crime_dataset(request):
    crime_data=serialize('json',Crime_data.objects.order_by("Area_unitID")[:10])
    return HttpResponse(crime_data,content_type='json')

def Crime_dataset_pred(request):
    crime_data_pred=serialize('json',Crime_prediction.objects.all())
    return HttpResponse(Crime_prediction,content_type='json')


def home(request):
    return render(
        request,
        'index.html',
        {
            'title':'Home Page'
        }

    )    
# pred
def pred_score():
    score=Crime_prediction.objects.all()[0]
    ret_score=str(round(Accuracy,score,2))
    return ret_score

def home(request):
    return render(
        request,
        'index.html',
        
        {
            'title':'Home Page',
            'pred_score': pred_score()
        }
    )
