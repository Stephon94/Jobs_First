from __future__ import unicode_literals

from django.shortcuts import render

from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def publications_page(request):

    context_dict = {}
    banner = Banner.objects.get(id=1)
    articles = [article for article in Article.objects.all() if article.is_featured == False]
    featured = [article for article in Article.objects.all() if article.is_featured == True]

    print articles
    context_dict['banner'] = banner
    context_dict['articles'] = articles
    context_dict['featured'] = featured

    return render(request,'publications.html', context_dict)
