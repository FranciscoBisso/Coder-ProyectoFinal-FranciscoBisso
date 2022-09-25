from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from User.forms import *
from User.models import *

# Create your views here. 

# PROCESAMIENTO DE LOGIN
def login_request(req):
    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)

        if form.is_valid():
            data = form.cleaned_data

            username = data.get('username')
            password = data.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(req, user)
                messages.info(req, f'Hello there {user.username.upper()}!')
                return redirect('Home')


        else:
            messages.info(req, 'Ups! Invalid credentials. Please try again.')

            return redirect('Login')

    context = {
        'form': AuthenticationForm(),
        'form_name': 'LOGIN',
        'button': 'LOGIN'
    }
    return render(req, 'User/user_form.html', context)


# PROCESAMIENTO DE REGISTRO
def register_request(req):
    if req.method == 'POST':

        form = UserRegisterForm(req.POST)

        if form.is_valid():

            form.save()

            messages.info(req, 'Welcome to the community!')
        else:
            messages.info(req, 'Ups! Please try again.')
        
        return redirect('Login')

    context = {
        'form': UserRegisterForm(),
        'form_name': 'REGISTER',
        'button': 'REGISTER'
    }

    return render(req, 'User/user_form.html', context)


@login_required
def update_profile(req):
    user = req.user
    if req.method == 'POST':

        form = UserRegisterForm(req.POST)

        if form.is_valid():
            data = form.cleaned_data
            user.username = data.get('username')
            user.email = data.get('email')

            user.save()
            messages.info(req, f'{user.username.upper()}, your profile data has been updated!')
            
        else:
            messages.info(req, '¡Ups! Please try again.')
            
        return redirect('Home')
    
    
    context = {
        'form': UserRegisterForm(
            initial={
                'username': user.username,
                'email': user.email
            }),
        'form_name': 'UPDATE PROFILE',
        'button': 'UPDATE'
    }

    return render(req, 'User/user_form.html', context)

@login_required
def form_avatar(req):
    user = req.user
  
    if req.method == 'POST':
        form = AvatarForm(req.POST, req.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
            try:
                old_avatar = Avatar.objects.get(user_id=user.id)
                if old_avatar:
                    old_avatar.img = data.get('avatar')
                    old_avatar.save()
                    messages.info(req,
                        'UPDATED AVATAR!')
                    return redirect('Home')
                
            except:
                avatar = Avatar(
                    img=data.get('avatar'), 
                    user_id=user.id
                )
                avatar.save(data)
                
                messages.info(req,
                    'AVATAR UPLOADED!')
                return redirect('Home')
            
        else:
            messages.info(req, 'UPS! PLEASE TRY AGAIN.')
            return redirect('Avatar') 

    
   
    context = {
        'form': AvatarForm(),
        'form_name': 'UPLOAD AVATAR',
        'button': 'UPLOAD',
    }
    return render(req, 'User/avatar_form.html', context)