from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view



# Create your views here.
def home1( request ):
    return render(request, 'LittleLemonAPI/home116.html')



def manage1( request ):
    return render(request, 'LittleLemonAPI/manager121.html')
