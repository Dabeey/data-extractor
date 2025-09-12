import requests
from utils.logger import logging

def fetch_data(url: str, timeout: float = 10) -> list[dict]:
    """ 
    Fetch data from ESPN website.

    ARGS:
        url (str): The URL of the website.
        timeout (float): 10 seconds before timeout.

    OUTPUT:
        Returns a list of dictionary in JSON format.

    """
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        logging.info(f'Successfully fetched data from {url}')
        return response.json()
        
    except requests.RequestException as e:
        logging.error(f'An error occurred while fetching data: {e}')

