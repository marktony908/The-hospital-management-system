# models/__init__.py

from database import Base  # Ensure Base is imported from database.py
from .models import Doctor, Patient, Admission  # Import your models

__all__ = ['Doctor', 'Patient', 'Admission', 'Base']
