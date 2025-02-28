#!/usr/bin/env python
import sys
import warnings
import logging

from datetime import datetime
from dotenv import load_dotenv
from idea_generator.tools.generator import IdeaGeneratorTools
from idea_generator.crew import IdeaGenerator

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def main():
    """Point d'entrée principal du générateur d'idées"""
    
    # Chargement des variables d'environnement
    load_dotenv()
    
    try:
        # Initialisation des outils
        tools = IdeaGeneratorTools()
        
        # Création de l'équipe avec les outils
        idea_generator = IdeaGenerator()
        
        logger.info("Démarrage du processus de génération d'idées...")
        
        # Lancement du pipeline
        result = idea_generator.crew.kickoff()
        
        logger.info("Processus terminé avec succès!")
        logger.info("Les résultats ont été sauvegardés dans 'idea_generation_report.md'")
        
        return result
        
    except Exception as e:
        logger.error(f"Une erreur est survenue : {str(e)}")
        raise

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    try:
        IdeaGenerator().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        IdeaGenerator().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        IdeaGenerator().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        IdeaGenerator().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    main()
