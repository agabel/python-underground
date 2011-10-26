import unittest
from weather import weather

KEY = 'af3292e8dba2ce2f'
LOCATION = 'KS/Hays'

class WeatherTestCase(unittest.TestCase):

    def setUp(self):
        self.client = weather.Client(key=KEY)


    def test_conditions(self):
        response = self.client.request(features=['conditions'], location=LOCATION)
        
        self.assertIsNotNone(response)


    def test_multiple_features(self):
        response = self.client.request(features=['conditions', 'forecast'], location=LOCATION)
        self.assertIsNotNone(response)


    def test_features_by_location(self):
        response = self.client.get_features_by_city('Hays', 'KS', features=['conditions'])
        self.assertIsNotNone(response)

        response = self.client.get_features_by_city(city='Sidney', country='Australia', features=['conditions'])
        self.assertIsNotNone(response)

        try:
            response = self.client.get_features_by_city(city='Wichita', features=['conditions'])
            raise self.failureException
        except weather.WeatherInvalidLocation:
            self.assertIsNotNone(response)



    def test_features_by_ip(self):
        response = self.client.get_features_by_ip('24.225.1.168', features=['conditions'])
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
