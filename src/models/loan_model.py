class LoanModel:
    def __init__(self, principal: float, interest_rate: float, term_years: int):
        self.principal = principal
        self.interest_rate = interest_rate
        self.term_years = term_years

    def calculate_emi(self) -> float:
        monthly_interest_rate = self.interest_rate / (12 * 100)
        number_of_months = self.term_years * 12
        emi = (self.principal * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_months) / \
              ((1 + monthly_interest_rate) ** number_of_months - 1)
        return emi

    def total_payment(self) -> float:
        return self.calculate_emi() * self.term_years * 12

    def total_interest(self) -> float:
        return self.total_payment() - self.principal

    def validate(self) -> bool:
        if self.principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if self.interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if self.term_years <= 0:
            raise ValueError("Term in years must be greater than zero.")
        return True