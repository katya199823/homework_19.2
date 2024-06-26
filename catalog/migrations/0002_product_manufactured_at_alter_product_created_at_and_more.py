# Generated by Django 5.0.3 on 2024-04-21 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 21, 23, 14, 26, 609173), verbose_name='дата производства продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 21, 23, 14, 26, 609173), verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 21, 23, 14, 26, 609173), verbose_name='дата последнего изменения'),
        ),
    ]
