import logging


"""
Setting up logging in dev mode to catch everything properlly in the console.
"""
logging.basicConfig(
    filename='projects.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
