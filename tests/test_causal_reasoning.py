"""
Unit tests for the CausalReasoningModule.
"""

import pytest
from core.causal_reasoning import CausalReasoningModule

@pytest.fixture
def causal_module():
    """Returns an instance of CausalReasoningModule."""
    module = CausalReasoningModule()
    features = {
        "sentiment": [0.1, 0.2, 0.8, 0.9],
        "trend": [0.2, 0.3, 0.7, 0.8]
    }
    outcomes = [0.1, 0.3, 0.9, 0.7]
    module.fit_causal_model(features, outcomes)
    return module

def test_fit_causal_model(causal_module):
    """Test the causal model fitting."""
    assert ("sentiment", "outcome") in causal_module.causal_effects
    assert ("trend", "outcome") in causal_module.causal_effects
    assert causal_module.causal_effects[("sentiment", "outcome")] > 0.8
    assert causal_module.causal_effects[("trend", "outcome")] > 0.8

def test_estimate_causal_effect(causal_module):
    """Test the causal effect estimation."""
    effect = causal_module.estimate_causal_effect("sentiment", "outcome")
    assert 0 <= effect <= 1
    assert effect > 0.8

def test_compute_causal_impact_score(causal_module):
    """Test the causal impact score calculation."""
    idea_features = {
        "sentiment": 0.9,
        "trend": 0.8
    }
    score = causal_module.compute_causal_impact_score(idea_features)
    assert 0 < score < 1
