import config_parser
import scrapper
import json

class Apartment_Finder():
    def __init__(self):
        self.config_parser = config_parser.Configuration_Parser()
        self.scrapper = scrapper.Scrapper(self.config_parser)
    
    def print_data(self):
        apartments = self.scrapper.get_apartments_info()
        for apartment in apartments:
            print(apartment)

def main():
    ap = Apartment_Finder()
    print()
    ap.print_data()
    print()

if __name__ == '__main__':
    main()
