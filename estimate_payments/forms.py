from django import forms


class InfoForm(forms.Form):
    TAX_AREAS = (
        ('0', '----'),
        ('.0306', 'Blank County'),
        ('.0320', 'Blank County')
    )

    FILING_STATUS = (
        ('single', 'For Single Filers'),
        ('married', 'For Married Individuals Filing Joint Returns'),
        ('head_of_household', 'For Head\'s of Households')
    )

    filing_status = forms.ChoiceField(choices=FILING_STATUS)
    self_employment_income = forms.DecimalField(required=False)
    other_income = forms.DecimalField(required=False)
    state_tax_area = forms.ChoiceField(choices=TAX_AREAS)
    deductions = forms.DecimalField(required=False)
    dependents = forms.IntegerField(required=False)
