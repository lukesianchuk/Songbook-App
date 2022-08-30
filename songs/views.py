from django.shortcuts import render, redirect

# Create your views here.
from songs.models import Song
from songs.forms import SongForm

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

def song_form(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            return redirect("/songs")
    else:
        form = SongForm()
    return render(request, "song_form.html", {"form": form})

def delete(request, pk):
    song = Song.objects.get(pk=pk)
    song.delete()
    return redirect("/songs")



    
    
    