from pydantic import BaseModel
from typing import List, Optional

class LoanApplicationSchema(BaseModel):
    applicant_name: str
    applicant_income: float
    loan_amount: float
    loan_term: int  # in months
    purpose: str
    credit_score: Optional[int] = None

class LoanApprovalResponseSchema(BaseModel):
    application_id: str
    approved_amount: float
    interest_rate: float
    monthly_emi: float
    status: str  # e.g., "approved", "rejected"

class ErrorResponseSchema(BaseModel):
    error_code: int
    error_message: str

class LoanDetailsSchema(BaseModel):
    loan_id: str
    applicant_name: str
    loan_amount: float
    loan_term: int
    status: str  # e.g., "active", "closed"
    remaining_balance: float
    payment_history: List[float]  # List of payments made