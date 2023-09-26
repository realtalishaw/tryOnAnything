import logging

class Logger:
    def __init__(self, log_file="application.log"):
        logging.basicConfig(filename=log_file, level=logging.DEBUG)
    
    def log_info(self, message):
        logging.info(message)
        print(f"INFO: {message}")

    def log_error(self, message):
        logging.error(message)
        print(f"ERROR: {message}")

    def log_debug(self, message):
        logging.debug(message)
        print(f"DEBUG: {message}")
