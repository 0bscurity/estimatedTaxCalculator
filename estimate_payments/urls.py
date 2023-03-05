from django.urls import path

from estimate_payments.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('self-employment-tax-calculator/', BusinessCalculator.as_view(), name='business-calculator'),
]
