from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
        This function will return list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [r.replace("\n", "") for r in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name="ML-Project",
    version="0.0.1",
    author="afirahzahid",
    author_email="afirahzahid14@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirement.txt"),
    python_requires='>=3.8',
)