from django.shortcuts import render
from django.views.generic.base import View

from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import RegisterForm 

@login_required
def home(request):
	# if request.user.is_authenticated:
	# 	return render(request, 'home.html')
	# else:
	# 	return HttpResponseForbidden('Sizga ruhsat yo')
	return render(request, 'home.html')

def register(request):
	if request.method == 'POST':
		reg_form = RegisterForm(request.POST)
		if reg_form.is_valid():
			reg_form.save()
	else:
		reg_form = RegisterForm()
	context = {
		'form':reg_form
	}
	return render(request, 'registration/register.html', context)
