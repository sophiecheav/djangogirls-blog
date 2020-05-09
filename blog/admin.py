from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post)
# notre objet Post est désormais géré par l'admin de Django
