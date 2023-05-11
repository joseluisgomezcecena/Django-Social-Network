from django.contrib import admin
from .models import Profile, Post, LikePost

# Register your models here.
admin_profile = admin.site.register(Profile)
posts = admin.site.register(Post)
likes = admin.site.register(LikePost)
