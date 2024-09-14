#!"C:\users\gr80t\.pyenv\pyenv-win\versions\3.11.0"

# Copyright 2024, Josh Grady, All rights reserved. 

import argparse
import requests
from datetime import datetime
import datetime

# Define argparse
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--range", help="The time range for playlist to generate")
args = parser.parse_args()

# Time ranges would be 1 month, 3 months, 6 months, 1 year, YTD, and All time
today = datetime.date.today()
one_month_ago = today - datetime.timedelta(days=30)
three_months_ago = today - datetime.timedelta(days=90)
six_months_ago = today - datetime.timedelta(days=180)
one_year_ago = today - datetime.timedelta(days=365)
# year_to_date = Jan 1 of year - current date
print(str(today))
print(str(one_month_ago))
# Auth stuff for spotify api

# Get song data for time period of current date-range to current date 

# Get 50 highest played tracks for period in list

# Define playlist from song list

# Create/Export the playlist or print out (or both)
