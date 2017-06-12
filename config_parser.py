from configparser import SafeConfigParser
import os

class Configuration_Parser():
    def __init__(self):
        self.config = SafeConfigParser(os.environ)
        self.config.read("config.ini")
    
    def get_apartment_url(self):
        return self.config.get('apartments', 'apartments_url')

    def get_maps_url(self, source_address):
        url = ''
        url += self.config.get('maps', 'maps_url')
        url += 'units=' + self.config.get('maps', 'map_units')
        url += '&origins=' + source_address
        url += '&destinations=' + self.config.get('maps', 'destination_address')
        url += '&mode=' + self.config.get('maps','travel_mode')
        url += '&transit_mode=' + self.config.get('maps', 'transit_mode')
        url += '&transit_routing_preference=' + self.config.get('maps','transit_routing_preference')
        url += '&key=' + self.config.get('maps', 'maps_api_key')
        return url
        

