from django.shortcuts import render, redirect
from accounts.models import Data

# Create your views here.

''' direct user to the homepage '''
def index(request):
    data = Data.objects.all()
    return render(request, "index.html", {'data': data})
