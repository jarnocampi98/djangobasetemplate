from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.list import ListView

# Create your views here.

def homepage(request):
    return render(request, 'core/homepage.html')