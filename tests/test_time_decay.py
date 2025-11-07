"""
Unit tests for the TimeDecayModule.
"""

import pytest
from datetime import datetime, timedelta
from core.time_decay import TimeDecayModule

@pytest.fixture
def time_decay_module():
    """Returns an instance of TimeDecayModule."""
    return TimeDecayModule()

def test_calculate_freshness_new(time_decay_module):
    """Test the freshness calculation for a new idea."""
    timestamp = datetime.now()
    freshness = time_decay_module.calculate_freshness(timestamp)
    assert freshness > 0.99

def test_calculate_freshness_old(time_decay_module):
    """Test the freshness calculation for an old idea."""
    timestamp = datetime.now() - timedelta(days=365)
    freshness = time_decay_module.calculate_freshness(timestamp)
    assert freshness < 0.1
