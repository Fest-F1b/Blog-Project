
from os import truncate
from django.urls import reverse
from typing import ClassVar
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model, ModelState
from django.db.models.deletion import CASCADE
from django.utils.translation import to_language
from tinymce import models as tinymce_models


# blog Models


class Category_post(models.Model):
     name = models.CharField(max_length=100)
    
     def __str__(self) -> str:
          return self.name

     def get_absolute_url(self):
          return reverse("home")


HEALTH = 'Health'
LIFESTYLE = 'Life style'
WEB_DEVELOPMENT = 'Web development'
PROGRAMMING = 'Programming'
POST_IN_CATEGORY_CHOICES = [
     (HEALTH, 'Health'),
     (LIFESTYLE, 'Lifestyle'),
     (WEB_DEVELOPMENT, 'Web development'),
     (PROGRAMMING, 'Programming')
]

STATUS = (
    (0, "Draft"),
     (1, "Publish")
)


class Post (models.Model):
     title = models.CharField(max_length=100, unique=True)
     slug = models.SlugField(max_length=200, unique=True)
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     updated_on = models.DateTimeField(auto_now=True)
     content = tinymce_models.HTMLField()
     created_on = models.DateTimeField(auto_now_add=True)
     status = models.IntegerField(choices=STATUS, default=0)
     postImg = models.FileField(
          upload_to="images/", null=True, blank=True, verbose_name="Post Image")
     post_in_category = models.CharField(max_length=100, choices=POST_IN_CATEGORY_CHOICES,
                                         default=PROGRAMMING, null=False)


     class Meta:
          ordering = ['-created_on']

     def __str__(self) -> str:
          return str(self.title)


class Comment(models.Model):
     post = models.ForeignKey(
          Post, on_delete=models.CASCADE, related_name='comments')
     name = models.CharField(max_length=80)
     email = models.EmailField()
     body = models.TextField()
     created_on = models.DateTimeField(auto_now_add=True)
     active = models.BooleanField(default=False)

     class Meta:
          ordering = ['created_on']

     def __str__(self) -> str:
          return 'Comment {} by {}'.format(self.body, self.name)


class Subscribe(models.Model):
     email = models.EmailField()

     class Meta:
          ordering = ['email']

     def __str__(self) -> str:
          return str(self.email)



