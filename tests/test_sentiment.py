"""
Unit tests for the SentimentAnalyzer module.
"""

import pytest
from core.sentiment import SentimentAnalyzer

@pytest.fixture
def sentiment_analyzer():
    """Returns an instance of SentimentAnalyzer."""
    return SentimentAnalyzer()

def test_analyze_positive(sentiment_analyzer):
    """Test the sentiment analysis for a positive text."""
    text = "This is a wonderful and amazing idea. I love it!"
    sentiment = sentiment_analyzer.analyze(text)
    assert sentiment > 0.5

def test_analyze_negative(sentiment_analyzer):
    """Test the sentiment analysis for a negative text."""
    text = "This is a terrible and awful idea. I hate it."
    sentiment = sentiment_analyzer.analyze(text)
    assert sentiment < -0.5

def test_analyze_neutral(sentiment_analyzer):
    """Test the sentiment analysis for a neutral text."""
    text = "This is an idea."
    sentiment = sentiment_analyzer.analyze(text)
    assert -0.1 < sentiment < 0.1
