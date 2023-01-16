from deepparse.parser import AddressParser
import re


def parse_address(input_address: str) -> {}:
    res = {}
    address_parser = AddressParser(model_type="fastText", device=0, verbose=False)
    parsed_address = address_parser(input_address)
    street_name = " ".join(street[0] for street in parsed_address.address_parsed_components
                           if street[1] in ['StreetName'])
    house_number = " ".join(street[0] for street in parsed_address.address_parsed_components
                            if street[1] == 'StreetNumber')
    res.update({"street": re.search(street_name, input_address, re.IGNORECASE).group()})
    res.update({"housenumber": re.search(house_number, input_address, re.IGNORECASE).group()})
    return res


if __name__ == "__main__":
    inputs = [
        "Winterallee 3", "Musterstrasse 45",
        "Blaufeldweg 123B",
        "Am Bächle 23",
        "Auf der Vogelwiese 23 b",
        "4, rue de la revolution",
        "200 Broadway Av",
        "Calle Aduana, 29",
        "Calle 39 No 1540"
    ]
    for input_ad in inputs:
        print(parse_address(input_address=input_ad))
