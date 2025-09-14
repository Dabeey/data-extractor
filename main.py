from utils.logger import logging
from fetcher import fetch_data
from parser import extract_event
from storage import save_to_json
import argparse

if __name__=='__main__':

    url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"

    data = fetch_data(url) 
    extracted_list = extract_event(events=data.get('events',[]))
    save_to_json(extracted_list)


    parser = argparse.ArgumentParser()
    parser.add_argument('--storage',choices=['json','csv'], default='json')
    args = parser.parse_args()

    if args.storage == 'json':
        save_to_json(data)
    else:
        save_to_