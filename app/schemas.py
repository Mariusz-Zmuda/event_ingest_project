# app/schemas.py

from pydantic import BaseModel
from datetime import date
from typing import Optional

class TrackerRecordBase(BaseModel):
    user_id: int
    date: date
    steps: int
    heart_rate_avg: Optional[int] = None
    calories_burned: Optional[int] = None
    workout_type: Optional[str] = None

class TrackerRecordCreate(TrackerRecordBase):
    pass  # identical for now

class TrackerRecordRead(TrackerRecordBase):
    id: int  # include DB id for reading

    class Config:
        orm_mode = True
