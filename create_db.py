# Import Base and Engine from db.py
from app.db import Base, engine

# Import model so Base knows what to create
from app.models import TrackerRecord

# SQLAlchemy to create tables in the db if they don't exist yet
Base.metadata.create_all(bind=engine)

print("Table created!") 
