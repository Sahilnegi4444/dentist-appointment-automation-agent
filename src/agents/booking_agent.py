from db.orm_crud import get_available_slots, book_slot
from logger.custom_logger import get_logger

log = get_logger(__name__)

def booking_agent(state:dict):
    