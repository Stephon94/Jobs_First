# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.shortcuts import render
import random
from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from geopy.geocoders import Nominatim

geolocator = Nominatim()


def our_work_page(request):

    context_dict = {}
    banner = Banner.objects.get(id=1)
    partnership_types = Partnership_Type.objects.all()
    partners = Partner.objects.all()


    partnersANDtype = [[partnership, partner] for partnership in partnership_types for partner in partners if partner.partnership_type == partnership]
    print partnersANDtype



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
