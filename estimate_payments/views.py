from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView

from estimate_payments.calculations import calculate_tax
from estimate_payments.forms import InfoForm
from estimate_payments.models import Results


class Home(TemplateView):
    template_name = 'estimated_payments/home.html'


class GetInfo(FormView):
    template_name = 'estimated_payments/tax-calculator.html'
    form_class = InfoForm

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
        other_income = form.cleaned_data['other_income']
        dependents = form.cleaned_data['dependents']

        calc = calculate_tax(filing_status=filing_status, self_employment_income=self_employment_income,
                             other_income=other_income, dependents=dependents, deductions=deductions,
                             local_tax=local_tax)

        # calc = calculate_tax(other_income=other_income,
        #                      self_employment_income=self_employment_income, deductions=deductions,
        #                      local=local_tax, filing_status=filing_status)

        custom_context = {
            "form": form,
            "f_taxable_income": calc[0],
            "s_taxable_income": calc[1],
            "federal_tax": calc[2],
            "state_tax": calc[3],
            "local_tax": calc[4],
            "self_employment_tax": calc[5],
            "total_tax": calc[6],
            "total_income": calc[7],

            "f_q1": calc[8],
            "f_q2": calc[9],
            "f_q3": calc[10],
            "f_q4": calc[11],

            "s_q1": calc[12],
            "s_q2": calc[13],
            "s_q3": calc[14],
            "s_q4": calc[15],
        }

        context = self.get_context_data(form=form)
        context.update(custom_context)

        return render(self.request, self.template_name, context)


# class GetInfo(FormView):
#     template_name = 'estimated_payments/tax-calculator.html'
#     form_class = InfoForm
#     success_url = '/results/'
#
#         def form_valid(self, form):
#             self_employment_income = form.cleaned_data['self_employment_income']
#             deductions = form.cleaned_data['deductions']
#             local_tax = form.cleaned_data['state_tax_area']
#             other_income = form.cleaned_data['other_income']
#
#             calculate_tax(other_income=other_income, self_employment_income=self_employment_income, deductions=deductions,
#                           local=local_tax)
#
#             return super().form_valid(form)


class Result(ListView):
    model = Results
    template_name = 'estimated_payments/results.html'
