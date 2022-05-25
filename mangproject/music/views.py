from django.shortcuts import render
from .models import Playlist

# Create your views here.

def home(request):  

  return render(request, 'home.html')