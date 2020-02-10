from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from accounts.models import Data

# Create your views here.

''' Redirect the user to the histogram page.'''
def histogram(request):
    data = Data.objects.all()
    all_ages = []
    for d in data:
        all_ages.append(d.age)
    if request.user.is_authenticated:
        return render(request, 'histogram.html', {'data': data, 'all_ages': all_ages})
    else:
        return redirect('/', {'data': data})

