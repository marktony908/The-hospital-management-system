# seed.py

from database import Session, engine, Base
from models import Doctor, Patient, Admission

# Create the tables
Base.metadata.create_all(bind=engine)

# Example seed data
session = Session()

doctor1 = Doctor(name="Dr. Smith")
patient1 = Patient(name="John Doe")
admission1 = Admission(patient=patient1, doctor=doctor1)

session.add(doctor1)
session.add(patient1)
session.add(admission1)
session.commit()

session.close()
