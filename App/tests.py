from django.test import TestCase
from django.urls import reverse
import datetime
from django.contrib.auth.models import User
from App.models import Post, Comment


## RESULTADO DE LOS TEST: Ran 3 tests in 0.023s OK

# TEST DE CREACIÓN DE USUARIOS, POST Y COMENTARIOS DE POST.
class AppTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            username='user',
            email='user@user.com',
            password='Usuer@.,123',
        )
        Post.objects.create(
            author=User.objects.get(username='user'),
            title='Title',
            subtitle='Lorem ipsum',
            description='Lorem ipsum dolor sit amet consectetur adipiscing.', 
            date=datetime.datetime(2022, 9, 2, 11, 21, 37, 582857),
            img='/media/img-post/baco-ariadna.jpg'
        )
        Comment.objects.create(
            author=User.objects.get(username='user'),
            related_post=Post.objects.get(title='Title',),
            comment='Lorem ipsum dolor',
            date=datetime.datetime(2022, 9, 2, 11, 21, 37, 582857),
        )

    def test_creation(self):
        p1 = Post.objects.get(title='Title')
        p2 = Comment.objects.get(comment='Lorem ipsum dolor')
        self.assertEqual(p1.title, 'Title')
        self.assertEqual(p2.comment, 'Lorem ipsum dolor')


# TEST DE EDICIÓN DE POST Y COMENTARIOS DE POST.
    def test_edition(self):
        p1 = Post.objects.get(title='Title')
        p1.title = 'title'
        p1.save()
        self.assertEqual(p1.title, 'title')
        
        p2 = Comment.objects.get(comment='Lorem ipsum dolor')
        p2.comment = 'lorem Ipsum dolor'
        self.assertEqual(p2.comment, 'lorem Ipsum dolor')
        
        p3=User.objects.get(username='user')
        p3.username = 'USUARIO'
        self.assertEqual(p3.username, 'USUARIO')


# TEST DE URLS ACCESIBLES POR TODOS
class ViewTests(TestCase):
    def test_public_views(self):
        home = self.client.get(reverse('Home'))
        self.assertEqual(home.status_code, 200)
        self.assertContains(home, '')

        login = self.client.get(reverse('Login'))
        self.assertEqual(login.status_code, 200)
        self.assertContains(login, '')

        register = self.client.get(reverse('Register'))
        self.assertEqual(register.status_code, 200)
        self.assertContains(register, '')
        
        about_me = self.client.get(reverse('AboutMe'))
        self.assertEqual(about_me.status_code, 200)
        self.assertContains(about_me, '')


