# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.validators import validate_email

def validate_data(data=None):
	fields = ('name', 'org', 'email', 'subject', 'message')
	while True:
		for field in fields:
			if len(data.get(field)) > 0:
				if field == 'email':
					try:
						validate_email(data.get(field))
						print 'Good email'
					except:
						print 'Nope, bad email'
						return -1
				locals()[field] = data.get(field)

		return (name,org,email,subject,message)
		

def send_email(request):

	if request.POST:
		data = validate_data(request.POST)
		print data
		name = request.POST.get('name')
		org = request.POST.get('org')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')

	return HttpResponseRedirect('/')