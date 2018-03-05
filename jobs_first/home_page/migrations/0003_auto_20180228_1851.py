# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_auto_20180221_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(default='home_banner/no-banner-img.jpg', upload_to='home_banner'),
        ),
        migrations.AlterField(
            model_name='impact_section',
            name='image',
            field=models.ImageField(default='impact_banner/no-banner-img.jpg', upload_to='impact_banner'),
        ),
    ]
