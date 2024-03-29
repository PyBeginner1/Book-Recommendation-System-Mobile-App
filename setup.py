from setuptools import setup, find_packages
from typing import List 


def get_requirements_list()->List[str]:
    with open('requirements.txt') as requirement_file:
        requirement_list=requirement_file.readlines() 
        requirement_list=[req.replace('\n','') for req in requirement_list]
        if "-e ." in requirement_list:
            requirement_list.remove("-e .")
    return requirement_list

setup(
    name='Book-Recommendation-System-Mobile-App',
    version="0.0.1",
    author='Shashvath',
    description='Books Recommendation System',
    packages=find_packages(),
    install_requires = get_requirements_list()
)