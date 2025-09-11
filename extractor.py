import requests
import json

# Step 1: ESPN NBA Scoreboard API
url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"

def fetch_data(url):
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}")
        return None

data = fetch_data(url)


def extract_event(events: list = data.get("events", [])) -> list: 
    extracted = []

    i = 1
    for event in events: 
        try:
            event_id = event.get("id", "N/A")
            date = event.get("date", "N/A")

            # competitions is always a list, but still defensive
            competitions = event.get("competitions", [])
            if not competitions:
                print(f"Skipping Event {i}: no competitions data")
                continue

            venue = competitions[0].get("venue", {}).get("fullName", "Unknown Venue")
            competitors = competitions[0].get("competitors", [])
            if len(competitors) < 2:
                print(f"Skipping Event {i}: missing competitors")
                continue

            teams = [competitor.get("team", {}).get("shortDisplayName", "Unknown") 
                     for competitor in competitors]

            upcoming_event = (
                f'Event {i} ID: {event_id} | Date: {date} | '
                f'Venue: {venue} | Teams: {teams[0]} vs {teams[1]}'
            )
            print(upcoming_event)

            extracted.append({
                'id': event_id,
                'date': date,
                'venue': venue,
                'teams': f'{teams[0]} vs {teams[1]}',
            })

        except Exception as e:
            print(f"⚠️ Skipping Event {i} due to error: {e}")

        i += 1

    return extracted


extracted_list = extract_event()
print(extracted_list)
