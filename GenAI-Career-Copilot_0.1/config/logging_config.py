import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "career_copilot.log")


def setup_logging():
    os.makedirs(LOG_DIR, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()  # also prints to console, same as your current prints
        ]
    )