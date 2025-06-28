from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the current directory.")
        
    return requirement_lst

setup(
    name = "Network-Analysis",
    version = "1.0.0",
    author = "Yash Agarwal",
    author_email = "y2907ash@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
