from django.db import models
from django import forms
from model_form.models import Author, Book
from django.forms import ModelForm


class AuthorForm(ModelForm):
    model = Author
    fields = ['name', 'title', 'birth_date']


class BookForm(ModelForm):
    model = Book
    fields = ['name', 'authors']