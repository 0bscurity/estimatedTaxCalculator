def calculate_tax(self_employment_income, other_income, deductions, dependents, filing_status, local_tax):
    # Set to 0 if None
    self_employment_income = int(self_employment_income or 0)
    other_income = int(other_income or 0)
    deductions = int(deductions or 0)
    dependents = int(dependents or 0)
    # local_tax = int(local_tax or 0)

    # Define the tax brackets and rates for 2021 based on filing status
    if filing_status == "single":
        # Federal
        fed_tax_brackets = [
            (0, 9950),
            (9951, 40525),
            (40526, 86375),
            (86376, 164925),
            (164926, 209425),
            (209426, 523600),
            (523601, float('inf'))
        ]
        fed_tax_rates = [0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
        fed_standard_deduction = 12550

        # State
        state_tax_brackets = [
            (0, 1000),
            (1001, 2000),
            (2001, 3000),
            (3001, 100000),
            (100001, 125000),
            (125001, 150000),
            (150001, 250000),
            (250001, float('inf'))
        ]
        state_tax_rates = [0.02, 0.03, 0.04, 0.0475, 0.05, 0.0525, 0.055, 0.0575]
        state_standard_deduction = 2400

    elif filing_status == "married":
        # Federal
        fed_tax_brackets = [
            (0, 19900),
            (19901, 81050),
            (81051, 172750),
            (172751, 329850),
            (329851, 418850),
            (418851, 628300),
            (628301, float('inf'))
        ]
        fed_tax_rates = [0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
        fed_standard_deduction = 25100

        # State
        state_tax_brackets = [
            (0, 1000),
            (1001, 2000),
            (2001, 3000),
            (3001, 150000),
            (150001, 175000),
            (175001, 225000),
            (225001, 300000),
            (300001, float('inf'))
        ]
        state_tax_rates = [0.02, 0.03, 0.04, 0.0475, 0.05, 0.0525, 0.055, 0.0575]
        state_standard_deduction = 4850

    elif filing_status == "head_of_household":
        # Federal
        fed_tax_brackets = [
            (0, 14200),
            (14201, 54200),
            (54201, 86350),
            (86351, 164900),
            (164901, 209400),
            (209401, 523600),
            (523601, float('inf'))
        ]
        fed_tax_rates = [0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
        fed_standard_deduction = 18700

        # State
        state_tax_brackets = [
            (0, 1000),
            (1001, 2000),
            (2001, 3000),
            (3001, 125000),
            (125001, 150000),
            (150001, 200000),
            (200001, 250000),
            (250001, float('inf'))
        ]
        state_tax_rates = [0.02, 0.03, 0.04, 0.0475, 0.05, 0.0525, 0.055, 0.0575]
        state_standard_deduction = 4850

    else:
        raise ValueError("Invalid filing status")

    # Calculate the net income and self-employment tax
    gross_income = self_employment_income + other_income
    net_se_income = self_employment_income - deductions
    net_income = net_se_income + other_income

    se_tax = min(max(net_se_income * 0.9235 * 0.153, 0), 8950.40)

    # Calculate the taxable income based on filing status and dependents
    if filing_status == "single":
        federal_taxable_income = net_income - (fed_standard_deduction + (dependents * 4450))
        state_taxable_income = net_income - (state_standard_deduction + (dependents * 3250))
    else:
        federal_taxable_income = net_income - (fed_standard_deduction + (dependents * 4450 * 2))
        state_taxable_income = net_income - (state_standard_deduction + (dependents * 3250))

    # Calculate the federal income tax using the tax brackets and rates
    federal_tax = 0
    for i in range(len(fed_tax_brackets)):
        bracket_min, bracket_max = fed_tax_brackets[i]
        bracket_rate = fed_tax_rates[i]

        if federal_taxable_income >= bracket_max:
            federal_tax += (bracket_max - bracket_min + 1) * bracket_rate
        elif federal_taxable_income >= bracket_min:
            federal_tax += (federal_taxable_income - bracket_min + 1) * bracket_rate
            break

    # Calculate the state income tax using the tax brackets and rates
    state_tax = 0
    for i in range(len(state_tax_brackets)):
        bracket_min, bracket_max = state_tax_brackets[i]
        bracket_rate = state_tax_rates[i]

        if state_taxable_income >= bracket_max:
            state_tax += (bracket_max - bracket_min + 1) * bracket_rate
        elif state_taxable_income >= bracket_min:
            state_tax += (state_taxable_income - bracket_min + 1) * bracket_rate
            break

    local_tax = float(state_taxable_income) * float(local_tax)
    total_tax = state_tax + federal_tax + se_tax + local_tax

    # Federal Quarterly Payments -------------------------------------------------------------------------
    total_federal = federal_tax + se_tax
    f_month = total_federal / 12
    f_q1 = 3 * f_month
    f_q2 = 2 * f_month
    f_q3 = 3 * f_month
    f_q4 = 4 * f_month

    # State Quarterly Payments -------------------------------------------------------------------------
    total_state = state_tax + local_tax
    s_month = total_state / 12
    s_q1 = 3 * s_month
    s_q2 = 2 * s_month
    s_q3 = 3 * s_month
    s_q4 = 4 * s_month

    return federal_taxable_income, state_taxable_income, federal_tax, state_tax, local_tax, se_tax, total_tax, \
           gross_income, f_q1, f_q2, f_q3, f_q4, s_q1, s_q2, s_q3, s_q4
