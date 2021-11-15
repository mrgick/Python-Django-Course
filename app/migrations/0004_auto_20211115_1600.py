# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-15 14:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211115_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-posted'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Пост'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 11, 15, 16, 0, 57, 61187), verbose_name='Опубликован'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 11, 15, 16, 0, 57, 61187), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Blog', verbose_name='Пост'),
        ),
    ]
