from sqlalchemy import Column, Integer, String, Boolean, DateTime
from db.ingest_db import Base

class Slot(Base):
    """
    ORM model representing a doctor's time slot.

    Each row = one appointment slot.
    """

    __tablename__ = "slots"

    id = Column(Integer, primary_key=True, index=True)

    # Date + Time appointment
    date_slot = Column(DateTime, nullable=False)

    # Doctor name
    doc_name = Column(String(100))

    # Doctor's Specialisation
    specialisation = Column(String(100))

    # Slot free or booked
    is_available = Column(bool, default=True)

    # Patient assigned(null if not booked)
    patient_to_attend = Column(Integer, nullable=True)