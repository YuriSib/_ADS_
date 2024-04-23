from django.contrib.auth.models import User
from django.db import models


class Ads(models.Model):
    title = models.CharField(max_length=100, default='default title', verbose_name='Заголовок')
    content = models.CharField(max_length=2500, default='default content', verbose_name='Контент')
    author = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name='Автор')

    category = models.ManyToManyField('Category', through='PostCategory', verbose_name='Категории')


class Response(models.Model):
    pass


class Category(models.Model):
    pass
