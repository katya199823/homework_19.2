from datetime import datetime

from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование категории')
    description = models.TextField(**NULLABLE,verbose_name='описание')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='фото')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='URL')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=250, verbose_name='название продукта')
    description = models.TextField(verbose_name='описание')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_of_product = models.PositiveIntegerField(verbose_name='цена за товар')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='URL')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


    def __str__(self):
        return (f'{self.product_name} {self.photo}'
                f'{self.description} {self.price_of_product} Руб.'
                f'{self.created_at} {self.updated_at}')


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='название статьи')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='URL')
    description = models.TextField(verbose_name='описание')
    photo = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='фото')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    sign_of_publication = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')

    def str(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, **NULLABLE, verbose_name='продукт')
    version = models.PositiveIntegerField(verbose_name='версия')
    title = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='признак активной версии')

    def str(self):
        return f'{self.product}.'

    class Meta:
        verbose_name = 'версия продукта'
        verbose_name_plural = 'версии продуктов'