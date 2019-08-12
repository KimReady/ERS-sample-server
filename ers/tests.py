from django.test import TestCase
from datetime import datetime

# Create your tests here.
class SimpleTest(TestCase):

    def test_current_time(self):
        now = datetime.now()
        print(now)
        time = now.strftime("%Y-%m-%d %H:%M:%S")
        print(time)
