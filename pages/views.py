from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio

def index(request):
    projects = Portfolio.objects.all()
    # for project in projects:
    #     print(project)
    context = {
        'projects': projects
    }
    return render(request, 'pages/index.html', context)