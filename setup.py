from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Application that takes an XML file as input, such as the output of nmap after scanning the network and obtaining information about open TCP ports, and outputs two .txt files with summaries of that information',
    author='Abel Gómez Méndez',
    license='MIT',
)
