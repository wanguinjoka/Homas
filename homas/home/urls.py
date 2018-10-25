from django.conf.urls import url
from .views import (
    WeekDetailView,
    WeekUpdateView, 
    CleanCreateView,
    ItemCreateView,
    NoteCreateView,
    NoteDeleteView,
    ItemDeleteView
)
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$', views.home, name='home'),
    url(r'^Week/(?P<pk>[0-9]+)/$', WeekDetailView.as_view(), name='week-detail'),
    url(r'^Week/(?P<pk>[0-9]+)/update/$', WeekUpdateView.as_view(), name='week-update'),
    url(r'^mealplan/', views.MealPlan, name = 'mealplan'),
    url(r'^clean/new/', CleanCreateView.as_view(), name='clean-create'),
    url(r'^item/new/', ItemCreateView.as_view(), name='item-create'),
    url(r'^note/new/', NoteCreateView.as_view(), name='note-create'),
    url(r'^note/(?P<pk>[0-9]+)/delete/$', NoteDeleteView.as_view(), name='note-delete'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
