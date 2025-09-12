import requests
import json
from typing import Optional



url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"


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


""" 
Store the list from fetch data function to a variable for further parsing
"""
data = fetch_data(url) 



def extract_event(events: list | None) -> list:  
    """
    Extract events from the ESBN website with error handling.

    ARGS:
        events: A list that contains dictioaries of the event key in the data.

    OUTPUT:
        Returns a list containing the events of NBA.

    """
    if events is None:
        events = []
        logging.warning('Events is empty')
    
    extracted = []

    for i, event in enumerate(events, start=1): 
        try:
            event_id = event.get("id", "N/A")
            date = event.get("date", "N/A")

            competitions = event.get("competitions", [])

            if not competitions:
                logging.warning('Competition has a potential error')
                continue

            venue = competitions[0].get("venue", {}).get("fullName", "Unknown Venue")

            competitors = competitions[0].get("competitors", []) if competitions else []
            teams = [competitor.get("team", {}).get("shortDisplayName", "Unknown") for competitor in competitors]

            if len(teams) < 2:
                logging.warning(f"Skipping Event {i}: missing team data")
                continue

            upcoming_event = (
                f'Event {i} ID: {event_id} | Date: {date} | '
                f'Venue: {venue} | Teams: {teams[0]} vs {teams[1]}'
            )
            logging.info(upcoming_event)

            extracted.append({
                'id': event_id,
                'date': date,
                'venue': venue,
                'teams': f'{teams[0]} vs {teams[1]}',
            })

        except Exception as e:
            logging.error(f'An error occurred while extracting event {i}: {e}') 

    return extracted


extracted_list = extract_event(events=data.get('events',[]))


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

save_to_json(extracted_list)