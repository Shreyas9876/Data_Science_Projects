import logging
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logs_path = os.path.join(BASE_DIR, "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Create logger function for modules
def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():  # Prevent adding multiple handlers in interactive environments
        file_handler = logging.FileHandler(LOG_FILE_PATH)
        stream_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s [%(name)s:%(filename)s:%(lineno)d - %(funcName)s()] - %(message)s"
        )
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger

if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("Test log entry: Logging setup is working!")
    print(f"Log file created at: {LOG_FILE_PATH}")
