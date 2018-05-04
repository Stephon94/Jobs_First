from django import template

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
