# LinkedIn to Email Finder

Find verified emails and professional data (Name, Title, Company) from LinkedIn profile URLs using the Apollo.io API. Batch process CSV files and get enriched results in seconds.

> **Note**: This project uses Apollo’s native `match` endpoint – no manual scraping required. An optional Selenium scraper is included but disabled by default (due to LinkedIn’s aggressive anti‑bot policies).

## Features

- **Apollo API Integration** – Match a LinkedIn URL to a contact and retrieve email, name, title, and company.
- **Batch Processing** – Read `input.csv` with LinkedIn URLs, output enriched data to `output.csv`.
- **Optional Selenium Scraper** – Extract name and headline directly from LinkedIn DOM (needs `li_at` cookie).
- **Environment variable support** – Keep your API keys secure.

## Prerequisites

- Python 3.8 or higher
- Google Chrome (only if using the Selenium scraper)
- An [Apollo.io](https://www.apollo.io/) account with an **API key** (free tier available)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/linkedin-to-email-finder.git
cd linkedin-to-email-finder
