from django import template
from home_page import models as home_models


register = template.Library()

@register.simple_tag
def email(request):
	if request == "POST":
		print request.POST.get('message')
# class Email():
# 	def __init__(self, subject=None, message=None, sender=None, recipient=None):
# 		self.subject=subject
# 		self.message=message
# 		self.sender=sender
# 		self.recipient=recipient

# 	def subject(self):
# 		return

@register.filter
def main_logo(value):
	if value == 'url':
		value = 'https://jobsfirst-assets.s3.amazonaws.com/media/'
	return '{}{}'.format(value, home_models.Navbar_Brand_Logo.objects.get(id=1).image)

@register.filter
def media_url(value):
	if value == 'url':
		return 'https://jobsfirst-assets.s3.amazonaws.com/media/'
	else:
		return 'https://jobsfirst-assets.s3.amazonaws.com/media/{}'.format(value)
