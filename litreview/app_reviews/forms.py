from django import forms
from django.forms.widgets import Select

from .models import Review, Ticket

RATING_CHOISES = ['1', '2', '3', '4', '5']

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = (
            'title',
            'content',
            'image',
        )

class RawCreateTicketForm(forms.Form):
    title = forms.CharField(
        required=True,
        label='Titre',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Titre"
            },
        ),
    )
    content = forms.CharField(
        required=True,
        label='Description',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Description",
            },
        ),
    )
    image = forms.ImageField(
        required=True,
    )
    

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'headline',
            'rating',
            'body',
        )


class RawCreateReviewForm(forms.Form):
    CHOICES = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'))
    headline = forms.CharField(
        required=True,
        label='Titre',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Titre"
            },
        ),
    )
    body = forms.CharField(
        required=True,
        label='Description',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Description",
            },
        ),
    )
    rating = forms.MultipleChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
