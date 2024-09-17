from django.test import TestCase
from users.utilities.utility import return_today
from datetime import datetime as dt

# Create your tests here.
class TestUtilities(TestCase):
    
    def test_day (self):
        
        hoy = dt.now()
        
        self.assertEqual(hoy.day , return_today() )