from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import login
from django.http import HttpResponse

from .forms import UserCreationEmailForm, EmailAuthenticationForm

# Create your views here.
def signup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()

		#loguear usuario
		#redireccionar al home

	return render(request, 'signup.html', {'form': form})

def signin(request):
	form = EmailAuthenticationForm(request.POST or None)

	if form.is_valid():
		login(request, form.get_user())
		#redireccionar al home

	return render(request, 'signup.html', {'form': form})

class LoginView(View):

	def get(self, request, *args, **kwargs):
		return HttpResponse('Prueba')