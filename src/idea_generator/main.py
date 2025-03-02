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
    Configure le logger principal.
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

# Configuration du logger principal
logger = setup_logger()

def run():
    """
    Exécute le script.
    """
    logger.info("Démarrage du processus de génération d'idées...")
    try:
        api_key = os.environ.get("AI_API_KEY")
        if not api_key:
            raise ValueError("Aucune clé API trouvée dans les variables d'environnement (AI_API_KEY)")

        model = os.environ.get("AI_MODEL")
        base_url = os.environ.get("AI_BASE_URL")
        
        idea_generator = IdeaGenerator(
            model=model,
            api_key=api_key,
            base_url=base_url,
        )
        logger.info("Démarrage du générateur d'idées...")
        result = idea_generator.crew().kickoff()
        logger.info("Génération d'idées terminée avec succès!")
    except Exception as e:
        logger.error(f"Une erreur est survenue: {str(e)}")
        raise
    logger.info("Processus terminé avec succès!")
