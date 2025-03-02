#!/usr/bin/env python
import sys
import warnings
import logging
from idea_generator.crew import IdeaGenerator
import os

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def setup_logger() -> logging.Logger:
    """
    Configure the main logger.
    """
    logger = logging.getLogger("main")
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG if os.getenv("DEBUG") == "True" else logging.INFO)
    logger.propagate = False
    return logger

# Configure the main logger
logger = setup_logger()

def run():
    """
    Execute the script.
    """
    logger.debug("Starting idea generation process...")
    try:
        logger.debug("Initializing idea generator...")
        idea_generator = IdeaGenerator()
        os.makedirs("conversations", exist_ok=True)
        logger.debug("Starting idea generator...")
        idea_generator.crew().kickoff()
        logger.debug("Idea generation completed successfully!")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise
    logger.debug("Process completed successfully!")

if __name__ == "__main__":
    run()
