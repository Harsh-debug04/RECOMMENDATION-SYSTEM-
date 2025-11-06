"""
Unit tests for the WebScraper module.
"""

import pytest
from core.web_scraper import WebScraper

class MockGeminiResponse:
    def __init__(self, text):
        self.text = text

class MockGeminiModel:
    def generate_content(self, *args, **kwargs):
        return MockGeminiResponse("Summary: This is a test summary.\nScore: 0.8")

@pytest.fixture
def web_scraper(mocker):
    """Returns an instance of WebScraper with a mocked Gemini model."""
    mocker.patch('google.generativeai.GenerativeModel', return_value=MockGeminiModel())
    return WebScraper()

def test_search_and_summarize(web_scraper):
    """Test the search_and_summarize method."""
    result = web_scraper.search_and_summarize("test idea")
    assert "summary" in result
    assert "score" in result
    assert result["summary"] == "Summary: This is a test summary.\nScore: 0.8"
    assert result["score"] == 0.8
