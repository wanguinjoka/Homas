from django import forms
from .models import Week, Breakfast, Supper, Lunch, Clean, Item, Note
from django.contrib.auth.models import User


class BreakfastUpdateForm(forms.ModelForm):

    class Meta:
        model = Breakfast
        fields = ['image', 'description', 'week']

class LunchUpdateForm(forms.ModelForm):

    class Meta:
        model = Lunch
        fields = ['image', 'description', 'week']

class SupperUpdateForm(forms.ModelForm):

    class Meta:
        model = Supper
        fields = ['image', 'description', 'week']