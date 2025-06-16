import pandas as pd
from app.db import SessionLocal
from app.models import TrackerRecord
from datetime import datetime

# Load CSV
df = pd.read_csv("data/Fitness_Tracker_Data.csv")

# Open DB session
db = SessionLocal()

# Iterate rows and insert
for index, row in df.iterrows():
    record = TrackerRecord(
        user_id = int(row["User_ID"]),
        date = pd.to_datetime(row["Date"]).date(),
        steps = int(row["Steps"]),
        heart_rate_avg = int(row["Heart_Rate_avg"]) if not pd.isna(row["Heart_Rate_avg"]) else None,
        calories_burned = int(row["Calories_Burned"]) if not pd.isna(row["Calories_Burned"]) else None,
        workout_type = row["Workout_Type"] if not pd.isna(row["Workout_Type"]) else None
    )
    db.add(record)

db.commit()

# Close the session
db.close()

print("CSV data inserted successfully!")
