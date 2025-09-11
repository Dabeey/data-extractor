import requests
import json
import logging

'''
Setting up logging in dev mode to catch everything in the console
'''
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s - %(message)s'
)



# Step 1: ESPN NBA Scoreboard API
url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"


''''''
def fetch_data(url: str, timeout: float = 10) -> list[dict]:
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        logging.info(f'Successfully fetched data from {url}')
        return response.json()
        
    except requests.RequestException as e:
        logging.error(f'An erroe occurred while fetchind data: {e}')

    except requests.exceptions as e:
        logging.error(f'Error occurred due to: {e}')

    
data = fetch_data(url)


def extract_event(events: list = data.get("events", [])) -> list:
    try:
        if not isinstance(events,list):
            logging.warning(f'Data not fetched correctly as JSON: {type(events)}')

        extracted = []
        i = 1

        for event in events: 
            event_id = event.get("id", "N/A")
            date = event.get("date", "N/A")

            competitions = event.get("competitions", [])

            if not competitions:
                logging.warning('Competition has a potential error')
                continue

            venue = competitions[0].get("venue", {}).get("fullName", "Unknown Venue") if competitions else "Unknown Venue"

            competitors = competitions[0].get("competitors", []) if competitions else []

            if not competitors:
                logging.warning('Skipping Competitors.')
                continue

            teams = [competitor.get("team", {}).get("shortDisplayName", "Unknown") for competitor in competitors]

            if len(teams) >= 2:
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
            else:
                logging.warning(f"Skipping Event {i}: missing team data")
                continue

            i += 1
        return extracted

    except Exception as e:
        logging.error(f'An error occurred while extracting event: {e}') 
>>>>>>> f8ac0ec (Refactor: Enhance error handling and logging in fetch_data and extract_event functions)





extracted_list = extract_event()
print(extracted_list)
