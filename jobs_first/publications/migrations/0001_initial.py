# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=5000)),
                ('is_featured', models.BooleanField(default=False)),
                ('publish_date', models.DateField()),
                ('author_first_name', models.CharField(max_length=200)),
                ('author_last_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
