from django import forms
from .models import Week, Breakfast, Supper, Lunch, Clean, Item, Note
from django.contrib.auth.models import User


class BreakfastUpdateForm(forms.ModelForm):

    class Meta:
        model = Breakfast
        fields = ['image', 'details', 'week']

class LunchUpdateForm(forms.ModelForm):

    class Meta:
        model = Lunch
        fields = ['image', 'details', 'week']

class SupperUpdateForm(forms.ModelForm):

    class Meta:
        model = Supper
        fields = ['image', 'details', 'week']