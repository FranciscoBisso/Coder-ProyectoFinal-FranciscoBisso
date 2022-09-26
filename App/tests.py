from django.test import TestCase
from django.urls import reverse
import datetime
from django.contrib.auth.models import User
from App.models import Post, Comment
from User.models import *


class AppTestCase(TestCase):
    def setUp(self):
        Post.objects.create(
            author=User.objects.get(id=1),
            title='Title',
            subtitle='Lorem ipsum',
            description='Lorem ipsum dolor sit amet consectetur adipiscing.', 
            date=datetime.datetime(2022, 9, 2, 11, 21, 37, 582857),
            img='/media/img-post/baco-ariadna.jpg'
        )
        Comment.objects.create(
            author=User.objects.get(id=1),
            related_post=Post.objects.get(id=1),
            comment='Lorem ipsum dolor',
            date=datetime.datetime(2022, 9, 2, 11, 21, 37, 582857),
        )

    def test_creation_of_post_and_comment(self):
        p1 = Post.objects.get(title='Title')
        p2 = Comment.objects.get(comment='Lorem ipsum dolor')
        self.assertEqual(p1.title, 'Title')
        self.assertEqual(p2.comment, 'Lorem ipsum dolor')