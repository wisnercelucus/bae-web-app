from django.shortcuts import render, redirect, get_object_or_404

def welcome(request):
	return render(request, 'welcome.html')