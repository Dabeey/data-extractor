# Sports Data Extractor

A Python tool for fetching, parsing, and saving live NBA and NFL scoreboard data from ESPN's public API. Export game details to CSV and JSON for analysis, dashboards, or automation.

## Features

- Fetches NBA and NFL scoreboard data from ESPN
- Extracts game details: teams, scores, venue, status, and date
- Saves results to both CSV and JSON formats
- Simple, extensible codebase for other sports or endpoints

## Installation

Clone the repo:
```sh
git clone https://github.com/yourusername/sports-data-extractor.git
cd sports-data-extractor
```

Install dependencies:
```sh
pip install requests
```

## Usage

Run the script to fetch and save NBA and NFL scoreboard data:
```sh
python main.py
```

- Output files: `nba_scoreboard.csv`, `nba_scoreboard.json`, `nfl_scoreboard.csv`, `nfl_scoreboard.json`
- Data includes game ID, date, status, venue, home/away teams, and scores

## Example Output

```
Fetching NBA...
[SUCCESS] JSON retrieved from ESPN API
[SAVED] nba_scoreboard.json
[SAVED] nba_scoreboard.csv
Fetching NFL...
[SUCCESS] JSON retrieved from ESPN API
[SAVED] nfl_scoreboard.json
[SAVED] nfl_scoreboard.csv
✅ Done.
```

## Extending

- Add more sports by updating API endpoints and labels in your script
- Integrate with dashboards, analytics, or notification systems

## License

MIT License — free to use and modify for personal or commercial