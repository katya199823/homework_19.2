from datetime import datetime

from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование категории')
    description = models.TextField(**NULLABLE,verbose_name='описание')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='фото')

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

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


    def __str__(self):
        return (f'{self.product_name} {self.photo}'
                f'{self.description} {self.price_of_product} Руб.'
                f'{self.created_at} {self.updated_at}')

