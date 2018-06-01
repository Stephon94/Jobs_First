from __future__ import unicode_literals

from django.shortcuts import render

from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import EmailForm
import os
from wsgiref.util import FileWrapper

def publications_page(request):

    context_dict = {}

    if request.method == "POST":
    	context_dict['results'] = [article for article in Article.objects.all() if request.POST.get('keyword') in article.title]
        if len(context_dict['results']) == 0:
            context_dict['results'] = -1

    banner = Banner.objects.get(id=1)
    print vars(banner)
    articles = [article for article in Article.objects.all() if article.is_featured == False]
    featured = [article for article in Article.objects.all() if article.is_featured == True]

    context_dict['banner'] = banner
    context_dict['form'] = EmailForm()
    context_dict['articles'] = articles
    context_dict['featured'] = featured

    return render(request,'publications.html', context_dict)

def publications_article(request, slug):

    context_dict = {}
    article = Article.objects.get(slug=slug)
    context_dict['article'] = article
    context_dict['switch'] = -1

    return render(request,'article.html', context_dict)

def pdf_download(request, filename):
    
    from wsgiref.util import FileWrapper
    f = open(path+filename, "r")
    response = HttpResponse(FileWrapper(f), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename={}.pdf'.format("".join(filename.split('.')[0]))
    f.close()
