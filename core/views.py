from django.shortcuts import render
from django.views.generic.base import TemplateView
from core.models import Event, Tag, Level
from django.views.generic import ListView
from django.utils import timezone



class HomePageView(TemplateView):
    """
    Welcome screen with calls to action.
    """
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['upcoming_events'] = Event.objects.filter(
            start_time__gte=timezone.now()
        ).order_by('-start_time')[:4]
        return context


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
    template_name = 'core/rescue.html'


class SavePageView(TemplateView):
    """
    """
    template_name = 'core/save.html'
