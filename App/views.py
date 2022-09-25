from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from App.models import *
from App.forms import *

# Create your views here.
def home(req):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(req, 'home.html', context)



@login_required
def new_post(req):
    if req.method == 'POST':
        user = req.user
        author = User.objects.get(id=user.id)
        
        form = PostForm(req.POST, req.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
            
            post = Post(
                author=author,
                title=data.get('title'),
                subtitle=data.get('subtitle'),
                description=data.get('description'),
                img=data.get('img'),
            )
            post.save(data)
            
            messages.info(req, 'All right, all right, all right!')
            return redirect('Home')
        
        else:
            messages.info(req, '¡Ups! Please try again.')
            

    context = {
        'form': PostForm(),
        'form_name': 'NEW POST',
        'button': 'SEND'
    }
    return render(req, 'blog/blog_form.html', context)