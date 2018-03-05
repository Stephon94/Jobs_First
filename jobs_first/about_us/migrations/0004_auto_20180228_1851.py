# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0003_auto_20180221_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(default='about_banner/no-banner-img.jpg', upload_to='about_banner'),
        ),
        migrations.AlterField(
            model_name='director',
            name='image',
            field=models.ImageField(default='directors/No_person-1.jpg', upload_to='directors'),
        ),
        migrations.AlterField(
            model_name='staff_member',
            name='image',
            field=models.ImageField(default='staff/No_person-1.jpg', upload_to='staff'),
        ),
    ]
