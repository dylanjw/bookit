#!/usr/bin/env python3

from django.contrib.auth.forms import UserCreationForm
from .models import User as BookitUser


class BookitUserCreationForm(UserCreationForm):
    class Meta:
        model = BookitUser
        fields = ("username", "password1", "password2")
