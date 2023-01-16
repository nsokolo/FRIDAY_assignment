from deepparse.parser import AddressParser
import re


class SimpleModel:
    street: str
    housenumber: str

    @staticmethod
    def validate_address(input_address: str):
        address_list = input_address.split(" ")
        if len(address_list) == 2:
            if not address_list[0].isdigit() and address_list[1].isdigit():
                return {"street": address_list[0], "housenumber": address_list[1]}


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
    print(parse_address("Winterallee 3"))
    print(parse_address("Musterstrasse 45"))
    print(parse_address("Blaufeldweg 123B"))

    print(parse_address("Am Bächle 23"))
    print(parse_address("Auf der Vogelwiese 23 b"))

    print(parse_address("4, rue de la revolution"))
    print(parse_address("200 Broadway Av"))
    print(parse_address("Calle Aduana, 29"))
    print(parse_address("Calle 39 No 1540"))
