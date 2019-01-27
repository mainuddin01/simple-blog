from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse

User = get_user_model()

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    category = models.ManyToManyField('Category')
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    publication_date = models.DateTimeField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    visited = models.PositiveIntegerField(default=0)

    def post_visited(self):
        self.visited += 1
        self.save()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:tag_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    message = models.TextField()
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog:comment_create', kwargs={'slug':self.post.slug})

    def __str__(self):
        return self.message