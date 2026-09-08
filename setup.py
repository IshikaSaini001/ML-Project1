from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """this function will return the list of requirements"""
    with open(file_path) as file_obj:
        reqs = file_obj.readlines()
        reqs = [req.replace("\n", "") for req in reqs]

        if "-e ." in reqs:
            reqs.remove("-e .")

    return reqs

setup(
    name = "ML-Project-01",
    version = "0.0.1",
    author = "ishika",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)