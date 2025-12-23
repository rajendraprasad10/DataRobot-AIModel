from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    row_id = Column(Integer, index=True)
    prediction = Column(Integer)
    prediction_threshold = Column(Float)
    deployment_approval_status = Column(String)

    prediction_values = relationship(
        "PredictionValue",
        back_populates="prediction",
        cascade="all, delete"
    )


class PredictionValue(Base):
    __tablename__ = "prediction_values"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(Integer)
    value = Column(Float)

    prediction_id = Column(Integer, ForeignKey("predictions.id"))
    prediction = relationship("Prediction", back_populates="prediction_values")

