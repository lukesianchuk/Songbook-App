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
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save()
            return redirect("/songs")
    else:
        form = SongForm()
    return render(request, "song_form.html", {"form": form})

def delete(request, pk):
    song = Song.objects.get(pk=pk)
    context ={}
 
 
    if request.method =="POST":
        # delete object
        song.delete()
        # after deleting redirect to
        # home page
        return redirect("/songs")
 
    return render(request, "song_delete.html", context)


def update(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    song = Song.objects.get(pk=pk)
 
    # pass the object as instance in form
    form = SongForm(request.POST or None, instance = song)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("/songs")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "song_update.html", context)




    
    
    