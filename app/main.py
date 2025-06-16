# app/main.py

from fastapi import FastAPI, HTTPException
from typing import List

from app.db import SessionLocal
from app.models import TrackerRecord
from app.schemas import TrackerRecordCreate, TrackerRecordRead

# Create FastAPI app instance
app = FastAPI()


# GET all records
@app.get("/records", response_model=List[TrackerRecordRead])
def get_records():
    db = SessionLocal()
    try:
        records = db.query(TrackerRecord).all()
        return records
    finally:
        db.close()


# POST a new record
@app.post("/records", response_model=TrackerRecordRead)
def create_record(record: TrackerRecordCreate):
    db = SessionLocal()
    try:
        db_record = TrackerRecord(**record.dict())
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        return db_record
    finally:
        db.close()
