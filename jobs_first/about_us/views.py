# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def about_us_page(request):

    context_dict = {}
    banner = Banner.objects.get(id=1)
    history_block = History_Section.objects.get(id=1)
    directors = Director.objects.all()
    staff_members = Staff_Member.objects.all()
    supporter_block = Supporter_Section.objects.get(id=1)
    supporters = Supporter.objects.all()

    context_dict['banner'] = banner
    context_dict['history_block_title'] = history_block.title
    context_dict['history_block_text'] = history_block.text
    context_dict['staff_members'] = staff_members
    context_dict['directors'] = directors
    context_dict['supporter_block_title'] = supporter_block.title
    context_dict['supporter_block_text'] = supporter_block.text
    context_dict['supporters'] = supporters

    return render(request,'about_us.html', context_dict)
