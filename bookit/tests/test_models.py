import pytest

from django.test import TestCase

from dateutil.relativedelta import relativedelta
from datetime import datetime
import pytz

from core.models import (
    User,
)

from schedule.models import (
    Calendar,
)


pytestmark = pytest.mark.django_db


def test_user_creation_with_related_calendar():
    user = User(username="test", password="test")
    user.save()
    assert User.objects.get(username='test')
    calendar = Calendar.objects.get_calendar_for_object(user)
    assert calendar
