from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Playlist


# Create your views here.

def home(request):  
  playlists = Playlist.objects

  return render(request, 'home.html', {'playlists': playlists})

def upload(request):
  if request.method == 'POST':
    playlist = Playlist()
    playlist.genre = request.POST.get('genre').split(",")
    playlist.name = request.POST.get('name')
    playlist.pub_data = timezone.datetime.now()
    playlist.thumbnail = request.FILES['thumbnail']
    print(playlist.thumbnail)
    playlist.save()

    return redirect('/')
  else:
    return render(request, 'upload.html')
  
