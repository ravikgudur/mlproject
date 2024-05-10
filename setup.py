from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This function will read the requirements.txt file and return the list of requirements
    """
    requirements = []
    with open(file_path, "r") as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="mlproject",
    version="0.1",
    author="Ravik",
    author_email="trymeoutt@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    include_package_data=True,
    description="This is a ML project",
    license="MIT",
    url="https://github.com/Ravik12345/MLProject",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
