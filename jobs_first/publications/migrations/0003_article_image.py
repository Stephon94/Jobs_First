# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='our_work_banner/solutions.jpg', upload_to='Article'),
        ),
    ]