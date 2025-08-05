# test_sushimaster.py
"""
Tests for SushiMaster module.
"""

import unittest
from sushimaster import SushiMaster

class TestSushiMaster(unittest.TestCase):
    """Test cases for SushiMaster class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SushiMaster()
        self.assertIsInstance(instance, SushiMaster)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SushiMaster()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
