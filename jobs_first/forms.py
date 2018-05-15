from django import forms

class EmailForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'id': 'inputName',
														'class': 'form-control',
														'label': 'Your Name'}), label='Your Name', max_length=100)
	title = forms.CharField(widget=forms.TextInput(attrs={'id': 'inputTitle',
														'class': 'form-control'}), label='Your Title', max_length=100)
	org = forms.CharField(widget=forms.TextInput(attrs={'id': 'inputOrg',
														'class': 'form-control'}), label='Your Org', max_length=100)
	email = forms.EmailField(widget=forms.TextInput(attrs={'id': 'inputEmail',
														'class': 'form-control'}))
	subject = forms.CharField(widget=forms.TextInput(attrs={'id': 'inputSubject',
														'class': 'form-control'}), label='Subject', max_length=100)
	message = forms.CharField(widget=forms.Textarea(attrs={'id': 'inputMessage',
														'class': 'form-control'}))
	