from utils.logger import logging
from fetcher import fetch_data
from parser import extract_event
from storage import save_to_json


if __name__=='__main__':
    
    url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"

    data = fetch_data(url) 
    extracted_list = extract_event(events=data.get('events',[]))
    save_to_json(extracted_list)


    