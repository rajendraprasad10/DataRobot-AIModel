from pydantic import BaseModel
from typing import List


class PredictionValueSchema(BaseModel):
    label: int
    value: float


class PredictionDataSchema(BaseModel):
    rowId: int
    prediction: int
    predictionThreshold: float
    predictionValues: List[PredictionValueSchema]
    deploymentApprovalStatus: str


class PredictionRequest(BaseModel):
    data: List[PredictionDataSchema]
