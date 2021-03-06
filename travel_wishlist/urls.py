from django.conf.urls import url
from . import views


urlpatterns = [

url(r'^$', views.place_list, name = 'place_list'),
url(r'^visited$', views.places_visited, name = 'places_visited'),
url(r'^isvisited$', views.place_is_visited, name = 'place_is_visited'),
url(r'^location/(?P<pk>\d+)/$', views.location_details, name = 'location_details')

]
