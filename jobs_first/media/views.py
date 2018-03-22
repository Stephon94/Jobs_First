from __future__ import unicode_literals

from django.shortcuts import render

from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def news_page(request):

    context_dict = {}
    banner = Banner.objects.get(id=1)
    blog_posts = [article for article in News.objects.all() if (article.is_news == False and article.publish == True) and article.external_link == ""]
    in_press = [article for article in News.objects.all() if article.is_news == True and article.publish == True]
    featured = [article for article in News.objects.all() if article.is_news == False and article.external_link != ""]

    print featured
    context_dict['banner'] = banner
    context_dict['blog_posts'] = blog_posts
    context_dict['in_press'] = in_press
    context_dict['featured'] = featured

    return render(request,'media.html', context_dict)

def selected_post(request, post_slug):
    context_dict = {}
    post = News.object.get(slug=post_slug)

    return render(request, 'post_detail.html')
