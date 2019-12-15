#!/usr/bin/env python3
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404

import schedule.views
from schedule.models import Calendar

from .forms import (
    BookitUserCreationForm,
    BookitEventCreationForm,
)

# from core.models import BookitUserCalendar

@login_required
def home(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {'booking_form': BookitEventCreationForm})
    else:
        return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = BookitUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = BookitUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class CalendarView(schedule.views.CalendarView):
    template_name = "schedule/dashboard.html"
    def get_object(self):
        return get_object_or_404(
            Calendar,
            slug=self.request.user.username)


class CreateEventView(schedule.views.CreateEventView):
    # Use the user calendar, and dont require a slug
    def form_valid(self, form):
        event = form.save(commit=False)
        event.creator = self.request.user
        event.calendar = Calendar.objects.get_calendar_for_object(
            self.request.user)
        event.save()
        return HttpResponseRedirect(event.get_absolute_url())


class CreateBookingView(schedule.views.CreateEventView):
    pass


class EditBookingView(schedule.views.EditOccurrenceView):
    pass
