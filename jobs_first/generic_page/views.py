# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from home_page import models as home_models

def general_page(request):

    context_dict = {}
    banner = Banner.objects.get(id=1)
    posts = [article for article in Page.objects.all() if article.publish == True]

    print featured
    context_dict['banner'] = banner
    context_dict['posts'] = posts
    context_dict['default'] = home_models.Default.objects.all()[2]

    return render(request,'media.html', context_dict)

def selected_post(request, slug):
    context_dict = {}
    article = Page.objects.get(slug=slug)
    context_dict['article'] = article
    context_dict['generic'] = True
    context_dict['default'] = home_models.Default.objects.all()[1]


    return render(request, 'article.html', context_dict)