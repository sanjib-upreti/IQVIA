import unittest
from disease_activity import days
# importing the disease_activity module for testing

class TestDiseaseActivity(unittest.TestCase):
    
    # Test 1
    def test_days_positive_integer(self):
        self.assertEqual(type(days),int)
        # testing the number of days, must be a positive integer
    
    # Test 2
    def test_days_max_30(self):
        self.assertTrue(days<=30)
        # testing input must not exceed from 30
        
    # Test 3
    def test_days_not_zero(self):
        self.assertTrue(days>0)
        # testing input must be zero or negative number
        

        
