from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Week, Breakfast, Supper, Lunch, Clean, Item, Note
# Create your views here.

def home(request):
    context={
        'weeks': Week.objects.all()
    }
    return render(request,'home/index.html', context)
