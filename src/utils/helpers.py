def calculate_emi(principal, rate_of_interest, tenure):
    """
    Calculate the Equated Monthly Installment (EMI) for a loan.

    :param principal: The loan amount
    :param rate_of_interest: The annual interest rate (in percentage)
    :param tenure: The loan tenure (in months)
    :return: The calculated EMI
    """
    monthly_rate = rate_of_interest / (12 * 100)
    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure) / ((1 + monthly_rate) ** tenure - 1)
    return emi

def validate_loan_amount(amount):
    """
    Validate the loan amount.

    :param amount: The loan amount to validate
    :return: True if valid, False otherwise
    """
    return amount > 0

def validate_tenure(tenure):
    """
    Validate the loan tenure.

    :param tenure: The loan tenure to validate (in months)
    :return: True if valid, False otherwise
    """
    return tenure > 0

def format_currency(amount):
    """
    Format the amount as currency.

    :param amount: The amount to format
    :return: Formatted currency string
    """
    return "${:,.2f}".format(amount)