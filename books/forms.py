from django import forms
from .models import Book, Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'desc', 'rate', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple,
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
