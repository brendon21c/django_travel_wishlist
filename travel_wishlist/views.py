from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf.urls import url
from .models import Place
from .forms import *


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


    places = Place.objects.all()
    form = NewPlaceForm()

    return render(request, 'travel_wishlist/wishlist.html', {'places' : places, 'form' : form})

def places_visited(request):


    visited = Place.objects.filter(visited = True)

    return render(request, 'travel_wishlist/visited.html', {'visited' : visited})

def location_details(request, pk):

    location = get_object_or_404(Place, pk = pk)
    location_name = location.name
    location_pk = location.pk
    location_visited = location.visited

    if request.method == 'POST':

        form = UpdatePlaceForm(request.POST)
        place = form.save(commit = False)

        if form.is_valid():

            data = form.cleaned_data
            notes = data['place_notes']
            visited = data['visited']

            if visited:

                location.place_notes = notes
                location.visited = visited

                location.save()

                return redirect('place_list')

            else:
                
                location.place_notes = notes

                location.save()

                return redirect('place_list')



    if location_visited == True:

        place = location

        return render(request, 'travel_wishlist/location_details.html', {'location' : location_name, 'visited' : place})

    else:

        form = UpdatePlaceForm()

        return render(request, 'travel_wishlist/location_details.html', {'location' : location_name, 'pk' : location_pk, 'form' : form})
