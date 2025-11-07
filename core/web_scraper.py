"""
Web Scraper Module - Uses Gemini to get real-time web context.
"""

import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import config
import requests
from bs4 import BeautifulSoup

class WebScraper:
    """
    A class to scrape and summarize web content using the Gemini API.
    """

    def __init__(self):
        """
        Initializes the WebScraper, configuring it with the Gemini API key.
        """
        if config.GEMINI_API_KEY:
            genai.configure(api_key=config.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-pro')
        else:
            self.model = None

    def search_and_summarize(self, idea_title: str) -> dict:
        """
        Searches the web for a given idea title and returns a summary of the findings.

        Args:
            idea_title: The title of the idea to search for.

        Returns:
            A dictionary containing the summary and a score.
        """
        if not self.model:
            return {"summary": "Gemini API key not configured.", "score": 0.5, "regulatory_urgency": 0.0, "trend_acceleration_factor": 0.0, "market_delta": 0.0, "web_signal": 0.5}

        try:
            prompt = f"Search the web for the startup idea '{idea_title}'. Summarize the competitive landscape, market potential, and any existing similar solutions. Provide a score from 0 to 1 indicating the idea's novelty and potential for success, where 1 is highly novel and promising."
            response = self.model.generate_content(
                prompt,
                safety_settings={
                    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                }
            )

            # Extract summary and score from the response
            summary = response.text
            # A simple way to extract a score from the text
            score_line = [line for line in summary.split('\n') if 'score' in line.lower()]
            if score_line:
                # Extract the first number from the score line
                score = float([s for s in score_line[0].split() if s.isdigit() or s.replace('.', '', 1).isdigit()][0])
            else:
                score = 0.5  # Default score

            # Placeholder for structured signal acquisition
            regulatory_urgency = self._scrape_regulatory_bulletins(idea_title)
            trend_acceleration_factor = self._scrape_news_feeds(idea_title)
            market_delta = self._scrape_market_data(idea_title)

            # Combine signals into a composite score
            web_signal = 0.4 * score + 0.3 * regulatory_urgency + 0.2 * trend_acceleration_factor + 0.1 * market_delta

            return {"summary": summary, "score": score, "regulatory_urgency": regulatory_urgency, "trend_acceleration_factor": trend_acceleration_factor, "market_delta": market_delta, "web_signal": web_signal}
        except Exception as e:
            print(f"Error during web scraping: {e}")
            return {"summary": "Could not perform web search.", "score": 0.5, "regulatory_urgency": 0.0, "trend_acceleration_factor": 0.0, "market_delta": 0.0, "web_signal": 0.5}

    def _scrape_regulatory_bulletins(self, idea_title: str) -> float:
        """
        Scrapes Google Search for regulatory bulletins.
        """
        try:
            query = f'"{idea_title}" regulatory bulletins'
            response = requests.get(f"https://www.google.com/search?q={query}")
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            # A simple metric: count the number of search results
            result_stats = soup.find(id="result-stats")
            if result_stats:
                # Extract the number of results
                import re
                results_text = result_stats.text
                results_count = int(re.search(r'(\d[\d,]*)\sresults', results_text).group(1).replace(',', ''))
                # Normalize the count to a score
                return min(1.0, results_count / 100000.0)
            return 0.1
        except Exception as e:
            print(f"Error scraping regulatory bulletins: {e}")
            return 0.5

    def _scrape_news_feeds(self, idea_title: str) -> float:
        """
        Scrapes Google Search for news feeds.
        """
        try:
            query = f'"{idea_title}" news'
            response = requests.get(f"https://www.google.com/search?q={query}")
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            # A simple metric: count the number of search results
            result_stats = soup.find(id="result-stats")
            if result_stats:
                # Extract the number of results
                import re
                results_text = result_stats.text
                results_count = int(re.search(r'(\d[\d,]*)\sresults', results_text).group(1).replace(',', ''))
                # Normalize the count to a score
                return min(1.0, results_count / 1000000.0)
            return 0.1
        except Exception as e:
            print(f"Error scraping news feeds: {e}")
            return 0.5

    def _scrape_market_data(self, idea_title: str) -> float:
        """
        Scrapes Google Search for market data.
        """
        try:
            query = f'"{idea_title}" market size'
            response = requests.get(f"https://www.google.com/search?q={query}")
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            # A simple metric: count the number of search results
            result_stats = soup.find(id="result-stats")
            if result_stats:
                # Extract the number of results
                import re
                results_text = result_stats.text
                results_count = int(re.search(r'(\d[\d,]*)\sresults', results_text).group(1).replace(',', ''))
                # Normalize the count to a score
                return min(1.0, results_count / 100000.0)
            return 0.1
        except Exception as e:
            print(f"Error scraping market data: {e}")
            return 0.5
