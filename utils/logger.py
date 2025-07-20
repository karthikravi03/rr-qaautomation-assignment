import logging


def get_logger():
    logger = logging.getLogger("test_logger")
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger
