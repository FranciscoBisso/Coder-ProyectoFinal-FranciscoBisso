from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from App.models import *
from App.forms import *


## SOBRE MI  ##
# PÁGINA PRINCIPAL DONDE SE MUESTRAN TODOS LOS POSTS EXISTENTES
def about_me(req):
    return render(req, 'base/about.html')



## POSTS  ##
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
            return redirect('MyPost')
        
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
    user = req.user
    if user.id == editable_post.author.id:
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
                
                return redirect('MyPost')
            
            else:
                messages.info(req, '¡Ups! Please try again.')
                
        
        
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
    else:
        messages.info(req, 'Only the author of the post can edit it')
            
        return redirect('Home')



# ELIMINAR POSTS
@login_required
def delete_post(req, id):
    deletable_post = Post.objects.get(id=id)
    user = req.user
    
    if user.id == deletable_post.author.id:
        try:

            deletable_post.delete()
            
            messages.info(req, f'Deleted post: {deletable_post.title}!')
        except:
            messages.info(req, 'Unable to delete a non-existent post!')        
        
        return redirect('MyPost')
    else:
        messages.info(req, 'Only the author of the post can delete it.')
        return redirect('Home')



##  COMENTARIOS  ##
# CREACIÓN DE NUEVOS COMENTARIOS
@login_required
def new_comment(req, id):
    if req.method == 'POST':
        form = CommentForm(req.POST)
        post = Post.objects.get(id=id)
        user = req.user
        
        if form.is_valid():
            data = form.cleaned_data
            
            comment = Comment(
                comment=data.get('comment'), 
                related_post=post,
                author=user
            )
            comment.save()
            
            messages.info(req,
                  'Comment uploaded!')
        else:
            messages.info(req, 'Ups! Please try again.')
            
        return redirect('Comment', id) 
        
    
    post = Post.objects.get(id=id)
    old_comments = Comment.objects.filter(related_post=id)
    context = {
        'form': CommentForm(),
        'form_name': 'COMMENT',
        'button': 'COMMENT',
        'post': post,
        'old_comments': old_comments
    }
    return render(req, 'blog/comment.html', context)



# ELIMINAR POSTS
@login_required
def delete_comment(req, id):
    try:
        
        deletable_comment = Comment.objects.get(id=id)
        post_id = deletable_comment.related_post.id
        print(f'post_id ---> {post_id}')

        deletable_comment.delete() 
        
        messages.info(req, f'Comment Deleted.')
        return redirect('Comment', post_id)
    
    except:
        messages.info(req, 'Unable to delete a non-existent comment!')
        return redirect('Comment', post_id)
    
             
    
    