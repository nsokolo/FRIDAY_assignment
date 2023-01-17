# Address Parser
**Home project for FRI:DAY recruitment process.**  

The goal of the project was to provide a tool for parsing unstructured address string to structured json-like 
format with the following structure:
```
{"street": streetname, "housenumber": number_of_the_house}
```

Two different approaches were explored:
 - naive solution of parsing addresses with regexes
 - using available ai-based open source projects (**deepparser** and **libpostal**).  

Advantages and disadvantages of both approaches are discussed in *Few Comments* section.

## Requirements
- Python 3.9


## Package structure 

```
FRIDAY_assignment/
├── README.md
├── address_parser/  
│   └── __init__.py
│   └── .gitignore
│   └── parse_address
│   └── setup.py
│   └── requirements.txt
│   └── pyproject.toml
│   └── naive_solution/
│       └──  __init__.py  
│       └── src/
│           └── __init__.py  
│           └── address_parser.py  
│       └── tests/
│           └── test_*.py  
│   └── ai_based_parses/
│       └──  __init__.py  
│       └── src/
│           └── __init__.py  
│           └── parser_deepparser.py  
│           └── parser_libpostal.py  
│       └── tests/
│           └── test_*.py   
```
The source code (**src/**) for both approaches and related unit tests (**tests/**) are 
located in **address_parses/*approach***. 
The **address_parses/** folder contains `reqiremets.txt`, `setup.py`, `pyproject.toml` and `parse_address` executable for 
simple CLI tool.

## Installation
- second solution requires compilation of the **libpostal** library. 
Here you can find instructions to follow: https://github.com/openvenues/libpostal   
Please, make sure you have **libpostal** installed before moving to next steps
- create new virtual environment:
```sh
python3 -m venv venv
```
- activate it:
```sh
source venv/bin/activate
```
- run `pip install` to install package and its dependencies:
```sh
pip install ./address_parser
``` 
To test if installation was successful run `parse_address test`. You should see the following output:
```
Yay! It works, you can parse your address now!
```

## Usage 
```
usage: parse_address parse [-h] [--function {deepparser,libpostal,naive}] --address ADDRESS [ADDRESS ...]

optional arguments:
  -h, --help            show this help message and exit
  --function {deepparser,libpostal,naive}
                        You can specify which module you want to use to parse your address. If not provided, all three will be executed
  --address ADDRESS [ADDRESS ...]
                        Address you want to parse, required
```
Examples of usage:
- `parse_address parse  --address "4, rue de la revolution"`  
will parse "4, rue de la revolution" into json-like format using all three implemented modules:
```
deepparser result: {'street': 'rue de la revolution', 'housenumber': '4'}
libpostal result: {'street': 'rue de la revolution', 'housenumber': '4'}
naive result: {'street': 'rue de la revolution', 'housenumber': '4'}
```
- `parse_address parse --function naive  --address "4, rue de la revolution"`  
will parse "4, rue de la revolution" into json-like format using only chosen (naive) module:
```
naive result: {'street': 'rue de la revolution', 'housenumber': '4'}
```
- `parse_address parse --function naive  --address "4, rue de la revolution" "Calle 39 No 1540" ...`
will parse all provided addresses into json-like format using only chosen (naive) module:
```
naive result: {'street': 'rue de la revolution', 'housenumber': '4'}
naive result: {'street': 'Calle 39', 'housenumber': 'No 1540'}
...
```

## Few comments

Each implemented function has its own advantages and disadvantages. Here are the most important ones:

### naive solution
**Pros:**
- it's very light and fast 
- it's not complex
- doesn't need external packages

 **Cons**
- questionable scalability - each time new address format arrives it will need dev to add address model,
so it can be parsed. This may lead to lage repository of models which can be difficult to maintain.

### deepparser package
**Pros:**
- it can be easily installed via pip
- it can be run on CPU (although it's relatively slow)
- works fine in most cases 
- can be fine-tuned (retrained) with additional dataset

 **Cons**
- slow without GPU
- without additional retraining it doesn't parse all provided examples


### postal package
**Pros:**
- works fine for all provided examples
- it can be run on CPU (although it's relatively slow)
- doesn't have to be fine-tuned

 **Cons**
- it works slow without GPU
- needs extra step for compiling `libpostal` lib
