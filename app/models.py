from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='profile_pictures/icon')
    header = models.ImageField(upload_to='profile_pictures/header')
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    social_media = models.CharField(max_length=100, blank=True)