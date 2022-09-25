from django.urls import path
from django.contrib.auth.views import LogoutView
from User.views import *

urlpatterns = [
    path('login/', login_request, name='Login'),
    path('register/', register_request, name='Register'),
    path('profile/', user_profile, name='ProfileUser'),
    path('update-profile/', update_profile, name='UpdateUser'),
    path('avatar/', form_avatar, name='Avatar'),
    path('logout/', LogoutView.as_view(template_name='User/logout.html'), name='Logout'),
]




