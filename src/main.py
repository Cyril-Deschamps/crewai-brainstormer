#!/usr/bin/env python
import sys
import warnings
import logging
import os
from CrewAIBrainstormer import CrewAIBrainstormer

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
    logger.debug("Starting crewai brainstorming process...")
    try:
        logger.debug("Initializing crewai brainstormer...")
        idea_generator = CrewAIBrainstormer()
        os.makedirs("conversations", exist_ok=True)
        logger.debug("Starting crewai brainstormer...")
        idea_generator.crew().kickoff()
        logger.debug("CrewAI brainstorming completed successfully!")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise
    logger.debug("Process completed successfully!")

def runAll():
    """
    Run all types of crew - Placeholder for potential future expansion
    """
    run()

if __name__ == "__main__":
    run()
