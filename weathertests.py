import unittest
import weather

KEY = ''
LOCATION = ''

class WeatherTestCase(unittest.TestCase):

    def setUp(self):
        self.client = weather.Client(key=KEY)

    def test_conditions(self):
        response = self.client.request(features=['conditions'], location=LOCATION)
        
        self.assertIsNotNone(response)


    def test_multiple_features(self):
        response = self.client.request(features=['conditions', 'forecast'], location=LOCATION)
        self.assertIsNotNone(response)

        


if __name__ == "__main__":
    unittest.main()
