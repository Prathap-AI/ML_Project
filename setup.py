
###In Python, setup.py is a module used to build and distribute Python packages.
### It typically contains information about the package, such as its name, version, and dependencies, as well as instructions for building and installing the package.


from setuptools import find_packages, setup
from typing import list 
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)-> list [str]:
    ''' 
    this function will retuen the list of requirements 
    '''
    requirements=[]
    with open(file_path) as file_obj:  
        requirements= file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(

name='mlproject',
version='0.0.1',
author='prathap',
author_email='prathapsm.ai@gmail.com',
packages='find_package()',
install_requires=get_requirements('requirements.txt')


)