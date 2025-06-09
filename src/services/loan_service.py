from typing import Dict, Any

class LoanService:
    def __init__(self):
        pass

    def calculate_emi(self, principal: float, rate_of_interest: float, tenure: int) -> float:
        """
        Calculate the Equated Monthly Installment (EMI) for a loan.
        
        :param principal: The principal amount of the loan
        :param rate_of_interest: The annual interest rate (in percentage)
        :param tenure: The tenure of the loan in months
        :return: The calculated EMI
        """
        monthly_rate = rate_of_interest / (12 * 100)
        emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure) / ((1 + monthly_rate) ** tenure - 1)
        return emi

    def approve_loan(self, applicant_data: Dict[str, Any]) -> bool:
        """
        Approve or reject a loan application based on applicant data.
        
        :param applicant_data: A dictionary containing applicant details
        :return: True if approved, False otherwise
        """
        # Placeholder logic for loan approval
        if applicant_data.get('credit_score', 0) >= 700 and applicant_data.get('income', 0) >= 30000:
            return True
        return False

    def get_loan_details(self, loan_id: str) -> Dict[str, Any]:
        """
        Retrieve loan details based on loan ID.
        
        :param loan_id: The ID of the loan
        :return: A dictionary containing loan details
        """
        # Placeholder for fetching loan details from a database or data source
        return {
            "loan_id": loan_id,
            "amount": 50000,
            "interest_rate": 7.5,
            "tenure": 24,
            "emi": self.calculate_emi(50000, 7.5, 24)
        }