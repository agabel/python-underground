import urllib2
import simplejson

# Setting this for future use
API_VERSION = '1.0'

URL = 'http://api.wunderground.com/api'


FEATURES_STRATUS = (
    'autocomplete',
    'astronomy',
    'conditions',
    'forecast',
    'geolookup',
)

FEATURES_CUMULUS = FEATURES_STRATUS + (
    'forecast7day',
    'hourly',
    'satellite',
    'radar',
    'alerts',
)

FEATURES_ANVIL = FEATURES_CUMULUS + (
    'hourly7day',
    'yesterday',
    'webcams',
)

ADD_ONS = 'history'

FEATURES = (
    'geolookup',
    'conditions',
    'forecast',
    'astronomy',
    'radar',
    'satellite',
    'webcams',
    'history',
    'alerts',
    'hourly',
    'hourly7day',
    'forecast7day',
    'yesterday',
    'autocomplete',
)


class WeatherException(Exception): pass
class WeatherInvalidFeature(WeatherException): pass
class WeatherInvalidLocation(WeatherException): pass
class WeatherServerException(WeatherException): pass


class Client(object):

    def __init__(self, key, api_version=API_VERSION, timeout=None):
        self.key = key
        self.api_version = api_version
        self.timeout = timeout

        
    def get_features_by_city(self, city, state=None, country=None, features=[]):
        if country:
            location = '%s/%s' % (country, state)
        elif state:
            location = "%s/%s" % (state, city)
        else:
            raise WeatherInvalidLocation
        return self.request(features, location)


    def get_features_by_zipcode(self, zipcode, features=[]):
        return self.request(features, zipcode)


    def get_features_by_coordinates(self, lat, lng, features=[]):
        location = "%f/%f" % (lat, lng)
        return self.request(features, location=location)


    def get_features_by_ip(self, ip, features=[]):
        return self.request(features, location=ip)

    
    def request(self,features=[], location=''):

        feature_string = "/".join(features)
        uri = '%s/%s/%s/q/%s.json' % (URL, self.key, feature_string, location)

        response = urllib2.urlopen(uri,timeout=self.timeout)
        data = response.read()

        return simplejson.loads(data)

        




__all__ = ['Client', 'WeatherException', 'WeatherInvalidFeature', 'WeatherServerException']