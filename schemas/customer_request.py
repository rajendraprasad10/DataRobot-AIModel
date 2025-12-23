from enum import Enum
from pydantic import BaseModel



class ContractType(str, Enum):
    month_to_month = "Month-to-month"
    one_year = "One year"
    two_year = "Two year"


class InternetService(str, Enum):
    dsl = "DSL"
    fiber = "Fiber optic"
    none = "None"


class PaymentMethod(str, Enum):
    electronic_check = "Electronic check"
    mailed_check = "Mailed check"
    bank_transfer = "Bank transfer"
    credit_card = "Credit card"


# ---------------------------
# Request Schema
# ---------------------------
class CustomerRequest(BaseModel):
    gender: str
    age: int
    tenure: int
    monthly_charges: float
    total_charges: float
    contract_type: ContractType
    internet_service: InternetService
    payment_method: PaymentMethod
