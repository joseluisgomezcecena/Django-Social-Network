from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from . import urls
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='core:login_form')
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
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                # create a profile object for the user.
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id, name=name)
                new_profile.save()

                print('User created')
                messages.info(request, 'Your Account was created successfully, you can now login.')
                return redirect('core:settings')

        else:
            messages.info(request, 'Passwords don\'t match, please try again.')
            return redirect('core:signup_form')

    else:
        return render(request, 'signup.html')


@login_required(login_url='core:login_form')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        if request.FILES.get('image') is None:
            image = user_profile.image
        else:
            image = request.FILES['image']

        bio = request.POST['bio']
        location = request.POST['location']

        user_profile.image = image
        user_profile.bio = bio
        user_profile.location = location
        user_profile.save()

    return render(request, 'setting.html', {'user_profile': user_profile})


def login(request):
    if request.method == 'POST':
        # do something
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        # if user exists
        if user is not None:
            auth.login(request, user)
            print('User logged in')
            return redirect('core:profile')
        else:
            print('Invalid credentials')
            messages.info(request, 'Invalid credentials, please try again.')
            return redirect('core:login_form')

    else:
        return render(request, 'signin.html')


@login_required(login_url='core:login_form')
def logout(request):
    auth.logout(request)
    print('User logged out')
    messages.info(request, "You've, been logged out.")
    return redirect('core:index')
