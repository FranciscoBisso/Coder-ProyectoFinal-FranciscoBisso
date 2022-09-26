from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from App.models import *
from App.forms import *

## Create your views here.

# PÁGINA PRINCIPAL DONDE SE MUESTRAN TODOS LOS POSTS EXISTENTES
def home(req):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(req, 'home.html', context)



# CREACIÓN DE NUEVOS POSTS
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


# SE MUESTRAN TODOS LOS POSTS CREADOS POR EL USUARIO
@login_required
def my_post(req):
    user = req.user
    posts = Post.objects.filter(author = user.id)
    context = {
        'posts': posts,
    }
    return render(req, 'blog/my_post.html', context)



# EDICIÓN DE MIS POSTS EXISTENTES.
@login_required
def edit_post(req, id):
    editable_post = Post.objects.get(id=id)
 
    if req.method == 'POST':
        form = PostForm(req.POST, req.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
            editable_post.title = data.get('title')        
            editable_post.subtitle = data.get('subtitle')        
            editable_post.description = data.get('description')        
            editable_post.img = data.get('img')        
            editable_post.save()
            
            messages.info(req, 'Post edited successfully!')
            
            return redirect('Home')
        
        else:
            messages.info(req, '¡Ups! Please try again.')
            return render(req, 'blog/edit-post.html', context)
    
    
    context = {
        'form': PostForm(initial={
            'title': editable_post.title,     
            'subtitle': editable_post.subtitle,    
            'description': editable_post.description,   
            'img': editable_post.img
        }),
        'editable_post': editable_post,
        'form_name': 'EDIT POST',
        'button': 'EDIT',
    }
    
    return render(req, 'blog/edit-post.html', context)



# ELIMINAR POSTS
def delete_post(req, id):
    try:
        deletable_post = Post.objects.get(id=id)

        deletable_post.delete()
        
        messages.info(req, f'Deleted post: {deletable_post.title}!')
    except:
        messages.info(req, 'Unable to delete a non-existent post!')        
    
    return redirect('MyPost')