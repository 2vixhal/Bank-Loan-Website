def calculate_emi(principal, annual_rate, tenure_months):
    """
    Calculate monthly EMI using compound interest formula.

    Args:
        principal (float): Loan amount in ₹
        annual_rate (float): Annual interest rate in %
        tenure_months (int): Loan tenure in months

    Returns:
        float: EMI value rounded to 2 decimal places
    """
    if annual_rate == 0:
        return round(principal / tenure_months, 2)  # Avoid division by zero

    r = ((annual_rate / 12) / 100)  # Monthly interest rate
    t = tenure_months

    emi = (principal * r * (1 + r)**t) / ((1 + r)**t - 1)
    return round(emi, 2)
