from django.views.generic import TemplateView

from mileage_tracker.models import Vehicle


class MileageTrackerLanding(TemplateView):
    template_name = 'mileage_tracker/mileage-tracker-landing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user.id
        vehicles = Vehicle.objects.filter(user=user)

        context['vehicles'] = vehicles

        return context
