from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
class LoginView(View):
	#Method get to get template
	def get(self, request):
		return render(request, 'home.html')