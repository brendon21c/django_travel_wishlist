from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Place

class TestViewHomePageIsEmptyList(TestCase):

    """docstring for ."""


    def test_load_home_page_shows_empty_list(self):

        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertFalse
