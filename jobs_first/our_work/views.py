# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.shortcuts import render
import random
from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

class PartnersJsonEndpoint(ListView):
	queryset = Partner.objects.all()
    get(queryset)

	def get(queryset, request, *args, **kwargs):
		dictionary = [ obj.as_dict() for obj in queryset ]
		return	HttpResponse(json.dumps({"data": dictionary}), content_type='application/json')


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
        print partner[1].coordinate, 1
    locations = [[partner[1].get_position(), partner[1].name] for partner in partnersANDtype if partner[1].get_position() != None ]
    print locations, 2

    for location in locations:
        print location,3

    start_location = random.choice(locations)
    print start_location



    context_dict['banner'] = banner
    context_dict['partnership_types'] = partnersANDtype
    context_dict['locations'] = locations
    context_dict['start_location'] = start_location



    return render(request,'our_work.html', context_dict)
