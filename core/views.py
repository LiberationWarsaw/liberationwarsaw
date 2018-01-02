from django.shortcuts import render
from django.views.generic.base import TemplateView
from core.models import Event, Tag, Level
from django.views.generic import ListView


class HomePageView(TemplateView):
    """
    Welcome screen with calls to action.
    """
    template_name = 'core/index.html'

class AboutPageView(TemplateView):
    """
    """
    template_name = 'core/about.html'

class EventsListView(ListView):
    """
    """
    template_name = 'core/event-list.html'
    model = Event

class ContactPageView(TemplateView):
    """
    """
    template_name = 'core/contact.html'

class PledgePageView(TemplateView):
    """
    """
    template_name = 'core/pledge.html'

class RescuePageView(TemplateView):
    """
    """
    template_name = 'core//rescue.html'

class SavePageView(TemplateView):
    """
    """
    template_name = 'core/save.html'
