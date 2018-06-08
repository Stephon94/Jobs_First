# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import random
import models as home
from forms import EmailForm
from our_work.models import *
from media.models import *
from our_work.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from jobs_first.settings import MEDIA_URL

def index(request):

# Querying everything the Home Page needs
    context_dict = {}
    banners = home.Banner.objects.all()
    problem_block = home.Problem_Section.objects.get(id=1)
    solution_block = home.Solution_Section.objects.get(id=1)
    solutions = home.Solution.objects.all()
    impact_block = home.Impact_Section.objects.get()
    featured = [article for article in News.objects.all() if article.is_featured == True and article.publish == True]
    affiliates = Affiliates.objects.all()
    partners = Partner.objects.all()
    logo = home.Navbar_Brand_Logo.objects.get(id=1)
    location_coordinates = []

    for partner in partners:
        if partner.address is not None:
            location_coordinates.append(partner.get_coordinates())

    if location_coordinates:
        start_location = random.choice(list(location_coordinates[0]))
        context_dict['start_location'] = start_location
        if len(location_coordinates) > 1:
            location_coordinates = location_coordinates[len(location_coordinates)/2:]
            context_dict['locations'] = location_coordinates

    if request.POST:
        print request.POST


    context_dict['banners'] = banners
    context_dict['main_logo'] = '{}{}'.format(MEDIA_URL,logo.image)
    context_dict['form'] = EmailForm()
    context_dict['MEDIA_URL'] = MEDIA_URL
    context_dict['affiliates'] = affiliates
    context_dict['featured'] = featured
    context_dict['solutions'] = solutions
    context_dict['problem_block_title'] = problem_block.title
    context_dict['problem_block_text'] = problem_block.text
    context_dict['solution_block_title'] = solution_block.title
    context_dict['solution_block_text'] = solution_block.text
    context_dict['impact_block_title'] = impact_block.title
    context_dict['impact_block_text'] = impact_block.text
    context_dict['impact_block_image'] = impact_block.image
    
    


    return render(request,'index.html', context_dict)
