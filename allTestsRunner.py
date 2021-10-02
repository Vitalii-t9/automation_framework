import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
from Tests.CreateAnAccount import CreteAnAccountTest
from Tests.SearchBox import SearchBoxTest
from Tests.SendMassageOnContactUsPage import SendMessageOnContactsUsPageTest
# Create test cases for test run
tc1 = unittest.TestLoader.loadTestsFromTestCase(CreteAnAccountTest)
tc2 = unittest.TestLoader.loadTestsFromTestCase(SearchBoxTest)
tc3 = unittest.TestLoader.loadTestsFromTestCase(SendMessageOnContactsUsPageTest)

fullTestSuit = unittest.TestSuite([tc1, tc2, tc3]) # full testrun is running all test cases

unittest.TextTestRunner().run(fullTestSuit)