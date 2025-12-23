from fastapi import FastAPI, HTTPException
from schemas.customer_request import CustomerRequest
from database import engine, Base
import requests
import config as Constants

from database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from models import User, Prediction, PredictionValue
from schemas.priductive import PredictionRequest
# ---------------------------
# FastAPI app
# ---------------------------
app = FastAPI(title="Customer Churn Prediction API")

# ---------------------------
# DataRobot Configuration
# ---------------------------
API_KEY = Constants.API_KEY  # use env in prod
DR_URL = Constants.DR_URL

HEADERS = {
    "Authorization": f"Token {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

Base.metadata.create_all(bind=engine)

# ---------------------------
# Prediction Endpoint
# ---------------------------

@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()




@app.post("/predict")
def predict_churn(customer: CustomerRequest):
    payload = [customer.dict()]  # API v2 expects RAW ARRAY

    try:
        response = requests.post(
            DR_URL,
            headers=HEADERS,
            json=payload,
            timeout=10
        )
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )

    
    return response.json()


@app.post("/save-prediction")
def save_prediction(payload: PredictionRequest, db: Session = Depends(get_db)):
    for item in payload.data:
        prediction = Prediction(
            row_id=item.rowId,
            prediction=item.prediction,
            prediction_threshold=item.predictionThreshold,
            deployment_approval_status=item.deploymentApprovalStatus,
        )

        for pv in item.predictionValues:
            prediction_value = PredictionValue(
                label=pv.label,
                value=pv.value
            )
            prediction.prediction_values.append(prediction_value)

        db.add(prediction)

    db.commit()
    return {"message": "Prediction data saved successfully"}
