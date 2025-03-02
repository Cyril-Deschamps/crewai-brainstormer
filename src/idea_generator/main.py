#!/usr/bin/env python
import os
import sys
import warnings
import logging
from dotenv import load_dotenv
from idea_generator.crew import IdeaGenerator

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

load_dotenv()

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
    logger.setLevel(logging.INFO)
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
        api_key = os.environ.get("AI_API_KEY")
        if not api_key:
            raise ValueError("No API key found in environment variables (AI_API_KEY)")

        model = os.environ.get("AI_MODEL")
        base_url = os.environ.get("AI_BASE_URL")
        
        idea_generator = IdeaGenerator(
            model=model,
            api_key=api_key,
            base_url=base_url,
        )
        logger.debug("Starting idea generator...")
        result = idea_generator.crew().kickoff()
        logger.debug("Idea generation completed successfully!")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise
    logger.debug("Process completed successfully!")

if __name__ == "__main__":
    run()
