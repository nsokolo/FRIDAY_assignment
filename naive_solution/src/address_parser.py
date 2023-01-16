from __future__ import annotations
import re
from typing import Union


class BaseModel:
    street: str
    house_number: str

    def validate_address(self, input_address: str) -> Union[BaseModel, bool]:
        pass


class SimpleModel(BaseModel):
    def validate_address(self, input_address: str) -> Union[SimpleModel, bool]:
        input_split = re.split(' |, ', input_address)
        reg_exp = "([a-zA-ZäöüÄÖÜß]+\s*)+[,]*\s*[0-9]+\s*([a-zA-Z]+)*"
        if re.match(reg_exp, input_address):
            reg_exp = "(([a-zA-ZäöüÄÖÜß]+)\s)+[,]*[0-9]+\s([a-zA-Z]+)*"
            if re.match(reg_exp, input_address):
                self.street = " ".join(input_split[:-2])
                self.house_number = " ".join(input_split[-2:])
            else:
                self.street = " ".join(input_split[:-1])
                self.house_number = input_split[-1]
            return self
        else:
            return False


class NumberStreetModel(BaseModel):
    def validate_address(self, input_address: str) -> Union[NumberStreetModel, bool]:
        input_split = re.split(' |, ', input_address)
        reg_exp = "([0-9]+)([a-zA-Z]+)*[,]*(\s*[a-zA-ZäöüÄÖÜß]+)*"
        if re.match(reg_exp, input_address):
            self.street = " ".join(input_split[1:])
            self.house_number = input_split[0]
            return self
        else:
            return False


def model_to_dict(model: Union[NumberStreetModel, SimpleModel]) -> {}:
    return {"street": model.street, "housenumber": model.house_number}


def parse_address(input_address: str) -> {}:
    models_list = [NumberStreetModel(), SimpleModel()]
    result = [model.validate_address(input_address) for model in models_list
              if model.validate_address(input_address)][0]
    return model_to_dict(result)


if __name__ == '__main__':
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
