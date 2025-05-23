import logging
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logs_path = os.path.join(BASE_DIR, "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"))

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"))

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logging.info("Test log entry: Logging setup is working!")

print(f"Log file created at: {LOG_FILE_PATH}")
