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

class MockResponse:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code != 200:
            raise Exception("Mock HTTP error")

@pytest.fixture
def web_scraper(mocker):
    """Returns an instance of WebScraper with a mocked Gemini model."""
    mocker.patch('config.GEMINI_API_KEY', "test_api_key")
    mocker.patch('google.generativeai.GenerativeModel', return_value=MockGeminiModel())
    mock_response = MockResponse('<html><body><div id="result-stats">About 1,230,000 results</div></body></html>')
    mocker.patch('requests.get', return_value=mock_response)
    return WebScraper()

def test_search_and_summarize(web_scraper):
    """Test the search_and_summarize method."""
    result = web_scraper.search_and_summarize("test idea")
    assert "summary" in result
    assert "score" in result
    assert result["summary"] == "Summary: This is a test summary.\nScore: 0.8"
    assert result["score"] == 0.8
    assert "regulatory_urgency" in result
    assert "trend_acceleration_factor" in result
    assert "market_delta" in result
    assert "web_signal" in result
    assert result["regulatory_urgency"] > 0
    assert result["trend_acceleration_factor"] > 0
    assert result["market_delta"] > 0
