"""Predict URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import re_path as url
import django.contrib.auth.views

import geoCrimeapp.views
from geoCrimeapp.views import Crime_dataset, Crime_dataset_pred
# from geoCrimeapp.views import showdata
# from geoCrimeapp import views

urlpatterns =[
    url(r'^$',geoCrimeapp.views.home, name='home'),#automatic go to home page with no need url
    url(r'^crime_dataset/',Crime_dataset, name='crimedataset'),
    url(r'^Crime_dataset_pred/',Crime_dataset_pred, name='Crimedatasetpred'),
    # url(r'^data/',views.showdata, name='crimedataset'),
    path('admin/', admin.site.urls),
]
