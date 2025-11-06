"""
Unit tests for the IntegrityBlockchainLayer.
"""

import pytest
from core.blockchain import IntegrityBlockchainLayer

@pytest.fixture
def blockchain():
    """Returns an instance of IntegrityBlockchainLayer."""
    return IntegrityBlockchainLayer()

def test_create_genesis_block(blockchain):
    """Test the creation of the genesis block."""
    assert len(blockchain.chain) == 1
    genesis_block = blockchain.chain[0]
    assert genesis_block.index == 0
    assert genesis_block.previous_hash == "0"

def test_add_block(blockchain):
    """Test adding a new block to the chain."""
    blockchain.add_block("test_idea", "1"*64)
    assert len(blockchain.chain) == 2
    new_block = blockchain.chain[1]
    assert new_block.data["idea_id"] == "test_idea"
    assert new_block.data["idea_hash"] == "1"*64
    assert new_block.previous_hash == blockchain.chain[0].hash

def test_add_block_invalid_hash(blockchain):
    """Test adding a block with an invalid hash."""
    with pytest.raises(ValueError):
        blockchain.add_block("test_idea", "invalid_hash")

def test_verify_chain_integrity(blockchain):
    """Test the chain integrity verification."""
    blockchain.add_block("test_idea_1", "1"*64)
    blockchain.add_block("test_idea_2", "2"*64)

    # Test a valid chain
    verification = blockchain.verify_chain_integrity()
    assert verification["valid"]

    # Tamper with the chain
    blockchain.chain[1].data["idea_id"] = "tampered_idea"

    # Test an invalid chain
    verification = blockchain.verify_chain_integrity()
    assert not verification["valid"]
    assert len(verification["errors"]) > 0
