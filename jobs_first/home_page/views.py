# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import *
from publications.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def index(request):

# Querying everything the Home Page needs
    context_dict = {}
    banners = Banner.objects.all()
    problem_block = Problem_Section.objects.get(id=1)
    solution_block = Solution_Section.objects.get(id=1)
    solutions = Solution.objects.all()
    impact_block = Impact_Section.objects.get()
    articles = Article.objects.all()

    print impact_block

    context_dict['banners'] = banners
    context_dict['solutions'] = solutions
    context_dict['problem_block_title'] = problem_block.title
    context_dict['problem_block_text'] = problem_block.text
    context_dict['solution_block_title'] = solution_block.title
    context_dict['solution_block_text'] = solution_block.text
    context_dict['impact_block_title'] = impact_block.title
    context_dict['impact_block_text'] = impact_block.text
    context_dict['impact_block_image'] = impact_block.image


    return render(request,'index.html', context_dict)
