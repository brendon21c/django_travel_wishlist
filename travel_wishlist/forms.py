from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):

    """docstring for NewPlaceForm."""

    class Meta:

        model = Place
        fields = ('name', 'visited')
