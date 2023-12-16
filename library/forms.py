from django import forms
from django.core.exceptions import ValidationError

from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_year', 'isbn')
    
    def clean_isbn(self):
        data = self.cleaned_data["isbn"]
        isbn_len =  len(data)
        if 10 > isbn_len or isbn_len > 13:
            raise ValidationError("ISBN should be between 10 and 13")
        return data
    
    def clean_publication_year(self):
        data = self.cleaned_data["publication_year"]
        # we can some validations to publication_year here
        return data
    