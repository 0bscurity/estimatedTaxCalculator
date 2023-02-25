from django.db import models


class Results(models.Model):
    adjusted_federal_income = models.DecimalField(max_digits=10, decimal_places=2)
    adjusted_state_income = models.DecimalField(max_digits=10, decimal_places=2)

    self_employment_tax = models.DecimalField(max_digits=10, decimal_places=2)
    state_tax = models.DecimalField(max_digits=10, decimal_places=2)
    federal_tax = models.DecimalField(max_digits=10, decimal_places=2)
    local_tax = models.DecimalField(max_digits=10, decimal_places=2)

    total_tax = models.DecimalField(max_digits=10, decimal_places=2)
