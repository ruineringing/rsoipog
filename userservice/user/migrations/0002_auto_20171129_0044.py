# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='flatnum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='housenum',
            field=models.CharField(default='НЕТ', max_length=4),
        ),
    ]