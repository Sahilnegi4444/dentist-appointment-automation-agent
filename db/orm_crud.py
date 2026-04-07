from db.ingest_db import SessionLocal
from models.slot import Slot

def get_available_slots(date:str) ->list:
    """
    Fetch the available slot for the given data
    """

    session = SessionLocal()

    try:
        slots = (
            session.query(Slot)
            .filter(Slot.date_slot.startswith(date))
            .filter(Slot.is_available == True)
            .limit(10)
            .all()
        )

        return slots
    
    finally:
        session.close()

def book_slot(slot_id: int, patient_id: int) -> bool:
    """
    Book a slot by updating availability
    """

    session = SessionLocal()

    try:
        slot = session.query(Slot).filter(Slot.id == slot_id).first()

        # if slot not found or already booked
        if not slot or not slot.is_available:
            return False

        # Update Slot
        slot.is_available = False
        slot.patient_to_attend = patient_id

        return True

    except Exception:
        session.rollback()
        return False
    
    finally:
        session.close()


