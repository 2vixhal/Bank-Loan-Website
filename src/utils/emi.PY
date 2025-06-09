def calculate_emi(principal, annual_rate, tenure_months):
    r = annual_rate / 12 / 100
    t = tenure_months
    emi = (principal * r * (1 + r)**t) / ((1 + r)**t - 1)
    return round(emi, 2)
