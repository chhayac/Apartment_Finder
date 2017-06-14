from config_parser import Configuration_Parser
import urllib.request
import ssl
from bs4 import BeautifulSoup


class Apartment():
    def __init__(self):
        self.property_name = ''
        self.url = ''
        self.rent = ''
        self.distance = ''
        self.contact = ''
        self.address = ''
        self.description = ''

    def get_property_name(self):
        return self.property_name

    def set_property_name(self, property_name):
        self.property_name = property_name

    def get_url(self):
        return self.url
    
    def set_url(self, url):
        self.url = url

    def get_rent(self):
        return self.rent

    def set_rent(self, rent):
        self.rent = rent

    def get_distance(self):
        return self.distance
    
    def set_distance(self, distance):
        self.distance = distance

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_contact(self):
        return self.contact

    def set_contact(self, contact):
        self.contact = contact

    def __str__(self):
        apartmentString = '==============\n' + self.property_name + '\n' + self.rent + '\n'
        return apartmentString

class Scrapper():
    def __init__(self, config):
        self.config = config
        self.url = config.get_apartment_url()
        self.apartments = []
        request = urllib.request.Request(self.url)
        response = urllib.request.urlopen(request, context=ssl._create_unverified_context())
        page = response.read()
        soup = BeautifulSoup(page, 'html.parser')
        self.soup = soup.find('div', class_ = "placardContainer")
        self.soup.prettify()


    def get_apartments_info(self):
        for item in self.soup.find_all('article', class_ = 'placard'):
            
            apartment = Apartment()

            property_name = item.find('a', class_='placardTitle').get('title')
            if property_name is not None:
                apartment.set_property_name(property_name)
            

            url = item.find('a', class_ = 'placardTitle').get('href')
            if url is not None:
                apartment.set_url(url)

            rent= item.find('span',class_ = "altRentDisplay")
            if rent is not None:
                apartment.set_rent(rent.getText().strip())
            
            contact = item.find('div', class_ = 'phone')
            if contact is not None:
                apartment.set_contact(contact)

            self.apartments.append(apartment)

        return self.apartments



