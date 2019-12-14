"""bookit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

import core.views as core_views

urlpatterns = [
    path('', core_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', core_views.signup, name='signup'),
    path('calendar/',
         core_views.CalendarView.as_view(),
         name='full_calendar',
         ),
    path('booking/create/',
         core_views.CreateEventView.as_view(),
         name='create_booking',
         ),
    path('booking/edit/',
         core_views.EditBookingView.as_view(),
         name='edit_booking',
         ),
    re_path(r'^schedule/', include('schedule.urls')),
]
