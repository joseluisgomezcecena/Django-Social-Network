from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from . import urls
from django.contrib import messages
from .models import Profile

# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        # do something
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password2']
        name = request.POST['firstname'] + ' ' + request.POST['lastname']

        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                print('Username taken')
                messages.info(request, 'That username is already taken, please try again.')
            elif User.objects.filter(email=email).exists():
                print('Email taken')
                messages.info(request, 'That email is already taken, please try again.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # log user in and redirect to settings page.

                # create a profile object for the user.
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id, name=name)
                new_profile.save()

                print('User created')
                messages.info(request, 'Your Account was created successfully, you can now login.')
                return redirect('core:signup_form')

        else:
            messages.info(request, 'Passwords don\'t match, please try again.')
            return redirect('core:signup_form')

    else:
        return render(request, 'signup.html')
