from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Playlist


# Create your views here.

def home(request):  
  playlists = Playlist.objects.all()

  return render(request, 'home.html', {'playlists': playlists})

def upload(request):
  if request.method == 'POST':
    playlist = Playlist()
    playlist.genre = request.POST.get('genre')
    playlist.name = request.POST.get('name')
    playlist.pub_date = timezone.datetime.now()
    try:
      playlist.thumbnail = request.FILES['thumbnail']
    except:
      pass
    playlist.save()

    return redirect('/')
  else:
    return render(request, 'upload.html')
  
def playlist_detail(request, playlist_id):
  playlist_detail = Playlist.objects.get(id = playlist_id)
  return render(request, 'playlist_detail.html', {'playlist': playlist_detail})

def playlist_delete(request, playlist_id):
  Playlist.objects.get(id = playlist_id).delete()
  return redirect('/')
  
def playlist_edit(request, playlist_id):
  playlist = Playlist.objects.get(id = playlist_id)
  if request.method == 'POST':
    playlist.genre = request.POST.get('genre')
    playlist.name = request.POST.get('name')
    playlist.pub_date = timezone.datetime.now()
    try:
      playlist.thumbnail = request.FILES['thumbnail']
      
    except:
      pass
    playlist.save()
    return redirect(f'/music/{playlist_id}')
  else:
    return render(request, 'playlist_edit.html', {'playlist' : playlist})
