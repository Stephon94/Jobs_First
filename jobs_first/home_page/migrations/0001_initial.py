# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'')),
            ],
            options={
                'verbose_name_plural': 'Home Page Banner',
            },
        ),
        migrations.CreateModel(
            name='Impact_Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Home Page Impact Section',
            },
        ),
        migrations.CreateModel(
            name='Problem_Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Home Page Problem Section',
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Home Page Solution Section: Solutions',
            },
        ),
        migrations.CreateModel(
            name='Solution_Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Home Page Solution Section',
            },
        ),
    ]
