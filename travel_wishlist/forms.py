from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):

    """docstring for NewPlaceForm."""

    class Meta:

        model = Place
        fields = ('name',)


class UpdatePlaceForm(forms.ModelForm):
    """ This is the form which is accesed from location_details.html """


    class Meta:
        """Following the same model as NewPlaceForm"""

        model = Place
        
        fields = ('visited', 'place_notes')
