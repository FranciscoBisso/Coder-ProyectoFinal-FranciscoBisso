# PROYECTO FINAL EN EL MARCO DEL CURSO DE PYTHON DE CODERHOUSE

El proyecto se pensó como una página donde se pueden compartir y comentar memes, aunque nada impide que se puedan compartir pequeños post a lo twitter.

## Inspiración: 🚀

-   9gag: https://9gag.com/.
-   twitter: https://twitter.com/.

## Autor ✒️

-   Francisco Bisso.

## Construido con 🛠️

-   Python 3.9.13
-   Django 4.1.1

## Listado de páginas: 📋

### Accesibles por cualquiera:

-   Página principal, donde se muestran todos los posts existentes: http://127.0.0.1:8000/app/
-   Página de registro de nuevos usuarios: http://127.0.0.1:8000/user/register/
-   Página de login: http://127.0.0.1:8000/user/login/
-   Página de logout: http://127.0.0.1:8000/user/logout/

### Accesibles por usuarios registrados:

-   Página de datos de perfil del usuario: http://127.0.0.1:8000/user/profile/
-   Página de posts realizados por el usuario: http://127.0.0.1:8000/app/my-post
-   Página para crear un post: http://127.0.0.1:8000/app/new-post/
-   Página para ver con mayor profundidad un post y poder comentar: http://127.0.0.1:8000/app/comment/...
-   Página para editar un post: http://127.0.0.1:8000/app/edit-post/...
-   Página para eliminar un post: http://127.0.0.1:8000/app/delete-post/...

## Pruebas Ejecutadas ⚙️

Las pruebas realizadas fueron:

-   Se creó un usuario desde el formulario que solicita los datos.
-   Se creó un post desde el formulario que solicita los datos.
-   Se creó un comentario desde el formulario que solicita los datos.

-   Se editó un usuario desde el formulario que solicita los datos.
-   Se editó un post desde el formulario que solicita los datos.
-   Se editó un comentario desde el formulario que solicita los datos.

-   Se verificaron los status de respuesta de las páginas públicas.

Las pruebas se encuentran en App/test.py.
