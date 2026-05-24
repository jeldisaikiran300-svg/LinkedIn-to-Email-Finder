import time
import logging
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)

class LinkedInScraper:
    def __init__(self, li_at_cookie: str = None):
        """
        Initializes the Selenium WebDriver.
        Pass the `li_at` cookie to bypass the LinkedIn login wall.
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Adding a common user agent to avoid basic blocks
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.li_at_cookie = li_at_cookie

        if self.li_at_cookie:
            self._authenticate()

    def _authenticate(self):
        """Sets the LinkedIn authentication cookie."""
        logger.info("Setting LinkedIn authentication cookie...")
        self.driver.get("https://www.linkedin.com")
        self.driver.add_cookie({
            "name": "li_at",
            "value": self.li_at_cookie,
            "domain": ".linkedin.com"
        })
        self.driver.refresh()
        time.sleep(2)

    def scrape_profile(self, linkedin_url: str):
        """
        Visits a LinkedIn profile and extracts basic details (Name, Headline).
        """
        logger.info(f"Scraping profile: {linkedin_url}")
        try:
            self.driver.get(linkedin_url)
            # Wait for content to load
            time.sleep(4) 
            
            # Check if we hit a login wall
            if "linkedin.com/signup" in self.driver.current_url or "linkedin.com/login" in self.driver.current_url:
                logger.error("Hit LinkedIn login wall. The li_at cookie might be expired or missing.")
                return None
            
            # Extract page source and parse with BeautifulSoup
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            
            # Name extraction (LinkedIn DOM changes frequently, this is a common current structure)
            name_tag = soup.find('h1', class_='text-heading-xlarge')
            name = name_tag.text.strip() if name_tag else "Unknown Name"
            
            # Headline extraction
            headline_tag = soup.find('div', class_='text-body-medium')
            headline = headline_tag.text.strip() if headline_tag else "Unknown Headline"

            return {
                "scraped_name": name,
                "scraped_headline": headline
            }
        
        except Exception as e:
            logger.error(f"Failed to scrape {linkedin_url}: {str(e)}")
            return None

    def close(self):
        self.driver.quit()
