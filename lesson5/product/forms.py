from django import forms
from .models import Apartments
class ApartmentsForm(forms.ModelForm):
    class Meta:
        model = Apartments
        fields = ['title', 'desc', 'rooms', 'address', 'image', 'price']