from django.db import models

# Create your models here.
class Setting(models.Model):
    name = models.CharField(max_length=20)
    slogan = models.CharField(max_length=50, null=True, blank=True)
    logo = models.ImageField(upload_to='site_logo', null=True, blank=True)
    favicon = models.ImageField(upload_to='site_logo', null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    google_plus_link = models.URLField(null=True, blank=True)
    rss_link = models.URLField(null=True, blank=True)
    footer_logo = models.ImageField(upload_to='site_logo', null=True, blank=True)
    footer_text = models.TextField(null=True, blank=True)
    copyright = models.CharField(max_length=100, null=True, blank=True)
    header_ad = models.TextField(null=True, blank=True)
    middle_ad = models.TextField(null=True, blank=True)
    footer_ad = models.TextField(null=True, blank=True)
    sidebar_ad = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        return super(Setting, self).save(*args, **kwargs)

    def __str__(self):
        return self.name