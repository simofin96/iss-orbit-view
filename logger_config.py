"""This module configures the logger for the project."""
import logging

def configure_logger():
    """Configures the logger for the entire project."""
    logger = logging.getLogger()  # Get the main logger
    logger.setLevel(logging.INFO)  # Set the global log level to INFO (INFO and above)

    # Create a log format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Create the handler to display logs in the console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)

    return logger
