import logging
import os

def get_logger():
    logger = logging.getLogger("pipeline")
    logger.setLevel(logging.DEBUG)

    # avoids duplicate handlers on repeated imports
    if logger.handlers:
        return logger

    file_handler = logging.FileHandler("logs/pipeline.log")
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger