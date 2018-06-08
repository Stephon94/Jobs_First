# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import EmailForm
from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from jobs_first.settings import MEDIA_URL

def about_us_page(request):

    context_dict = {}
    banners = Banner.objects.all()
    num = 0
    if len(banners) > 1:
        while num < len(banners):
            num += 1
        banner = banners[num-1]
    else:
        banner = banners[0]
    print banner
    history_block = History_Section.objects.get(id=1)
    directors = Director.objects.all()
    staff_members = Staff_Member.objects.all()
    supporter_block = Supporter_Section.objects.get(id=1)
    supporters = Supporter.objects.all()

    context_dict['banner'] = banner
    context_dict['form'] = EmailForm()
    context_dict['history_block_title'] = history_block.title
    context_dict['history_block_text'] = history_block.text
    context_dict['staff_members'] = staff_members
    context_dict['directors'] = directors
    context_dict['supporter_block_title'] = supporter_block.title
    context_dict['supporter_block_text'] = supporter_block.text
    context_dict['supporters'] = supporters
    context_dict['MEDIA_URL'] = MEDIA_URL

    return render(request,'about_us.html', context_dict)
