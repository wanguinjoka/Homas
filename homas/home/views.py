from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Week, Breakfast, Supper, Lunch, Clean, Item, Note
from .forms import BreakfastUpdateForm, LunchUpdateForm, SupperUpdateForm
# Create your views here.

def home(request):
    context={
        'weeks': Week.objects.all()
    }
    return render(request,'home/index.html', context)

class WeekDetailView(LoginRequiredMixin, DetailView):
     model = Week

class WeekUpdateView(LoginRequiredMixin,UpdateView):
    model = Week
    fields = ['image','quote']

class CleanCreateView(LoginRequiredMixin, CreateView):
    model = Clean
    fields = ['room','details','week']



@login_required
def MealPlan(request):
    if request.method == 'POST':
        b_form = BreakfastUpdateForm(request.POST, request.FILES)
        l_form = LunchUpdateForm(request.POST, request.FILES)
        s_form = SupperUpdateForm(request.POST, request.FILES)

        if b_form.is_valid() and l_form.is_valid() and s_form.is_valid():
            b_form.save()
            l_form.save()
            s_form.save()
            messages.success(request, f'Your meal plan has been updated!')
            return redirect('home')

    else:
        b_form = BreakfastUpdateForm()
        l_form = LunchUpdateForm()
        s_form = SupperUpdateForm()

    context = {
        'b_form': b_form,
        'l_form': l_form,
        's_form': s_form
    }

    return render(request, 'home/mealplan.html', context)




