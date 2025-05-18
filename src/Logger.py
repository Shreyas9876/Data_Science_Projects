import logging
import os
from datetime import datetime

# Setting up logs directory and log file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logs_path = os.path.join(BASE_DIR, "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Setting up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File Handler
file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"))

# Console Handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"))

# Adding Handlers
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

if __name__ == "__main__":
    logging.info("Logging has started")
