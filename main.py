from fastapi import FastAPI
from src.api.routes import router as api_router  # keep if you have your other routes here
from src.utils.investment import lumpsum_investment, sip_investment, swp_withdrawal
app = FastAPI(title="AI-Powered Loan Assistant Platform")

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to Loan & Investment Calculator API"}

# Include other routes if you have them
app.include_router(api_router)

# EMI Calculator logic
def calculate_emi(principal: float, tenure_years: int, annual_rate: float) -> float:
    monthly_rate = annual_rate / (12 * 100)
    n = tenure_years * 12
    emi = principal * monthly_rate * (1 + monthly_rate) ** n / ((1 + monthly_rate) ** n - 1)
    return round(emi, 2)

# Investment Calculator logic
def lumpsum_future_value(principal: float, annual_rate: float, years: int) -> float:
    r = annual_rate / 100
    fv = principal * ((1 + r) ** years)
    return round(fv, 2)

# Pydantic models
from pydantic import BaseModel

class EMICalcRequest(BaseModel):
    principal: float
    tenure_years: int
    annual_interest_rate: float

class LumpsumRequest(BaseModel):
    principal: float
    annual_interest_rate: float
    years: int

class SIPRequest(BaseModel):
    monthly_investment: float
    annual_interest_rate: float
    years: int

class SWPRequest(BaseModel):
    initial_investment: float
    monthly_withdrawal: float
    annual_interest_rate: float
    years: int

# Calculator endpoints
@app.post("/emi")
async def emi_calculator(data: EMICalcRequest):
    emi = calculate_emi(data.principal, data.tenure_years, data.annual_interest_rate)
    return {"emi": emi}

@app.post("/investment/lumpsum")
async def calculate_lumpsum(data: LumpsumRequest):
    fv = lumpsum_investment(data.principal, data.annual_interest_rate, data.years)
    return {"future_value": fv}

@app.post("/investment/sip")
async def calculate_sip(data: SIPRequest):
    fv = sip_investment(data.monthly_investment, data.annual_interest_rate, data.years)
    return {"future_value": fv}

@app.post("/investment/swp")
async def calculate_swp(data: SWPRequest):
    fv = swp_withdrawal(data.initial_investment, data.monthly_withdrawal, data.annual_interest_rate, data.years)
    return {"remaining_investment": fv}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

