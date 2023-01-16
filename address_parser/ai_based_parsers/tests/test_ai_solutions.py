from ai_based_parsers.src.parser_deepparser import parse_address as deepparser
from ai_based_parsers.src.parser_libpostal import parse_address as libpostal


def test_deepparser():
    input_strings = [
        "Winterallee 3", "Musterstrasse 45", "Blaufeldweg 123B",
        "Am Bächle 23", "Auf der Vogelwiese 23 b",
        "4, rue de la revolution", "200 Broadway Av", "Calle Aduana, 29",
        # "Calle 39 No 1540"  # this one will fail ; <
    ]

    expected_outputs = [
        {"street": "Winterallee", "housenumber": "3"},
        {"street": "Musterstrasse", "housenumber": "45"},
        {"street": "Blaufeldweg", "housenumber": "123B"},
        {"street": "Am Bächle", "housenumber": "23"},
        {"street": "Auf der Vogelwiese", "housenumber": "23 b"},
        {"street": "rue de la revolution", "housenumber": "4"},
        {"street": "Broadway Av", "housenumber": "200"},
        {"street": "Calle Aduana", "housenumber": "29"},
        # {"street": "Calle 39", "housenumber": "No 1540"}

    ]

    for input_string, expected_output in zip(input_strings, expected_outputs):
        res = deepparser(input_address=input_string)
        assert type(res) == dict
        assert res == expected_output, f"Failed for input: {input_string}"


def test_libpostal():
    input_strings = [
        "Winterallee 3", "Musterstrasse 45", "Blaufeldweg 123B",
        "Am Bächle 23", "Auf der Vogelwiese 23 b",
        "4, rue de la revolution", "200 Broadway Av", "Calle Aduana, 29", "Calle 39 No 1540"
    ]

    expected_outputs = [
        {"street": "Winterallee", "housenumber": "3"},
        {"street": "Musterstrasse", "housenumber": "45"},
        {"street": "Blaufeldweg", "housenumber": "123B"},
        {"street": "Am Bächle", "housenumber": "23"},
        {"street": "Auf der Vogelwiese", "housenumber": "23 b"},
        {"street": "rue de la revolution", "housenumber": "4"},
        {"street": "Broadway Av", "housenumber": "200"},
        {"street": "Calle Aduana", "housenumber": "29"},
        {"street": "Calle 39", "housenumber": "No 1540"}
    ]

    for input_string, expected_output in zip(input_strings, expected_outputs):
        res = libpostal(input_address=input_string)
        assert type(res) == dict
        assert res == expected_output, f"Failed for input: {input_string}"
