import setuptools
import os

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

setuptools.setup(
    name="address_parser",
    version="1.0.0",
    author="Natalia Sokolowska",
    author_email="sokolowska.natalia.anna@gmail.com",
    description="Three different modules to parse address",
    install_requires=install_requires,
    packages=setuptools.find_packages(),
    scripts=['parse_address'],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
)