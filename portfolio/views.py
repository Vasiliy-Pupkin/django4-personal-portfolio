from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def home_page(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def view_portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})
def about(request):
    return render(request, 'portfolio/about.html')