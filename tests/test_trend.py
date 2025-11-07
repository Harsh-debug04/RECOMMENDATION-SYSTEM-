"""
Unit tests for the MarketTrendAnalyzer module.
"""

import pytest
from core.trend import MarketTrendAnalyzer

@pytest.fixture
def trend_analyzer():
    """Returns an instance of MarketTrendAnalyzer."""
    return MarketTrendAnalyzer()

def test_analyze_trend_high(trend_analyzer):
    """Test the trend analysis for a high-trend topic."""
    text = "This idea is about AI and machine learning, which are very popular topics."
    tags = ["AI", "machine learning"]
    trend_score = trend_analyzer.analyze_trend(text, tags)
    assert trend_score > 0.7

def test_analyze_trend_low(trend_analyzer):
    """Test the trend analysis for a low-trend topic."""
    text = "This idea is about a niche topic with very little interest."
    tags = ["niche", "obscure"]
    trend_score = trend_analyzer.analyze_trend(text, tags)
    assert trend_score < 0.3
