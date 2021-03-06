from __future__ import unicode_literals

from django.shortcuts import render
from forms import EmailForm
from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from home_page import models as home_models

def news_page(request):

    context_dict = {}
    banner = Banner.objects.get(id=1)
    blog_posts = [article for article in News.objects.all() if article.external_link == "" and article.publish == True]
    for post in News.objects.all():
        print post.external_link
    in_press = [article for article in News.objects.all() if article.external_link != "" and article.publish == True]
    featured = [article for article in News.objects.all() if article.is_featured == True]

    print featured
    context_dict['banner'] = banner
    context_dict['form'] = EmailForm()
    context_dict['blog_posts'] = blog_posts
    context_dict['in_press'] = in_press
    context_dict['featured'] = featured
    context_dict['default'] = home_models.Default.objects.all()[2]

    return render(request,'media.html', context_dict)

def selected_post(request, slug):
    context_dict = {}
    article = News.objects.get(slug=slug)
    context_dict['article'] = article
    context_dict['form'] = EmailForm()
    context_dict['default'] = home_models.Default.objects.all()[1]


    return render(request, 'article.html', context_dict)
