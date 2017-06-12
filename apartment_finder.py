import config_parser


class Apartment_Finder():
    def __init__(self):
        self.config_parser = config_parser.Configuration_Parser()
    
    def get_data(self, source_address):
        maps_url = self.config_parser.get_maps_url(source_address)
        print(maps_url)


def main():
    ap = Apartment_Finder()
    print()
    source_address = 'Times Square, Manhattan, NY 10036'
    ap.get_data(source_address)
    print()

if __name__ == '__main__':
    main()