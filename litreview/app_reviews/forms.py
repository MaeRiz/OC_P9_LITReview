from django import forms


RATING_CHOISES = ['1', '2', '3', '4', '5']

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
    description = forms.CharField(
        required=True,
        label='Description',
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description",
            },
        ),
    )
    image = forms.ImageField(
        required=True,
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
        widget=forms.Textarea(
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
