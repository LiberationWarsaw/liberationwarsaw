from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    """
    Welcome screen with calls to action.
    """
    template_name = 'core/index.html'

class AboutPageView(TemplateView):
    """
    """
    template_name = 'core/about.html'

class EventsPageView(TemplateView):
    """
    """
    template_name = 'core/events.html'

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
