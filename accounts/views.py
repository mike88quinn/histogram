from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Data

# Create your views here.

''' Create the page call for registering a user.'''
def register(request):

    # if the request is a POST then get the user's information
    if request.method == "POST":
        username = request.POST['username']
        age = int(request.POST['age'])
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # test if the passwords are different
        if password1 == password2:
            # if the user name exists send a message to the user that the username is taken
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username " + username + " is already taken")
                return redirect('register')
            # the username does not exist. Sign the user up for the website and redirect user to the histogram
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                auth.login(request, user)
                data = Data.objects.create(username=username, email=email, age=age, id=user.id)

                return redirect('../histogram/histogram', {'data': data})
        # passwords do not match. send a message to the user.
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')

    # not a post. display the register website.
    else:
        return render(request, 'register.html')

''' Create the page call for registering a user.'''
def login(request):

    # if the request is a POST then get the user's information
    if request.method == "POST":
        name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=name, password=password)

        # confirm the user is not null and if so log user in then redirect user to histogram
        if user is not None:
            auth.login(request, user)
            return redirect('../histogram/histogram')
        # user has incorrect credentials. pass message to user
        else:
            messages.info(request, 'Incorrect username or password')
            return render(request, 'login.html')
    # not a post. display the login website.
    else:
        return render(request, 'login.html')

''' Log user out '''
def logout(request):
    auth.logout(request)
    return redirect('/')
