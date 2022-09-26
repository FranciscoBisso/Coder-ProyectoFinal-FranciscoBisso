from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# MODELO PARA POSTS
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=80, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='img-post', null=False, blank=False)
    
    def __str__(self):
        return f"AUTHOR: {self.author} - TITLE: {self.title} - SUBTITLE: {self.subtitle} - DATE: {self.date} - IMG: {self.img} - DESCRIPTION: {self.description[0:15]}..."



# MODELO PARA COMENTARIOS
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"AUTHOR: {self.author} - RELATED POST: {self.related_post.id} - DATE: {self.date} - COMMENT: {self.comment[0:15]}..."
    

