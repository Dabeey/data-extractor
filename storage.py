import json
from typing import Optional
from utils.logger import logging
import csv

def save_to_json(data: Optional[list], filename: str = 'events.json'):
    """ 
    Save extracted data to JSON. 

    Args:
        data (Optional[list]) : List containing extracted events data.
        filename (str) : File name to save the data in. Default is 'events.json'

    Return:
        None

    Side Effect:
        Creates or overwrites a JSON file on disk
    """
    if data is None:
        data = []
        logging.warning('Data does not exist. Check empty list and try again')
        
    with open(filename, 'w', newline='') as file:
        json.dump(data, file, indent=2)


def save_to_csv(data: Optional[list], filename='events.csv'):
    with open(filename,'w',newline='') as file:
        fieldnames = ['id', 'date', 'venue','teams']
        writer = csv.DictWriter(data,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)