# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.validators import validate_email
from forms import EmailForm
from django.core.mail import send_mail

def send_email(request):

	if request.POST:
		form = EmailForm(request.POST)
		if form.is_valid():
				
			name = form.cleaned_data['name']
			org = form.cleaned_data['org']
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']


	return HttpResponseRedirect('/')