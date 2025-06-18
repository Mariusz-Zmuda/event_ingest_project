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

# PUT update a record by ID
@app.put("/records/{record_id}", response_model=TrackerRecordRead)
def update_record(record_id: int, updated_record: TrackerRecordCreate):
    db = SessionLocal()
    try:
        db_record = db.query(TrackerRecord).filter(TrackerRecord.id == record_id).first()
        if db_record is None:
            raise HTTPException(status_code=404, detail="Record not found")

        # Update fields one by one
        for field, value in updated_record.dict().items():
            setattr(db_record, field, value)

        db.commit()
        db.refresh(db_record)
        return db_record
    finally:
        db.close()

# DELETE a record by ID
@app.delete("/records/{record_id}")
def delete_record(record_id: int):
    db = SessionLocal()
    try:
        db_record = db.query(TrackerRecord).filter(TrackerRecord.id == record_id).first()
        if db_record is None:
            raise HTTPException(status_code=404, detail="Record not found")

        db.delete(db_record)
        db.commit()
        return {"detail": f"Record {record_id} deleted"}
    finally:
        db.close()
