from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField("Название",max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,verbose_name= "Title")
    text = models.TextField(verbose_name="Text")
    image = models.ImageField(upload_to="posts/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField("Активный",default=False)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title    


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        related_name="comments",
        null=True,
    )
    name = models.CharField("name", max_length=50)
    comment = models.TextField("Comment")
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['-created']

    def __str__(self):
        return str(self.comment)[:50]
