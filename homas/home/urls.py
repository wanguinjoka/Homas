from django.conf.urls import url
from .views import WeekDetailView, WeekUpdateView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$', views.home, name='home'),
    url(r'^Week/(?P<pk>[0-9]+)/$', WeekDetailView.as_view(), name='week-detail'),
    url(r'^Week/(?P<pk>[0-9]+)/update/$', WeekUpdateView.as_view(), name='week-update'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
