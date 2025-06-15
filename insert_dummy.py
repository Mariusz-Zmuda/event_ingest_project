# Import SessionLocal (DB connection) and model
from app.db import SessionLocal
from app.models import TrackerRecord
from datetime import date

# Open a new DB session
db = SessionLocal()

# Create a dummy TrackerRecord object (1 row)
record = TrackerRecord(
    user_id=4001,
    date=date.today(),
    steps=12345,
    heart_rate_avg=75,
    calories_burned=500,
    workout_type="Cardio"
)

# Add the new record to the session
db.add(record)

# Commit the transaction - this INSERTS the row into the database
db.commit()

# Close the session to free up resources
db.close()

print("Inserted dummy row!")
