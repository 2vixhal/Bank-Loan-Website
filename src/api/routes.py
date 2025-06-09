from fastapi import APIRouter
from src.services.loan_service import LoanService

router = APIRouter()

@router.post("/loans/apply")
async def apply_loan(loan_request: dict):
    return await LoanService.apply_loan(loan_request)

@router.get("/loans/{loan_id}")
async def get_loan(loan_id: int):
    return await LoanService.get_loan(loan_id)

@router.put("/loans/{loan_id}/approve")
async def approve_loan(loan_id: int):
    return await LoanService.approve_loan(loan_id)

@router.delete("/loans/{loan_id}")
async def delete_loan(loan_id: int):
    return await LoanService.delete_loan(loan_id)