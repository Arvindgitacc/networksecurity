'''This setup.py file is used to package the project and its dependencies. It specifies the project name, version, description, author, and required packages.'''
from setuptools import setup, find_packages
from typing import List

requirement_lst: List[str] = []

def get_requirements() -> List[str]:
    '''Reads the requirements.txt file and returns a list of dependencies.'''
    try:
        with open('requirements.txt','r') as f:
            lines=f.readlines()
            for line in lines:
                requirement=line.strip()                
                if requirement and requirement!='-e .':                    
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")
    return requirement_lst

setup(
    name='Network_Security_Project',
    version='0.0.1',
    author='Arvind',
    author_email='aravindavp79@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)