#!/usr/bin/env python3

from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from django import forms
from django.forms import ModelForm
from .models import (
    User as BookitUser,
    BookitEvent,
)


START_TIME_SLOTS = [
    ('10:00:00', '10am'),
    ('16:00:00', '4pm'),
]

END_TIME_SLOTS = [
    ('16:00:00', '4pm'),
    ('22:00:00', '10pm')
]


class BookitUserCreationForm(UserCreationForm):
    class Meta:
        model = BookitUser
        fields = ("username", "password1", "password2")


class EventDateSelectorWidget(forms.MultiWidget):
    def __init__(self, attrs=None, time_slots=None):
        widgets = [
            forms.DateInput(attrs=attrs),
            forms.Select(attrs=attrs, choices=time_slots),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, datetime):
            return [value.date, value.time]
        elif isinstance(value, str):
            date, time = value.split('T')
            return [date, time]
        return [None, None]

    def value_from_datadict(self, data, files, name):
        date, time = super().value_from_datadict(data, files, name)
        # DateField expects a single string that it can parse into a date.
        return '{}T{}'.format(date, time)


class BookitEventCreationForm(ModelForm):
    class Meta:
        model = BookitEvent
        fields = ["start", "end"]
        widgets = {
            'start': EventDateSelectorWidget(time_slots=START_TIME_SLOTS),
            'end': EventDateSelectorWidget(time_slots=END_TIME_SLOTS)
        }
