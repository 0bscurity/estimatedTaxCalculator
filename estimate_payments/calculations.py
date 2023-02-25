from .models import Results


def calculate_tax(other_income, self_employment_income, deductions, local):

    federal_sd = 13850
    state_sd = 2250
    federal_tax = 0
    state_tax = 0

    if self_employment_income:
        self_employment_income = int(self_employment_income)
    else:
        self_employment_income = 0

    if other_income:
        other_income = int(other_income)
    else:
        other_income = 0

    if deductions:
        deductions = int(deductions)
    else:
        deductions = 0

    # Get total Income
    total_income = self_employment_income + other_income

    # Get Federal Taxable Income
    f_taxable_income = self_employment_income + other_income - federal_sd

    # Get State Taxable Income
    s_taxable_income = self_employment_income + other_income - state_sd
    local_tax = float(s_taxable_income) * float(local)

    # Get Federal Tax
    if f_taxable_income in range(0, 11000):
        federal_tax = f_taxable_income * .10
    elif f_taxable_income in range(11001, 44725):
        federal_tax = f_taxable_income * .12
    elif f_taxable_income in range(44726, 95375):
        federal_tax = f_taxable_income * .22
    elif f_taxable_income in range(95376, 182100):
        federal_tax = f_taxable_income * .24
    elif f_taxable_income in range(182101, 231250):
        federal_tax = f_taxable_income * .32
    elif f_taxable_income in range(231251, 578125):
        federal_tax = f_taxable_income * .35
    elif f_taxable_income > 578125:
        federal_tax = f_taxable_income * .37

    # Get Self-Employment Tax
    self_employment_tax = (self_employment_income - deductions) * .153

    # Get State Tax
    if s_taxable_income in range(0, 1000):
        state_tax = s_taxable_income * .02
    elif s_taxable_income in range(1001, 2000):
        state_tax = (s_taxable_income + 20 - 1000) * .03
    elif s_taxable_income in range(2001, 3000):
        state_tax = (s_taxable_income + 50 - 2000) * .04
    elif s_taxable_income in range(3001, 100000):
        state_tax = (s_taxable_income + 90 - 3000) * .0475
    elif s_taxable_income in range(100001, 125000):
        state_tax = (s_taxable_income + 4697.50 - 100000) * .05
    elif s_taxable_income in range(125001, 150000):
        state_tax = (s_taxable_income + 5947.50 - 125000) * .0525
    elif s_taxable_income in range(150001, 250000):
        state_tax = (s_taxable_income + 7260 - 150000) * .055
    elif s_taxable_income > 250000:
        state_tax = (s_taxable_income + 12760 - 25000) * .075

    total_tax = federal_tax + self_employment_tax + state_tax + local_tax

    print(f'----------------------------------------')

    print(f'Adjusted Federal Gross Income - ${f_taxable_income}')
    print(f'Adjusted State Gross Income - ${s_taxable_income}')

    print(f'----------------------------------------')

    print(f'Federal Taxes Owed - ${federal_tax}')
    print(f'State Taxes Owed - ${state_tax}')
    print(f'Local Taxes Owed - ${local_tax}')

    print(f'')

    print(f'Self-Employment Taxes Owed - ${self_employment_tax}')

    print(f'Total Federal Taxes Owed - ${federal_tax + self_employment_tax}')
    print(f'Total State Taxes Owed - ${state_tax + local_tax}')

    print(f'----------------------------------------')
    print(f'')

    print(f'Total Taxes Owed - ${total_tax}')

    print(f'')
    print(f'----------------------------------------')

    # Federal Quarterly Payments -------------------------------------------------------------------------
    total_federal = federal_tax + self_employment_tax
    f_month = total_federal / 12
    f_q1 = 3 * f_month
    f_q2 = 2 * f_month
    f_q3 = 3 * f_month
    f_q4 = 4 * f_month

    total_state = state_tax + local_tax
    s_month = total_state / 12
    s_q1 = 3 * s_month
    s_q2 = 2 * s_month
    s_q3 = 3 * s_month
    s_q4 = 4 * s_month


    return f_taxable_income, s_taxable_income, federal_tax, state_tax, local_tax, self_employment_tax, total_tax, \
           total_income, f_q1, f_q2, f_q3, f_q4, s_q1, s_q2, s_q3, s_q4
