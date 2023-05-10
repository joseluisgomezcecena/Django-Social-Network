from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    id_user = models.IntegerField()
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_images/', default='default.png')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images/', default='default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user


