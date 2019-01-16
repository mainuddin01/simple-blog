from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class UserProfileManager(UserManager):
    pass

class UserProfile(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)

    objects = UserProfileManager()

    def __str__(self):
        return self.username