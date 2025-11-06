"""
Web Scraper Module - Uses Gemini to get real-time web context.
"""

import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import config

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
            return {"summary": "Gemini API key not configured.", "score": 0.5}

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

            return {"summary": summary, "score": score}
        except Exception as e:
            print(f"Error during web scraping: {e}")
            return {"summary": "Could not perform web search.", "score": 0.5}
