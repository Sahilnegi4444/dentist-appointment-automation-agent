import pandas as pd
import os
from pathlib import Path
from sqlalchemy import create_engine
from dotenv import load_dotenv
from logger.custom_logger import get_logger
from exception_handling.custom_exception import CustomException

log = get_logger(__name__)

load_dotenv()

try:
    # db connection
    DATABASE_URL = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DATABASE')}"

    engine = create_engine(DATABASE_URL)

    # read_csv
    BASE_DIR = Path(__file__).resolve().parent.parent
    file_path = BASE_DIR / "data" / "doctor_availability.csv"

    df = pd.read_csv(file_path)

    log.info("Started ingestion")

    # push to mysql
    df.to_sql("slots", con=engine, if_exists="replace", index=False)

    log.info("Ingested to DB successfully")


except Exception as e:
    raise CustomException("Failed to ingest", e)


