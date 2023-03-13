from django.views.generic import TemplateView


class MileageTrackerLanding(TemplateView):
    template_name = 'mileage_tracker/mileage-tracker-landing.html'
