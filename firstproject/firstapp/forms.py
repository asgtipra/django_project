import re
from django import forms
from django.core import validators	#-> to import in-built validators
from django.core.exceptions import ValidationError
from django.forms import ModelForm	#-> to connect forms.py with models.py
from firstapp.models import Registration
from django.utils.translation import ugettext as _


class Registerform(forms.ModelForm):
	class Meta:
		model = Registration
		fields = "__all__"
		# fields=['name','email']


#-------------------------------------------------------------------------------------------------------
#-> TASK: custom password validation(1-uc, 1-lc, 2-special char)


# def Length(value):
# 	if len(value) < 6:
# 		raise ValidationError (_("Password should be at least 6 chars long"))
# 		# raise forms.ValidationError("Password should be at least 6 chars long")

# def LowerCase(value):
# 	if not re.findall('[a-z]', value):
# 		raise forms.ValidationError("The password must contain at least 1 lowercase letter, a-z.")


# def UpperCase(value):
# 	if not re.findall('[A-Z]', value):
# 		raise forms.ValidationError("The password must contain at least 1 uppercase letter, A-Z.")


# def SpecialChar(value):
# 	if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', value):
# 		raise forms.ValidationError("The password must contain at least 1 symbol: " +
#                   "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?")


# class Register(forms.Form):
#     name = forms.CharField(label='Name', max_length=100)
#     email = forms.EmailField(label='Email', max_length=40)
#     verify_email = forms.EmailField(label='Verify mail')
#     text = forms.CharField(help_text='100 characters max.', widget=forms.Textarea)
#     # password = forms.CharField(widget=forms.PasswordInput, validators=[validators.MinLengthValidator(8, 
#     # message = "The password should be minimum 8 characters long")])
#     password = forms.CharField(widget=forms.PasswordInput, validators=[Length, LowerCase, UpperCase, SpecialChar])


#     def clean(self):
#     	email = self.cleaned_data['email']
#     	vmail = self.cleaned_data['verify_email']
#     	if email != vmail:
#     		raise forms.ValidationError("Email do not match")
