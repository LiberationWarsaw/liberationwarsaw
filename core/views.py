from django.http import HttpResponseRedirect
from django.db.models import Q
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from core.models import Event, Tag, Level, Email

from .forms import EmailForm


class HomePageView(TemplateView):
    """
    Welcome screen with calls to action.
    """
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['upcoming_events'] = Event.objects.filter(
            start_time__gte=timezone.now()
        ).order_by('start_time')[:4]

        context['form'] = EmailForm()

        return context

    def post(self, request):
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            email = form.cleaned_data['email']
            Email.objects.create(
                email=email,
            )
            # redirect to a new URL:
            return HttpResponseRedirect('/')


class AboutPageView(TemplateView):
    """
    """
    template_name = 'core/about.html'


class AnonymousPageView(TemplateView):
    """
    """
    template_name = 'core/anonymous.html'

    def get_context_data(self, **kwargs):
        context = super(AnonymousPageView, self).get_context_data(**kwargs)
        context['upcoming_events'] = Event.objects.filter(
            start_time__gte=timezone.now()
        ).filter(
            tags__title="Cube"
        ).order_by('start_time')[:3]
        return context


class ContactPageView(TemplateView):
    """
    """
    template_name = 'core/contact.html'


class EventsListView(ListView):
    """
    """
    model = Event
    context_object_name = 'upcoming_events'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)

        context['form'] = EmailForm()

        return context

    def get_queryset(self):
        return Event.objects.filter(
            start_time__gte=timezone.now()
        ).order_by('start_time')


    def post(self, request):
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            email = form.cleaned_data['email']
            Email.objects.create(
                email=email,
            )
            # redirect to a new URL:
            return HttpResponseRedirect('/events')



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

    def get_context_data(self, **kwargs):
        context = super(SavePageView, self).get_context_data(**kwargs)
        context['upcoming_events'] = Event.objects.filter(
            start_time__gte=timezone.now()
        ).filter(
            Q(tags__title="Vigil") | Q(tags__title="Truck Stop")
        ).order_by('start_time')[:3]
        return context
