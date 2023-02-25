from django import forms


class InfoForm(forms.Form):
    TAX_AREAS = (
        ('0', '----'),
        ('.0306', 'Harford County'),
        ('.0320', 'Baltimore County')
    )

    other_income = forms.DecimalField(required=False)
    self_employment_income = forms.DecimalField(required=False)
    deductions = forms.DecimalField(required=False)
    state_tax_area = forms.ChoiceField(choices=TAX_AREAS)
