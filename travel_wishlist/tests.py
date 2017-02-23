from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Place

class TestViewHomePageIsEmptyList(TestCase):


    def test_load_home_page_shows_empty_list(self):

        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertFalse(response.context['places']) # Empty lists are False

class TestWishList(TestCase):

    fixtures = ['test_places']

    def test_view_wishlist(self):

        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # What was sent to the template?
        data_rendered = list(response.context['places'])

        # What is in the database? And get all that equals False
        data_expected = list(Place.objects.filter(visited = False))

        # Did we get what we want?
        self.assertCountEqual(data_rendered, data_expected)
