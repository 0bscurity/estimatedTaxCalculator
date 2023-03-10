from django import forms

# Data common to all maryland calculators
# TODO: These should be database driven eventually
TAX_AREAS = (
    ('0', '----'),
    ('.0306', 'Harford County'),
    ('.0320', 'Baltimore City'),
    ('.0320', 'Baltimore County'),
    ('.0296', 'Fredrick County'),
)

FILING_STATUS = (
    ('single', 'For Single Filers'),
    ('married', 'For Married Individuals Filing Joint Returns'),
    ('head_of_household', 'For Head\'s of Households')
)


class BusinessCalculatorForm(forms.Form):
    filing_status = forms.ChoiceField(choices=FILING_STATUS, required=False, label='FILING STATUS')
    self_employment_income = forms.DecimalField(required=False, label='SELF EMPLOYMENT INCOME')
    deductions = forms.DecimalField(required=False, label='DEDUCTIONS')
    state_tax_area = forms.ChoiceField(choices=TAX_AREAS, required=False, label='STATE TAX AREA')
    dependents = forms.IntegerField(required=False, label='DEPENDENTS')


class IndividualCalculatorForm(forms.Form):
    filing_status = forms.ChoiceField(choices=FILING_STATUS, required=False, label='FILING STATUS')
    income = forms.DecimalField(required=False, label='YEARLY INCOME')
    state_tax_area = forms.ChoiceField(choices=TAX_AREAS, required=False, label='STATE TAX AREA')
    dependents = forms.IntegerField(required=False, label='DEPENDENTS')
