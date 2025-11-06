"""
Unit tests for the EconomicFeasibilityAnalyzer.
"""

import pytest
from core.economic_feasibility import EconomicFeasibilityAnalyzer

@pytest.fixture
def analyzer():
    """Returns an instance of EconomicFeasibilityAnalyzer."""
    return EconomicFeasibilityAnalyzer()

def test_estimate_roi(analyzer):
    """Test the ROI estimation."""
    features = {
        "market_size": 0.8,
        "revenue_potential": 0.7,
        "cost": 0.3,
        "trend": 0.6,
        "sentiment": 0.5
    }
    roi = analyzer.estimate_roi(features)
    assert 0 <= roi <= 1
    # A high-potential idea should have a high ROI
    assert roi > 0.7

def test_estimate_risk(analyzer):
    """Test the risk estimation."""
    features = {
        "uncertainty": 0.7,
        "complexity": 0.6,
        "volatility": 0.8,
        "regulatory_risk": 0.5,
        "provenance": 0.4
    }
    risk = analyzer.estimate_risk(features)
    assert 0 <= risk <= 1
    # A risky idea should have a high risk score
    assert risk > 0.6

def test_compute_pareto_score(analyzer):
    """Test the Pareto score calculation."""
    high_roi = 0.9
    low_risk = 0.2
    pareto_high = analyzer.compute_pareto_score(high_roi, low_risk)
    assert 0 <= pareto_high <= 1
    assert pareto_high > 0.7

    low_roi = 0.3
    high_risk = 0.8
    pareto_low = analyzer.compute_pareto_score(low_roi, high_risk)
    assert 0 <= pareto_low <= 1
    assert pareto_low < 0.4

def test_analyze_feasibility(analyzer):
    """Test the full feasibility analysis."""
    features = {
        "market_size": 0.8,
        "revenue_potential": 0.7,
        "cost": 0.3,
        "trend": 0.6,
        "sentiment": 0.5,
        "uncertainty": 0.2,
        "complexity": 0.3,
        "volatility": 0.2,
        "regulatory_risk": 0.1,
        "provenance": 0.9
    }
    result = analyzer.analyze_feasibility(features)
    assert "roi" in result
    assert "risk" in result
    assert "pareto_score" in result
    assert result["recommendation"] == "Good investment candidate"
