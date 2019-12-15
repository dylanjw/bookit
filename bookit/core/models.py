#!/usr/bin/env python3

from django.db import (
    models,
)
from django.db.models.query import (
    QuerySet,
)
from django.contrib.auth.models import (
    AbstractUser,
    UserManager,
)

from schedule.models import (
    Calendar,
    Event,
)

'''Notes about `schedule`

Event is like a set of recurring booking
Occurance is like a booking


'''


class BookitUserManager(UserManager):
    pass


class User(AbstractUser):
    objects = BookitUserManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Calendar.objects.get_or_create_calendar_for_object(
            self)


class BookitEvent(Event):
    pass
