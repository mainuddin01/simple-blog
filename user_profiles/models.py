from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse

# Create your models here.
class UserProfileManager(UserManager):
    pass

class UserProfile(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    objects = UserProfileManager()

    def get_absolute_url(self):
        return reverse('user_profiles:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.username

class UserSocialLink(models.Model):
    SOCIAL_CHOICES = (
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('google-plus', 'Google +'),
        ('linkedin', 'Linkedin'),
        ('website', 'Website')
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    social_site = models.CharField(max_length=10, choices=SOCIAL_CHOICES)
    social_link = models.URLField()

    def __str__(self):
        return f"{self.user.username} - {self.social_site}"