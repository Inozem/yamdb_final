from django.contrib import admin

from .models import Categories, Comment, Genre, Title, User

admin.site.register(User)
admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Categories)
admin.site.register(Comment)
