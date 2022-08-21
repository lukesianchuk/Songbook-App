from django.shortcuts import render

# Create your views here.
from songs.models import Song

def song_index(request):
    songs = Song.objects.all()
    context = {
        'songs': songs
    }
    return render(request, 'song_index.html', context)

def song_detail(request, pk):
    song = Song.objects.get(pk=pk)
    context = {
        'song': song
    }
    return render(request, 'song_detail.html', context)