from django.contrib import admin

# Register your models here.
from App.models import *

admin.site.register(Post)
admin.site.register(Comment)