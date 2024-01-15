from setuptools import find_packages,setup
from typing import List

EVAR = "-e ."
def get_requirements(filepath:str) -> List[str]:
    """
    This function returns the list of requirements for the project
    """
    requirements=[]
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if EVAR in requirements:
            requirements.remove(EVAR)
    return requirements


setup(
    name = 'mlproject',
    version='0.0.1',
    author='Vidyasagar Reddy Kallem',
    author_email='sagarreddy.kallem@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)



