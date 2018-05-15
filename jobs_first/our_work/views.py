# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.shortcuts import render
import random
from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from geopy.geocoders import Nominatim
from forms import EmailForm

geolocator = Nominatim()


def our_work_page(request):

    context_dict = {}
    banner = Banner.objects.get(id=1)
    partnership_types = Partnership_Type.objects.all()
    partners = Partner.objects.all()
    place_based = Section.objects.get(title='Place-Based Partnerships')
    sector_based = Section.objects.get(title='Sector-Based Partnerships')
    in_school_based = Section.objects.get(title='In-School Partnerships')
    emp_engagement = Section.objects.get(title='Employer Engagement')
    policy = Section.objects.get(title='Policy')
    sub_sections = Sub_Section.objects.all()

    place_based.text = str(place_based.text.encode('utf-8'))
    place_based.save()

    sector_based.text = str(sector_based.text.encode('utf-8'))
    sector_based.save()

    in_school_based.text = str(in_school_based.text.encode('utf-8'))
    in_school_based.save()

    emp_engagement.text = str(emp_engagement.text.encode('utf-8'))
    emp_engagement.save()

    policy.text = str(policy.text.encode('utf-8'))
    policy.save()

    partnersANDtype = [[partnership, partner] for partnership in partnership_types for partner in partners if partner.partnership_type == partnership]
    print partnersANDtype



    #context_dict['sections'] = sections
    context_dict['']
    context_dict['form'] = EmailForm()
    context_dict['sub_sections'] = sub_sections
    context_dict['banner'] = banner
    context_dict['partnership_types'] = partnership_types
    context_dict['partner_w_types'] = partnersANDtype

    return render(request,'our_work.html', context_dict)

def map_locations(request):
        if request.method == 'GET':
               post_id = request.GET['post_id']
               likedpost = Post.obejcts.get(pk=post_id) #getting the liked posts
               m = Like(post=likedpost) # Creating Like Object
               m.save()  # saving it to store in database
               return HttpResponse("Success!") # Sending an success response
        else:
               return HttpResponse("Request method is not a GET")
