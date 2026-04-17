# test_mangomarket.py
"""
Tests for MangoMarket module.
"""

import unittest
from mangomarket import MangoMarket

class TestMangoMarket(unittest.TestCase):
    """Test cases for MangoMarket class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MangoMarket()
        self.assertIsInstance(instance, MangoMarket)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MangoMarket()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
