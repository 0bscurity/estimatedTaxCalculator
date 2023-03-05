from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView

from estimate_payments.calculations import calculate_se_tax
from estimate_payments.forms import BusinessCalculatorForm


class Home(TemplateView):
    template_name = 'estimated_payments/home.html'


class BusinessCalculator(FormView):
    template_name = 'estimated_payments/se-tax-calculator.html'
    form_class = BusinessCalculatorForm

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def form_valid(self, form):
        filing_status = form.cleaned_data['filing_status']
        self_employment_income = form.cleaned_data['self_employment_income']
        deductions = form.cleaned_data['deductions']
        local_tax = form.cleaned_data['state_tax_area']
        dependents = form.cleaned_data['dependents']

        results = calculate_se_tax(filing_status=filing_status, self_employment_income=self_employment_income,
                                   dependents=dependents, deductions=deductions,
                                   local_tax=local_tax)

        custom_context = {
            "form": form,
            "total_income": results.gross_income,
            "total_tax": results.total_tax,
            "s_taxable_income": results.state_taxable_income,
            "f_taxable_income": results.federal_taxable_income,
            "social": results.social_security_tax,
            "medicare": results.medicare_tax,
            "federal_tax": results.federal_tax,
            "state_tax": results.state_tax,
            "local_tax": results.local_tax,
            "self_employment_tax": results.se_tax,

            "f_q1": results.f_q1,
            "f_q2": results.f_q2,
            "f_q3": results.f_q3,
            "f_q4": results.f_q4,

            "s_q1": results.s_q1,
            "s_q2": results.s_q2,
            "s_q3": results.s_q3,
            "s_q4": results.s_q4,
        }

        context = self.get_context_data(form=form)
        context.update(custom_context)

        return render(self.request, self.template_name, context)
