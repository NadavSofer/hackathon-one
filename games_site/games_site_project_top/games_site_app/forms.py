# forms.py

from django import forms
from .models import Reviews

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'review_description', 'rating']

    name = forms.CharField(
        max_length=50,
        label='Review title'
    )
    review_description = forms.CharField(
        label='Your Review',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    rating = forms.IntegerField(
        label='Your Rating (out of 5)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '5'})
    )
