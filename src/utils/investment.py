def lumpsum_investment(principal, rate, years):
    return round(principal * ((1 + rate / 100) ** years), 2)

def sip_investment(monthly_invest, rate, years):
    r = rate / 12 / 100
    n = years * 12
    future_value = monthly_invest * (((1 + r)**n - 1) * (1 + r)) / r
    return round(future_value, 2)

def swp_withdrawal(investment, monthly_withdrawal, rate, years):
    r = rate / 12 / 100
    n = years * 12
    total_withdrawn = monthly_withdrawal * n
    # Simple reduction calculation for now
    future_value = investment * ((1 + r)**n) - total_withdrawn
    return round(future_value, 2)
