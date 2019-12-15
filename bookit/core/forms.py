#!/usr/bin/env python3

from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import (
    User as BookitUser,
    BookitEvent,
)


class BookitUserCreationForm(UserCreationForm):
    class Meta:
        model = BookitUser
        fields = ("username", "password1", "password2")


class BookitEventCreationForm(ModelForm):
    class Meta:
        model = BookitEvent
        fields = ["start", "end"]
