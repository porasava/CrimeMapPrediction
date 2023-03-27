from django.shortcuts import render
import requests
def button(request):
    return render(request('home.html'))

def output(request):
    data=requests.get("http://localhost:8501")
    return render(request,'home.html',{'data':data})