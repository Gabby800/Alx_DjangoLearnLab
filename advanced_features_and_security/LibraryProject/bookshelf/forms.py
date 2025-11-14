from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
    # Additional validation example
    def clean_title(self):
        title = self.cleaned_data['title']
        if '<script>' in title.lower():
            raise forms.ValidationError("Invalid characters in title.")
        return title
