from django.urls import path

from App.views import *

urlpatterns = [
    path('', home, name='Home'),
    path('new-post', new_post, name='NewPost'),
]