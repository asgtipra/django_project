from django.shortcuts import render, redirect
from django.http import HttpResponse
from firstapp import forms


def home(request):
	return render(request, 'firstapp/home.html')

#----------------------------------------------------------------------------
#->	this below code will display data on backend. 

def create(request):
	if request.method == 'POST':
		form = forms.Registerform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('success')
			except:
				print('error')
	else:
		form=forms.Registerform()
	return render (request, 'firstapp/register.html', {'form':form})

def success(request):
	return render (request, 'firstapp/success.html')


#----------------------------------------------------------------------------
#->	this below code will display data on terminal. 

# def form_view(request):
# 	if request.method == 'POST':
# 		form=forms.Register(request.POST)
# 		if form.is_valid():
# 			print('Success!!')
# 			print("Name: " + form.cleaned_data['name'])
# 			print("Email: " + form.cleaned_data['email'])
# 			print("Text: " + form.cleaned_data['text'])
# 		else:
# 			print('Please put valid values')

# 	form = forms.Register
# 	return render(request, 'firstapp/register.html', {'form':form})