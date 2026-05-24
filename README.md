# LinkedIn to Email Finder

This project takes a list of LinkedIn profile URLs and finds their associated verified emails and profile data (Name, Title, Company) using the Apollo.io API.

It also includes an optional LinkedIn scraper using Selenium, demonstrating how you could extract on-page profile data to augment the Apollo match if needed. However, since Apollo's match endpoint handles LinkedIn URLs natively, manual scraping is generally not required (and saves you from dealing with LinkedIn's aggressive anti-bot mechanisms).

## Features

-Apollo API Integration: Search for a B2B contact's email directly by supplying their LinkedIn URL.
-Selenium LinkedIn Scraper (Optional): Extract Name and Headline directly from the LinkedIn DOM. Bypasses the login wall using a li_at session cookie.
-Batch Processing: Reads from an input.csv file and writes all enriched data to an output.csv.

##Prerequisites

Python 3.8+
Google Chrome (if using the Selenium Scraper)
An Apollo.io account and API key.
Setup Instructions
Install Dependencies

Bash

pip install -r requirements.txt
Configure Environment Variables
Rename .env.example to .env:

Bash

cp .env.example .env
Add your Apollo API Key to .env. (Found in Apollo > Settings > Integrations > API).

(Optional) If you plan to use the manual Selenium scraper (linkedin_scraper.py), you need to supply your LinkedIn session cookie (li_at). You can find this in your browser's Developer Tools -> Application -> Cookies -> www.linkedin.com.

Prepare the Input Data
Add your target LinkedIn URLs to the input.csv file under the linkedin_url column.

Usage
Simply run the main script:

Bash

python main.py
How it works
Reads input.csv: Iterates through each LinkedIn profile URL.
Calls Apollo API: Hits POST /api/v1/people/match with the URL.
Saves Data: Exports the resulting match (Name, Title, Company, Email) to output.csv.
Note on LinkedIn Scraping
Scraping LinkedIn directly is notoriously difficult due to their strict anti-bot systems. Using automated headless browsers often leads to IP bans or account restrictions.

This project defaults to passing the URL directly to Apollo.io, which maintains its own massive database and handles the heavy lifting of matching the profile URL to an identity and email address. If you wish to enable the manual profile scraper, uncomment the scraper related lines in main.py. Ensure you have a valid li_at cookie in your .env file!
