from django.contrib import admin
from .models import Profile, Post

# Register your models here.
admin_profile = admin.site.register(Profile)
posts = admin.site.register(Post)
