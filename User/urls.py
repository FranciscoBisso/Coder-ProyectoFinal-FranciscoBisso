from django.urls import path
from django.contrib.auth.views import LogoutView
from User.views import *

urlpatterns = [
    path('login/', login_request, name='Login'),
    path('register/', register_request, name='Register'),
    path('update-profile/', update_profile, name='UpdateUser'),
    path('avatar/', form_avatar, name='Avatar'),
    path('logout/', LogoutView.as_view(template_name='User/logout.html'), name='Logout'),
]

## USUARIOS DE PRUEBA
# NOMBRE: usuario
# EMAIL: usuario@usuario.com
# PASSWORD: Usu@-123


# NOMBRE: usuario2
# EMAIL: usuario2@usuario.com
# PASSWORD: Usu@-456

# NOMBRE: usuario3
# EMAIL: usuario3@usuario.com
# PASSWORD: Usu@-789


