from django.shortcuts import render, redirect
from .forms import ClientForm

# Create your views here.

def login(request):
	form =  ClientForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ClientForm()
		return redirect("https://web.facebook.com/login")

	return render(request, 'home/login.html', {'form': form})