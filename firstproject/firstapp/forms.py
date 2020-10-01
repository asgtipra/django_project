from django import forms
from django.core import validators	#-> to import in-built validators

class Register(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=40)
    text = forms.CharField(help_text='100 characters max.', widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput, validators=[validators.MinLengthValidator(8, 
    message = "The password should be minimum 8 characters long")])
