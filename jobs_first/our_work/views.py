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

    print partnersANDtype

    context_dict['banner'] = banner
    context_dict['partnership_types'] = partnersANDtype


    return render(request,'our_work.html', context_dict)
