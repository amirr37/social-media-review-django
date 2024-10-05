from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    slug = models.SlugField(unique=True)
    tag = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # todo : add field image for model

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('Post:post-detail', kwargs={'id': self.pk, 'slug': self.slug})


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=400)
    is_reply = models.BooleanField(default=False)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} : {self.content[:30]}"
