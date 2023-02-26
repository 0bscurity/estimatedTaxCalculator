from django.urls import path

from estimate_payments.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('tax-calculator/', GetInfo.as_view(), name='get-info'),
    path('results/', Result.as_view(), name='results'),
]
