from setuptools import find_packages, setup
from typing import List



def get_requirements(file_path):
    """
    This function reads the requirements file and returns a list of packages.
    """
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

    return requirements


setup(
	name='mlproject',
	version='0.0.1',
	author='Shabhi',
	author_email='shabhialiyya3101@gmail.com',
	packages=find_packages(),
	install_requires= get_requirements('requirements.txt'),
)