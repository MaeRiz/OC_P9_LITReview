from django.forms import ModelForm, TextInput
from django.forms import fields

from .models import Ticket

class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = (
            'headline',
            'body',
            'image',
        )

        widgets = {
            'headline': TextInput(attrs={'placeholder': 'Ex: HungerGames'}),
        }

        labels = {
            'headline': 'Titre',
            'body': 'Description',
            'image': 'Image',
        }