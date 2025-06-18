# Import SQLAlchemy column types
from sqlalchemy import Column, Integer, String, Date

# Import the declarative Base made in db.py
from .db import Base

# Define TrackerRecord model (maps to tracker_data table in Postgres)
class TrackerRecord(Base):
    __tablename__ = "tracker_data"  # Table name in DB

    id = Column(Integer, primary_key=True, index=True)  # Auto-increment ID
    user_id = Column(Integer, nullable=False)           
    date = Column(Date, nullable=False)                 
    steps = Column(Integer, nullable=False)          
    heart_rate_avg = Column(Integer, nullable=True)
    calories_burned = Column(Integer, nullable=True)
    workout_type = Column(String, nullable=True)
                 
