from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.

'''
Category
title slug idpk
Tag
title slug idpk
Post
title slug author idpk content created_at photo views category tags
'''

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, verbose_name='Url Tags', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url Post', unique=True)
    author = models.CharField(max_length=100)
    content = CKEditor5Field(config_name='extends', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано') #Дата создается в момент создания
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    views = models.IntegerField(default=0, verbose_name="Кол-во просмотров")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts') # Если первичная модель до поста, то можно писать ввиде ссылки,
    # иначе обрамитьв ковычки
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'