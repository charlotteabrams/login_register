from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import datetime

def index(request):
	return render(request, 'loginRegisterApp/index.html')

def register(request):
	if User.userManager.register(request.POST, request):
		return redirect ('/success')
	else:
		error=False
		return redirect('/')

def login(request):
	if User.userManager.login(request.POST, request):
		return redirect('/success')
	else:
		return redirect('/')

	

def success(request):
	return render(request, 'loginRegisterApp/results.html')