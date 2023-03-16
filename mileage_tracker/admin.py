from django.contrib import admin

from mileage_tracker.models import Vehicle, MileageEntry

admin.site.register(Vehicle)
admin.site.register(MileageEntry)
