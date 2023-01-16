from postal.parser import parse_address as pa
import re


def parse_address(input_address: str) -> {}:
    res = {}
    parsed_address = pa(input_address)
    res.update({"street": item[0].capitalize() for item in parsed_address if item[1] == 'road'})
    res.update({"housenumber": item[0].capitalize() for item in parsed_address if item[1] == 'house_number'})
    actual_res = {key: re.search(value, input_address, re.IGNORECASE).group() for key, value in res.items()}
    return actual_res


if __name__ == "__main__":
    parse_address("1600 Pennsylvania Ave")
    parse_address("Winterallee 3")
    parse_address("Musterstrasse 45")
    parse_address("Blaufeldweg 123B")
    #
    parse_address("Am Bächle 23")
    parse_address("Auf der Vogelwiese 23 b")

    parse_address("4, rue de la revolution" )
    parse_address("200 Broadway Av")
    parse_address("Calle Aduana, 29")
    parse_address("Calle 39 No 1540")
