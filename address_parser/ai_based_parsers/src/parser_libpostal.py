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
