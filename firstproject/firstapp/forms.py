from django import forms
from django.core import validators	#-> to import in-built validators
from django.core.exceptions import ValidationError
from django.forms import ModelForm	#-> to connect forms.py with models.py
from firstapp.models import Registration


class Registerform(forms.ModelForm):
	class Meta:
		model = Registration
		fields = "__all__"
		# fields=['name','email']


#-------------------------------------------------------------------------------------------------------

# def check(value):
# 	if len(value) < 6:
# 		raise forms.ValidationError("Password should be at least 6 chars long")


# class Register(forms.Form):
#     name = forms.CharField(label='Name', max_length=100)
#     email = forms.EmailField(label='Email', max_length=40)
#     verify_email = forms.EmailField(label='Verify mail')
#     text = forms.CharField(help_text='100 characters max.', widget=forms.Textarea)
#     # password = forms.CharField(widget=forms.PasswordInput, validators=[validators.MinLengthValidator(8, 
#     # message = "The password should be minimum 8 characters long")])
#     password = forms.CharField(widget=forms.PasswordInput, validators=[check])


#     def clean(self):
#     	email = self.cleaned_data['email']
#     	vmail = self.cleaned_data['verify_email']
#     	if email != vmail:
#     		raise forms.ValidationError("Email do not match")
