from django.urls import path

from App.views import *

urlpatterns = [
    path('about/', about_me, name='AboutMe'),
    path('', home, name='Home'),
    path('new-post', new_post, name='NewPost'),
    path('my-post', my_post, name='MyPost'),
    path('edit-post/<int:id>', edit_post, name='EditPost'),
    path('delete-post/<int:id>', delete_post, name='DeletePost'),
    path('comment/<int:id>', new_comment, name='Comment'),
    path('delete-comment/<int:id>', delete_comment, name='DeleteComment'),
]