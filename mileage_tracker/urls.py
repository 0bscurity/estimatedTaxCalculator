from django.urls import path

from .views import *

urlpatterns = [
    path('mileage-tracker/', MileageTrackerLanding.as_view(), name='mileage-tracker-landing'),
]
