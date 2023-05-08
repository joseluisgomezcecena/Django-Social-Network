from django.db import models
from django.contrib.auth import get_user_model

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
