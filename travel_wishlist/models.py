from django.db import models
from datetime import datetime

class Place(models.Model):
    """docstring for ."""

    name = models.CharField(max_length = 200)
    visited = models.BooleanField(default = False)
    date_visited = models.DateTimeField(auto_now_add = True, blank = True)
    place_notes = models.CharField(max_length = 500)

    def __str__(self):

        return '%s visited? %s' % (self.name, self.visited, self.date_visited , self.place_notes)
