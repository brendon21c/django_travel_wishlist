from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf.urls import url
from .models import Place
from .forms import NewPlaceForm


# Create your views here.


def place_is_visited(request):

    if request.method == 'POST':

        pk = request.POST.get('pk')
        place = get_object_or_404(Place, pk = pk)
        place.visited = True
        print(place)
        place.save()


    return redirect('place_list')


def place_list(request):

    if request.method == 'POST':

        form = NewPlaceForm(request.POST)
        place = form.save()

        if form.is_valid():

            place.save()
            return redirect('place_list')


    places = Place.objects.filter(visited = False)
    form = NewPlaceForm()

    return render(request, 'travel_wishlist/wishlist.html', {'places' : places, 'form' : form})

def places_visited(request):


    visited = Place.objects.filter(visited = True)

    return render(request, 'travel_wishlist/visited.html', {'visited' : visited})

def location_details(request, pk):

    location = get_object_or_404(Place, pk = pk)
    location_name = location.name
    print(location.place_notes)
    print(location.visited)


    return render(request, 'travel_wishlist/location_details.html', {'location_name' : location_name})
