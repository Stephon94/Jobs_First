# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def our_work_page(request):

    context_dict = {}
    banner = Banner.objects.get(id=1)
    partnership_types = Partnership_Type.objects.all()
    partners = Partner.objects.all()

    partnersANDtype = [[partnership, partner] for partnership in partnership_types for partner in partners if partner.partnership_type == partnership]

    # for partnership in partnership_types:
    #     for partner in partners:
    #         if partner.partnership_type == partnership:
    #             partnersANDtype.append([partnership, partner])

    for partner in partnersANDtype:
        print partner,1
    locations = [partner[1].get_position() for partner in partnersANDtype]
    print locations,2

    for location in locations:
        print location,3

    start_location = locations[2]
    print start_location, 4

    location_names = [[partner[1].get_position(), partner[1].name] for partner in partnersANDtype]
    print location_names

    context_dict['banner'] = banner
    context_dict['partnership_types'] = partnersANDtype
    context_dict['locations'] = locations
    context_dict['start_location'] = start_location
    context_dict['location_names'] = location_names



    return render(request,'our_work.html', context_dict)
