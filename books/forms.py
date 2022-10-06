from django import forms
from .models import Author,Books
from django.forms.models import (
    inlineformset_factory
)

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = (
            "title",
            "namber_of_pages"
        )
    
BookFormSet = inlineformset_factory(
    Author,
    Books,
    BookForm,
    can_delete=False,
    min_num=2,
    extra=0
)